#! /bin/bash

# Change directory to exe
exedir=$LMP_SRC

lmp=${exedir}/lmp_mpi

mpirun --mca orte_base_help_aggregate 0 -np 8 ${lmp} -in sph_porous_fixed_reactive_surface_2d.lmp 

# lmp=${exedir}/lmp_serial

# ${lmp} -in sph_porous_fixed_reactive_surface_2d.lmp 

