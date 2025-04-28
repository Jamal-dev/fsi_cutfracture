
# FSI CutFEM + Phase‑Field Prototype (NGSolve/ngsxfem)

Minimal 2‑D example: incompressible Stokes flow over an elastic beam that may fracture
when the local fluid speed exceeds a threshold.  The code uses

* **NGSolve** for finite elements
* **ngsxfem** for CutFEM unfitted integration
* A simple phase‑field fracture model
* Symmetric Nitsche coupling on the fluid–solid interface

## Quick start

```bash
# create environment (Linux / conda):
conda env create -f env.yml
conda activate fsi-cutfracture

# run the demo:
python python/run.py
```

Results (velocity, pressure, displacement, damage) are written to `output/` as VTK
files and can be viewed in ParaView.

> **Note**  
> This is a research prototype—expect small time‑step restrictions and no adaptive
> time stepping.  For production, add stabilisation, non‑linear fluid, and MPI.
