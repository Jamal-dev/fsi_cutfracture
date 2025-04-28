from ngsolve import *

def make_spaces(mesh, order=2):
    # Fluid: Taylor–Hood P2–P1 on full mesh, but we’ll mask by level‑set
    V = VectorH1(mesh, order=order, dirichlet="wall")
    Q = H1(mesh, order=order-1)
    # Solid displacement (same order)
    W = VectorH1(mesh, order=order, dirichlet="block|wall")
    return V, Q, W
