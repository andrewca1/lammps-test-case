#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=data
lmp=${exedir}/lmp_mpi
${lmp} -in poiseuille.lmp -var dname ${dname}

