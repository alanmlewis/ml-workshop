from ase.md.verlet import VelocityVerlet
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs
import numpy as np
import ase.io
from quippy.potential import Potential

gap = Potential(param_filename='gap.xml')
init_snapshot = ase.io.read('gap_validate.xyz')
init_snapshot.set_calculator(gap)

MaxwellBoltzmannDistribution(init_snapshot,temperature_K=300.,force_temp=True)

#dyn = VelocityVerlet(init_snapshot,timestep=0.5*fs,logfile='nve.log',trajectory='nve.traj'))

dyn = Langevin(init_snapshot,temperature_K=300,timestep=0.5*fs,logfile='nvt.log',friction=0.1/fs,trajectory='nvt.traj')

n_steps = 100
dyn.run(n_steps)

traj = ase.io.trajectory.Trajectory('nvt.traj')
ase.io.write('trajectory.xyz',traj,write_info=False)
