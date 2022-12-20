COMP   = OMPI_CC=$(ROCM_PATH)/bin/hipcc mpicc
FLAGS = -fopenmp

MPI_HOME = /mnt/beegfs/home/balvarez/code/ompi
INCLUDES = -I${MPI_HOME}/include
LIBRARIES = -L${MPI_HOME}/lib -lmpi

hello_mpi_omp: hello_mpi_omp.o
	${COMP} ${FLAGS} ${LIBRARIES} hello_mpi_omp.o -o hello_mpi_omp

hello_mpi_omp.o: hello_mpi_omp.c
	${COMP} ${FLAGS} ${INCLUDES} -c hello_mpi_omp.c

PHONY: clean

clean:
	rm -f hello_mpi_omp *.o

