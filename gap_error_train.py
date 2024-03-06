import numpy as np
import ase.io
from quippy.potential import Potential

f = open('gap_fit_clean.cfg')
a = f.readline().split('=')[1].strip()
print(a)
pos = ase.io.read(a,':')

gap = Potential(param_filename='gap.xml')
gap_energy = []
energy = []
for atoms in pos:
    energy.append(atoms.info['energy'])
    atoms.set_calculator(gap)
    gap_energy.append(atoms.get_potential_energy())

np.savetxt('train_errors.out',np.vstack([energy,gap_energy]).T)

MSE = np.sum(np.square([energy[i]-gap_energy[i] for i in range(len(pos))]))
print(MSE)