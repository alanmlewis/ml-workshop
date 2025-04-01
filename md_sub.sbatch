#!/bin/bash -l
# Standard output and error:
#SBATCH -o ./md_run.out
#SBATCH -e ./md.err
# Initial working directory:
##SBATCH -D ./
# Job Name:
#SBATCH -J ML
# Queue (Partition):
#SBATCH --partition=nodes
#SBATCH --nodes=1
#SBATCH --ntasks=1
# for OpenMP:
#SBATCH --cpus-per-task=8
#
# Memory usage of the job [MB], 3800 MB per task:
#SBATCH --mem-per-cpu=3800
#
#SBATCH --mail-type=none
#
# Wall clock limit:
#SBATCH --time=0:10:00

### SET UP ENVIRONMENT VARIABLES: (uncomment and edit as needed)

ulimit -s unlimited
ulimit -c 0

export OMP_NUM_THREADS=8
export OPENBLAS_NUM_THREADS=1

### RUN YOUR CODE:

source venv/bin/activate

python molecular_dynamics.py 
