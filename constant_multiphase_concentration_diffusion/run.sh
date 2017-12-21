#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

# lmp=${exedir}/lmp_mpi

# mpirun --mca orte_base_help_aggregate 0 -np 4 ${lmp} -in sph_conc_diffusion_2d.lmp 

lmp=${exedir}/lmp_serial

${lmp} -in sph_multiphase_const_conc_diffusion_2d.lmp 

