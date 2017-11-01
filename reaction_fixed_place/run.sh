#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=results
mkdir -p ${dname}

lmp=${exedir}/lmp_serial

${lmp} -in sph_reaction_fixed_place_2d.lmp -var dname ${dname}

