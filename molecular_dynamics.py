from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs
import numpy as np
import ase.io
from quippy.potential import Potential

# Load the GAP model
gap = Potential(param_filename='gap.xml')
# Load a validation snapshot to use as the starting point for our simulation
init_snapshot = ase.io.read('gap_validate.xyz')
# Associate the GAP model with this snapshot
init_snapshot.set_calculator(gap)
# Randomly sample velocities from the MB distribution at 300K for each atom
MaxwellBoltzmannDistribution(init_snapshot,temperature_K=300.,force_temp=True)

# Uncomment the command below to run dynamics at a constant energy
#dyn = VelocityVerlet(init_snapshot,timestep=0.5*fs,logfile='nve.log',trajectory='trajectory.traj'))

# Uncomment the command below to run dynamics at a constant temperature
dyn = Langevin(init_snapshot,temperature_K=300,timestep=0.5*fs,logfile='nvt.log',friction=0.1/fs,trajectory='trajectory.traj')

# Set the number of steps for the MD simulation
n_steps = 100
# Run the MD simulation
dyn.run(n_steps)

# Load the resulting trajectory file
traj = ase.io.trajectory.Trajectory('trajectory.traj')
# Write the trajectory file in a xyz format
ase.io.write('trajectory.xyz',traj,write_info=False)
