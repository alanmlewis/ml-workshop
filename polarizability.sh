#! /bin/bash

sagpr_get_PS -f gap_input_100.xyz -lm 0 -p -nc 200 -o PS0
sagpr_get_PS -f gap_input_100.xyz -lm 2 -p -nc 200 -o PS2

sagpr_get_kernel -ps PS0.npy -z 2 -s PS0_natoms.npy -o kernel0
sagpr_get_kernel -ps PS2.npy -ps0 PS0.npy -z 2 -s PS2_natoms.npy -o kernel2

sagpr_train -r 2 -reg 1e-8 1e-5 -f gap_input_100.xyz -k kernel0.npy kernel2.npy -p Polarizability -rdm 100 -pr -t 1.0
