#! /bin/bash

# Change directory to exe
exedir=$LMP_SRC

dname=data-wall
mkdir -p ${dname}

lmp=${exedir}/lmp_mpi

mpirun -np 8 ${lmp} -in sph_flow_porous_fixed_reactive_surface_2d.lmp -var dname ${dname}

# lmp=${exedir}/lmp_serial

# ${lmp} -in sph_fixed_reactive_surface_2d.lmp 

