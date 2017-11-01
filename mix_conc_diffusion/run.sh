#! /bin/bash

# Change directory to exe
exedir=/home/qth20/Documents/lammps-sph/lammps/src

dname=results
mkdir -p ${dname}

lmp=${exedir}/lmp_serial

${lmp} -in sph_mix_conc_diffusion_2d.lmp -var dname ${dname}

