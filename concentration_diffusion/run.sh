#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

# lmp=${exedir}/lmp_mpi

# mpirun -np 4 ${lmp} -in sph_conc_diffusion_2d.lmp 

lmp=${exedir}/lmp_serial

${lmp} -in sph_conc_diffusion_2d.lmp 

