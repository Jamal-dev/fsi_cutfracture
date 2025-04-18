from mpi4py import MPI
from dolfinx.mesh import create_rectangle, CellType
from dolfinx.io import XDMFFile

# Dummy placeholder for now — CutFEM will come later
domain = create_rectangle(MPI.COMM_WORLD, [[0, 0], [4, 1]], [64, 16], CellType.triangle)

with XDMFFile(MPI.COMM_WORLD, "output/mesh.xdmf", "w") as xdmf:
    xdmf.write_mesh(domain)
