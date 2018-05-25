#! /bin/bash

# Change directory to exe
exedir=/home/andrew/lmpsproject/qlammps/lammps/src
dname=data-wall
mkdir -p ${dname}

# lmp=${exedir}/lmp_mpi

# mpirun --mca orte_base_help_aggregate 0 -np 2 ${lmp} -in sph_multiphase_precipitation_wall_2d.lmp 

lmp=${exedir}/lmp_serial

${lmp} -in sph_multiphase_precipitation_wall_2d.lmp -var dname ${dname}
