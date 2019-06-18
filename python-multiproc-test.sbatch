#!/bin/bash
#SBATCH --job-name=python-multiproc
#SBATCH --nodes=1
#SBATCH --output=/home/btimar/data/python-multiproc.out
#SBATCH --time=0:01:00

module load python
date
echo "SLURM_JOB_ID=$SLURM_JOB_ID"
echo "SLURM_JOB_NUM_NODES=$SLURM_JOB_NUM_NODES"
echo "SLURM_CPUS_ON_NODE=$SLURM_CPUS_ON_NODE"
echo "SLURM_NTASKS=$SLURM_NTASKS"
python python-multiproc-test.py
date

