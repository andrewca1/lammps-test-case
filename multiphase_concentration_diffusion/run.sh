#! /bin/bash

# Change directory to exe
exedir=$LMP_SRC

lmp=${exedir}/lmp_mpi

mpirun --mca orte_base_help_aggregate 0 -np 4 ${lmp} -in sph_multiphase_conc_diffusion_2d.lmp 

# lmp=${exedir}/lmp_serial

# ${lmp} -in sph_multiphase_conc_diffusion_2d.lmp 

