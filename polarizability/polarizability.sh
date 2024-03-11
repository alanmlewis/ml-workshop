#! /bin/bash

training_data=../gap_input_200.xyz

# Calculate descriptors
sagpr_get_PS -f $training_data -lm 0 -p -nc 200 -rc 4.0 -sg 0.3 -o PS0
sagpr_get_PS -f $training_data -lm 2 -p -nc 200 -rc 4.0 -sg 0.3 -o PS2

# Calculate kernels from these descriptors
sagpr_get_kernel -ps PS0.npy -z 2 -s PS0_natoms.npy -o kernel0
sagpr_get_kernel -ps PS2.npy -ps0 PS0.npy -z 2 -s PS2_natoms.npy -o kernel2

#Train and validate a model to predict the polarizability of water snapshots
sagpr_train -r 2 -p Polarizability -t 1.0 -f $training_data -k kernel0.npy kernel2.npy -reg 1e-8 1e-5 -rdm 150 -ftr 0.1 -pr 
