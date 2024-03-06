Introduction
============

This workshop provides a simple introduction to machine-learned potentials and tensorial property prediction. In both cases, kernel-based Gaussian process regression is used to perform the machine learning, but the majority of the principles introduced can be straightforwardly translated to neural network based models. It was originally written for the 2024 Spring School of the SFB 986. For introductory background to the software packages used here, please read `A. P. Bartok and G. Csanyi, International Journal of Quantum Chemistry 115, 1051 (2015)`_ for gap_fit and `A. Grisafi, D. M. Wilkins, G. Csanyi, and M. Ceriotti, Physical Review Letters 120, 36002 (2018)`_ for TENSOAP.

This workshop has been tested on Ubuntu and Windows machines, but not iOS. I believe it should run smoothly on iOS, but if you encounter any problems please report an issue through GitHub or e-mail me directly at alan.m.lewis@york.ac.uk. 

**Windows users** will need to install `Windows Subsystem for Linux`_ by running :code: `wsl --install` prior to any further steps, and use the WSL terminal to complete the steps shown below. You will also need to install git, using :code: `sudo apt-get install git`.

.. _A. P. Bartok and G. Csanyi, International Journal of Quantum Chemistry 115, 1051 (2015): https://onlinelibrary.wiley.com/doi/10.1002/qua.24927
.. _A. Grisafi, D. M. Wilkins, G. Csanyi, and M. Ceriotti, Physical Review Letters 120, 36002 (2018): https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.036002
.. _Git for Windows: https://gitforwindows.org/
.. _Windows Subsystem for Linux: https://learn.microsoft.com/en-us/windows/wsl/install

Preparing for the Workshop
==========================

Clone this repository
---------------------

To begin, clone this repository by running

 ``git clone https://github.com/alanmlewis/ml-workshop``

This will create a new folder called `ml-workshop`; change directory into that folder using `cd ml-workshop`. Everything else we do in the workshop will take place in this folder or a subfolder.

Creating a Python environment
-----------------------------

You may want to create a python environment specifically for this workshop. To do this, run

 ``python -m venv ./venv``

This will create a folder called venv where we will install all of the python packages needed to run the workshop. You should activate this by running:

 ``source venv/bin/activate``

or on Windows

 ``. venv/Scripts/activate/``

Installing gap_fit
------------------

To install gap_fit, run

 ``pip install quippy-ase``

This should install gap_fit and all of its dependencies. To test this has installed correctly, run

 ``gap_fit config_file=gap_config.cfg``

This program should take around 1 minute to complete, during which time you should see a lot of text produced, with the words 'Bye Bye' displayed near the end of this text. 

Installing TENSOAP
------------------

To install the dependencies needed to run TENSOAP, run

 ``pip install Cython sympy``

To install TENSOAP itself, first run:

 ``git clone https://github.com/alanmlewis/TENSOAP.git``

This will create a new folder called TENSOAP in your workshop folder. You need to change directory into ``TENSOAP/soapfast``, and then run

 ``make cython``

to complete the installation. Finally, to get simple access to the programs contained in TENSOAP, return the main directory for the workshop, and run

 ``source TENSOAP/env.sh``

To test the installation of TENSOAP, change directory into :code: `polarizabilities`, and run the following command:

 ``sagpr_get_PS -f ../gap_input_50.xyz -lm 0 -p -nc 200 -o PS0``

This should take a few seconds, and produce four files: `PS0.npy`, `PS0_Amat.npy`, `PS0_fps.npy`, and `PS0_natoms.npy`.


Workshop Instructions
=====================

Detailed instructions for completing the full workshop will be provided soon.
