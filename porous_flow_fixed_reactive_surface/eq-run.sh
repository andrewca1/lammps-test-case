#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=eq-data-wall
mkdir -p ${dname}

lmp=${exedir}/lmp_mpi

mpirun -np 8 ${lmp} -in eq_sph_flow_porous_fixed_reactive_surface_2d.lmp -var dname ${dname}

# lmp=${exedir}/lmp_serial

# ${lmp} -in sph_fixed_reactive_surface_2d.lmp 

