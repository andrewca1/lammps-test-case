#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=data-wall
lmp=${exedir}/lmp_mpi
mkdir -p ${dname}

${lmp} -in ad_diff.lmp -var dname ${dname}

