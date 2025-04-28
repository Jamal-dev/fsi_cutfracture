from ngsolve import *

def nitsche_coupling(mesh, V, W, gamma=10):
    uf, vf = V.Tn(2)
    us, vs = W.Tn(2)
    n = specialcf.normal(mesh.dim)

    penalty = gamma*1/mesh.ne*
              InnerProduct(uf-us, vf-vs)*dx(skeleton=True, definedon=mesh.Boundaries("block"))
    symm    = InnerProduct(uf-us, grad(vf).trans*n) + InnerProduct(grad(uf).trans*n, vf-vs)
    return penalty + symm
