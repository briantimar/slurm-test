#!/bin/bash
#SBATCH --job-name=script-test
#SBATCH --nodes=1
#SBATCH --output=/home/btimar/data/script-test.out
#SBATCH --time=0:0:01

pwd
echo "SLURM_JOB_ID=$SLURM_JOB_ID"
date

module load python
python script-test.py
date