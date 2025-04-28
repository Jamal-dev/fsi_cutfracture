from ngsolve import *
from .indicators import make_levelset

mu_f, rho_f = 1.0, 1.0
mu_s, lam_s, rho_s = 1e3, 1e3, 1e3


def fluid_forms(mesh, V, Q, levelset):
    uf, vf = V.Tn(2)
    pf, qf = Q.Tn(2)
    n = specialcf.normal(mesh.dim)

    # Cut integration: fluid region is phi>0
    fluid = {"domain_type":VOL, "domain_marker":lambda el: levelset(el.midpoint())>0}

    a = (rho_f*InnerProduct(grad(uf), grad(vf)) + 2*mu_f*InnerProduct(Symmetric(grad(uf)), Symmetric(grad(vf))))*dx(**fluid)
    b = (div(uf)*qf + div(vf)*pf)*dx(**fluid)
    return a+b


def solid_forms(mesh, W):
    us, vs = W.Tn(2)
    E = 0.5*(grad(us)+grad(us).trans) + 0.5*(grad(us).trans*grad(us))  # Green‑Lagrange
    S = lam_s*Trace(E)*Id(us.dim) + 2*mu_s*E
    a = InnerProduct(S, grad(vs))*dx("block")
    return a
