//==============================================================
// Copyright © 2022 Intel Corporation
//
// SPDX-License-Identifier: MIT
// =============================================================
// clang-format off
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <omp.h>

#define length 1024 * 1024 * 128 * 8

int main(void)
{
  int num_devices = omp_get_num_devices();
  int device_id = omp_get_default_device();
  int host_id = omp_get_initial_device();
  printf("Number of available devices %d\n", num_devices);  
  printf("Using device %d / %d   host_id: %d \n", device_id, num_devices, host_id );  
  


  size_t bytes = length*sizeof(double);
  double * d_A;
  double * d_B;
  double * d_C;
  double * h_A;
  double * h_B;
  double * h_C;
  double scalar = 3.0;
  double ar;
  double br;
  double cpu_sum = 0;
  double gpu_sum = 0;
  double ts, te, tgpu, tcpu;  
  int n_iter = 1000;

  h_A = (double *) malloc( bytes );
  h_B = (double *) malloc( bytes );
  h_C = (double *) malloc( bytes );

  for (size_t i=0; i<length; i++) {
    h_A[i] = 2.0;
    h_B[i] = 2.0;
    h_C[i] = 0.0;
  }

  ts = omp_get_wtime();  
  for (size_t i=0; i<length; i++) {
    h_C[i] = h_A[i] + scalar * h_B[i];
  }

  for (size_t i=0; i<length; i++) {
    cpu_sum += fabs(h_C[i]);
  }
  te = omp_get_wtime();
  tcpu = te - ts;

  printf("Time in host: %lf     \n", tcpu );
  



  // Allocate arrays in device memory
  d_A = (double *) omp_target_alloc(bytes, device_id);
  if (d_A == NULL){
     printf(" ERROR: Cannot allocate space for A using omp_target_alloc_device().\n");
     exit(1);
  }

  d_B = (double *) omp_target_alloc(bytes, device_id);
  if (d_B == NULL){
     printf(" ERROR: Cannot allocate space for B using omp_target_alloc_device().\n");
     exit(1);
  }

  d_C = (double *) omp_target_alloc(bytes, device_id);
  if (d_C == NULL){
     printf(" ERROR: Cannot allocate space for C using omp_target_alloc_device().\n");
     exit(1);
  }

  // Initialize the arrays
  omp_target_memcpy(d_A, h_A, bytes, 0, 0, device_id, host_id );
  omp_target_memcpy(d_B, h_B, bytes, 0, 0, device_id, host_id );
  omp_target_memcpy(d_C, h_C, bytes, 0, 0, device_id, host_id );
 

  ts = omp_get_wtime();  



  for (int i=0; i<n_iter; i++){  

    // Perform the computation

    #pragma omp target teams distribute parallel for is_device_ptr(d_A,d_B,d_C)
    for (size_t i=0; i<length; i++) {
        d_C[i] = d_A[i] + scalar * d_B[i];
    }

    // Validate and output results

    #pragma omp target teams distribute parallel for is_device_ptr(d_A,d_B,d_C) reduction(+:gpu_sum)
    for (size_t i=0; i<length; i++) {
        gpu_sum += fabs(d_C[i]);
    }

  }

  te = omp_get_wtime();
  tgpu = (te - ts) / n_iter;
  printf("Time in device: %lf    n_iter: %d \n", tgpu, n_iter );

  gpu_sum /= n_iter;

  omp_target_free(d_A, device_id);
  omp_target_free(d_B, device_id);
  omp_target_free(d_C, device_id);

  double epsilon=1.e-8;
  if (fabs(gpu_sum - cpu_sum)/cpu_sum > epsilon) {
      printf("Failed Validation on output array\n"
             "       Expected checksum: %lf\n"
             "       Observed checksum: %lf\n"
             "ERROR: solution did not validate\n", cpu_sum, gpu_sum);
      return 1;
  } else {
    printf( "SUCCESS! \n" );
  }

  


  return 0;
}
