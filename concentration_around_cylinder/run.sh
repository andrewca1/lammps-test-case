#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=data-wall
mkdir -p ${dname}

# lmp=${exedir}/lmp_mpi
# mpirun -np 4 ${lmp} -in flow.lmp -var dname ${dname}

lmp=${exedir}/lmp_serial
${lmp} -in flow.lmp -var dname ${dname}
