#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

lmp=${exedir}/lmp_serial

${lmp} -in sph_porous_conc_diff_2d.lmp 

