#! /bin/bash

training_data=../gap_input_200.xyz

# Recalculate the model using all 200 training snapshots
sagpr_train -r 2 -p Polarizability -t 1.0 -f $training_data -k kernel0.npy kernel2.npy -reg 1e-8 1e-5 -sel 0 200

# Calculate descriptors of the new snapshots
sagpr_get_PS -f ../trajectory.xyz -lm 0 -p -sf PS0 -o PS0_pr
sagpr_get_PS -f ../trajectory.xyz -lm 2 -p -sf PS2 -o PS2_pr

# Calculate the kernels between the training snaphots and new snaphots
sagpr_get_kernel -ps PS0_pr.npy PS0.npy -z 2 -s PS0_pr_natoms.npy PS0_natoms.npy -o kernel0_pr
sagpr_get_kernel -ps PS2_pr.npy PS2.npy -ps0 PS0_pr.npy PS0.npy -z 2 -s PS2_pr_natoms.npy PS2_natoms.npy -o kernel2_pr

# Predict the polarizabilities of the new snapshots
sagpr_prediction -r 2 -k kernel0_pr.npy kernel2_pr.npy -o trajectory
