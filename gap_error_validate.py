import numpy as np
import ase.io
from quippy.potential import Potential

# Load the validation data
pos = ase.io.read('gap_validate.xyz',':')

print('gap_validate.xyz')
# Load the GAP potential
gap = Potential(param_filename='gap.xml')

# Create empty lists to contain the predicted and actual energies of each snaphot
gap_energy = []
energy = []
#Loop over every snapshot in the validation data
for atoms in pos:
    # Extract the true energy of the snaphot and save it
#    energy.append(atoms.info['energy'])
    energy.append(atoms.get_total_energy())
    # Associate the ML potential with the snapshot
    atoms.set_calculator(gap)
    # Predict the energy of the snapshot using the ML potential
    gap_energy.append(atoms.get_potential_energy())

# Save the true and predicted energies to a file
np.savetxt('validation_errors.csv',np.vstack([energy,gap_energy]).T,delimiter=',')

# Calculate and print the root square mean error in the predicted energies
RMSE = np.sqrt(np.average(np.square([energy[i]-gap_energy[i] for i in range(len(pos))])))
print('Root Mean Square Error in the energy =',RMSE, 'eV')
