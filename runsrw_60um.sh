#!/bin/bash -l
#SBATCH -N 5
#SBATCH -C haswell
#SBATCH -q debug
#SBATCH -J 60um
#SBATCH --tasks-per-node=5
#SBATCH --mail-user=ahe@bnl.gov
#SBATCH --mail-type=ALL
#SBATCH -L SCRATCH
#SBATCH -t 0:30:00

#run the application:
srun -n 51 python SRWLIB_Example_60um.py
