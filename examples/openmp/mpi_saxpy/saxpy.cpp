#include <cstdlib>
#include <stdio.h>
#include <omp.h>
#include <mpi.h>

#define SZ 1024 * 1024 * 128 * 10

int main( int argc, char* argv[] ) 
{

  MPI_Init(&argc, &argv);

  double a;
  double *h_x, *h_y;
  double *d_x, *d_y;

  a = 2.0;
  h_x = (double *) malloc( SZ*sizeof(double) );
  h_y = (double *) malloc( SZ*sizeof(double) );
  d_x = (double *) malloc( SZ*sizeof(double) );
  d_y = (double *) malloc( SZ*sizeof(double) );

  double t = 0.0;
  double ts, te;  
  
  printf( "Saxpy \n");
  int num_devices = omp_get_num_devices();
  printf("Number of available devices %d\n", num_devices);

// #pragma omp target
// #pragma omp teams num_teams(2) thread_limit(3)
// #pragma omp parallel 
// {
//     if (omp_is_initial_device()) {
//       printf("Running on host\n");    
//     } else {
//       int nteams= omp_get_num_teams(); 
//       int nthreads= omp_get_num_threads();
//       printf("Running on device with %d teams in total and %d threads in each team\n",nteams,nthreads);
//     }
// }

  for ( int i=0; i<SZ; i++ ){
    h_x[i] = i;
    d_x[i] = i;
    h_y[i] = 2*i;
    d_y[i] = 2*i;
  }



  ts = omp_get_wtime();
  #pragma omp parallel for
  for ( int i=0; i<SZ; i++ ){
    h_y[i] = a * h_x[i] + h_y[i];
  }
  te = omp_get_wtime();
  t = te - ts;
  printf("Time of kernel in host %1f \n", t );

  int n_iter = 1000;

  // Copy x and y arrays to the gpu.  
  #pragma omp target data map(to:d_x[0:SZ]) map(tofrom:d_y[0:SZ]) 
  { 

  ts = omp_get_wtime();
  for (int iter=0; iter<n_iter; iter++){
    
    
    #pragma omp target teams distribute parallel for 
      for ( int i=0; i<SZ; i++ ){
        d_y[i] = a * d_x[i] + d_y[i];
      }
    


  }
  }

  te = omp_get_wtime();


// #pragma omp target teams distribute parallel for simd \
//           map(to:d_x[0:SZ]) map(tofrom:d_y[0:SZ]) 
//   for ( int i=0; i<SZ; i++ ){
//     d_y[i] = a * d_x[i] + d_y[i];
//   }

  t = (te - ts) / n_iter;
  printf("Time of kernel in device  %1f   n_iter: %d \n", t, n_iter );



  // double diff;
  // for (int i=0; i<SZ; i++ ){
  //   diff = abs( d_y[i] - h_y[i] );
  //   if ( diff > 1e-6 ){ 
  //     printf("ERROR: Large difference: h_y: %e  d_y: %e  diff:%e \n", h_y[i], d_y[i], diff );
  //     break;
  //   }
  // }



  free(h_x);
  free(h_y);
  free(d_x);
  free(d_y);

  printf("Finished \n" );

  MPI_Barrier(MPI_COMM_WORLD);
  
  MPI_Finalize();
}