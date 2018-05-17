#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

# lmp=${exedir}/lmp_mpi

# mpirun --mca orte_base_help_aggregate 0 -np 2 ${lmp} -in sph_multiphase_precipitation_wall_2d.lmp 

lmp=${exedir}/lmp_serial

${lmp} -in sph_multiphase_precipitation_wall_2d.lmp 
