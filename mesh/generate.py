from netgen.geom2d import SplineGeometry
from ngsolve import *
from netgen.geom2d import CSG2d, Circle, Rectangle
from matplotlib import pyplot as plt
from ngsolve.webgui import Draw

# Create a 2D geometry for the mesh
def create_geometry(W,H,w_solid,h_solid,pos_x_solid,pos_y_solid,order,maxh=0.05):
    geo = CSG2d()
    fluid = Rectangle(pmin=(0,0), pmax=(W,H), mat="fluid", left="inlet", top="wall", bottom="wall", right="outlet")
    solid = Rectangle(pmin=(pos_x_solid,pos_y_solid), pmax=(pos_x_solid+w_solid,pos_y_solid+h_solid), mat="solid", left="solid_left", top="solid_top", bottom="solid_bottom", right="solid_right")
    domain_fluid = fluid - solid
    domain_solid = solid
    geo.Add(domain_fluid)
    geo.Add(domain_solid)
    # generate mesh
    mesh = Mesh(geo.GenerateMesh(maxh=maxh))
    mesh.Curve(order)
    
    return mesh

# Parameters
W = 4.0  # Width of the fluid domain
H = 1.0  # Height of the fluid domain
w_solid = 1.0  # Width of the solid block
h_solid = 0.4  # Height of the solid block
pos_x_solid = 1.0  # X position of the solid block
pos_y_solid = 0.0  # Y position of the solid block
order = 3  # Polynomial order for the mesh
maxh = 0.05  # Maximum mesh size
# Create the mesh
mesh = create_geometry(W, H, w_solid, h_solid, pos_x_solid, pos_y_solid, order, maxh)
# Visualize the mesh
Draw(mesh)
plt.show()


