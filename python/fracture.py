from ngsolve import *


def fracture_trigger(gfu, threshold=1.0):
    """Return True if max |u_f| in fluid region > threshold."""
    velocity = gfu.components[0]
    vmax = max(abs(velocity(x)) for x in velocity.space.mesh.Points())
    return vmax > threshold
