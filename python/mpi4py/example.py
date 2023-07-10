from mpi4py import MPI
import lammps as lammps

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

lmp = lammps.lammps(comm=comm,
                    cmdargs=["-k", "on", "g", "4", "-sf", "kk"])

print(rank)
lmp.finalize()