### Python + LAMMPS in HPC environments

Goal: Use `srun` to run a LAMMPS Python script in parallel on multiple GPUs.

On Perlmutter, simply do:

    srun --ntasks-per-node=4 --gpus-per-node=4 python test-srun.py

    