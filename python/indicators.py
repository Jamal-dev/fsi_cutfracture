from ngsolve import *

def make_levelset(mesh, block_tag=2):
    """Return CoefficientFunction phi <0 inside solid block."""
    mat = mesh.GetMaterials()
    solid_cells = [(i,elm) for i,elm in enumerate(mesh.Elements(VOL)) if mat[elm.mat] == "block"]
    phi = CoefficientFunction([1])
    # tag solid elements with -1
    for idx, elm in solid_cells:
        phi.Set(-1, definedon=mesh.GetElementVDomains(elm))
    return phi
