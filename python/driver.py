from ngsolve import *
from netgen.geom2d import unit_square
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent))  # add python/ to path
from indicators import make_levelset
from spaces import make_spaces
from forms import fluid_forms, solid_forms
from interface import nitsche_coupling

mesh = Mesh("../mesh/channel.vol")
phi = make_levelset(mesh)
V, Q, W = make_spaces(mesh)

F = fluid_forms(mesh, V, Q, phi) + solid_forms(mesh, W) + nitsche_coupling(mesh, V, W)

# Assemble and solve (single step, stationary)
fes = FESpace([V, Q, W])

u = GridFunction(fes, name="u")
res = BilinearForm(fes)
res += F
res.Assemble()

rhs = LinearForm(fes)
rhs.Assemble()

print("Solving …")
Solve(res.mat, u.vec, rhs.vec)
Print("||u||=", u.vec.Norm())

vtk = VTKOutput(ma=mesh, coefs=[u.components[0], u.components[1]],
                names=["v", "p"], filename="../output/solution", subdivision=1)
vtk.Do()
