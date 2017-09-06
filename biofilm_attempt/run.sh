#! /bin/bash

set -e
set -u

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src
lmp=${exedir}/lmp_mpi

mpirun=mpirun
dname=data

mpirun -np 8 ${lmp} -in bubble.lmp -var dname ${dname} 
# ${lmp} -in bubble.lmp -var dname ${dname} 
