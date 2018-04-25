#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=data-wall
mkdir -p ${dname}

lmp=${exedir}/lmp_mpi

mpirun --mca orte_base_help_aggregate 0 -np 8 ${lmp} -in sph_inlet_flow_fixed_reactive_surface_2d.lmp -var dname ${dname}

# lmp=${exedir}/lmp_serial

# ${lmp} -in sph_fixed_reactive_surface_2d.lmp 

