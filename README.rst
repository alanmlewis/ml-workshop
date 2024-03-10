Introduction
============

This workshop provides a simple introduction to machine-learned potentials and tensorial property prediction. In both cases, kernel-based Gaussian process regression is used to perform the machine learning, but the majority of the principles introduced can be straightforwardly translated to neural network models. It was originally written for the 2024 Spring School of the SFB 986. For background reading about the software packages used here, please refer to `A. P. Bartok and G. Csanyi, International Journal of Quantum Chemistry 115, 1051 (2015)`_ for gap_fit and `A. Grisafi, D. M. Wilkins, G. Csanyi, and M. Ceriotti, Physical Review Letters 120, 36002 (2018)`_ for TENSOAP.

If you encounter any problems with this workshop please report an issue through GitHub or e-mail me directly at alan.m.lewis@york.ac.uk. 


.. _A. P. Bartok and G. Csanyi, International Journal of Quantum Chemistry 115, 1051 (2015): https://onlinelibrary.wiley.com/doi/10.1002/qua.24927
.. _A. Grisafi, D. M. Wilkins, G. Csanyi, and M. Ceriotti, Physical Review Letters 120, 36002 (2018): https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.120.036002
.. _Git for Windows: https://gitforwindows.org/
.. _Windows Subsystem for Linux: https://learn.microsoft.com/en-us/windows/wsl/install
.. _here: https://www.disk-image.com/faq-bootmenu.htm

Windows Users
=============

Like many specialised software packages, the tools we will use for the workshop are not available on Windows. Therefore, users who run Windows have three options:

#. The first and best option is to log into a UNIX machine you have access to through your institution and complete the preparation steps listed below on that computer. Your institution probably has a guide as to how to do this using ``ssh`` in PowerShell; note that you will probably need to log in to your institution VPN to access the machine from off-campus, so please make sure that has been set up correctly.

#. It is possible to complete the workshop on your local Windows machine by installing `Windows Subsystem for Linux`_. However, this may be complex to set up, and requires approximately 10GB hard disk space. This can be achieved by running ``wsl --install`` from a Powershell window opened as an administrator and following the instructions shown on the terminal. You may need to enable Virtual Machine Platform within Windows (this can be done by opening "Turn Windows features on or off" from the start menu and checking the corresponding box), and changing your BIOS settings to enable virtual environments (how this is done will depend on your hardware; check `here`_ for the hotkey to enter the BIOS when you switch your computer on). You may need to run ``wsl --install`` multiple times before installation is complete. Once you have installed WSL and have a WSL terminal open, you will also need to install various software packages, using the following commands:

   ``sudo add-apt-repository universe
   sudo apt-get install git python3-pip vim
   export PATH=$PATH:/home/your_user_name/.local/bin``

   Once this is complete, continue to the preparation steps below.

#. Alternatively, I will provide USB sticks from which a simple installation of Ubuntu can be booted, with all of the necessary installations already complete. Try to find out how to enter the boot menu when you start your computer. This is usually done by tapping a hotkey repeatedly immediately after turn on your laptop. The specific hotkey depends on the manufacturer, but the hotkeys for a number of brands can be found on `here`_ (note that you want the Boot Menu hotkey, not the BIOS key).

Mac Users
=========

The software we will use can run on Macs, but if you've not done much coding before you will likely need to install some features before you can begin. Alternatively, you can run the workshop on a UNIX machine you have access to through your institution; in this case see option 1 for Windows users above.

The first tool is pip, which can be installed by running

 ``curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py``

from the terminal.

You will also need to install gfortran. This can be downloaded from `this website`_, making sure you choose the appropriate version for your computer hardware and operating system. If you're not sure, try downloading `this installer`_ first. Once you have downloaded this, it can be installed in the usual way (if you need help try `these instructions`_), and then running the gfortran application once from the Applications directory to complete the setup.

Once you have installed these two requirements, you should be able to work through the commands below successfully. Note that the first time you run a ``git clone`` command, you may be prompted to install developer tools. This is necessary, but may take around 20 minutes to complete. If you have difficulty installing gap_fit, please move on to the instructions to install TENSOAP.

.. _this website: https://github.com/fxcoudert/gfortran-for-macOS/releases
.. _this installer: https://github.com/fxcoudert/gfortran-for-macOS/releases/download/11.2-bigsur-intel/gfortran-Intel-11.2-BigSur.dmg
.. _these instructions: https://jumpcloud.com/support/install-apps-silently-on-macos-using-dmg-files

Preparing for the Workshop
==========================

Clone this repository
---------------------

To begin, clone this repository by running

 ``git clone https://github.com/alanmlewis/ml-workshop``

This will create a new folder called ``ml-workshop``; change directory into that folder using ``cd ml-workshop``. Everything else we do in the workshop will take place in this folder or a subfolder.

Creating a Python environment
-----------------------------

This section is optional, and should definitely be skipped if you are using Windows Subsystem for Linux.

You may want to create a python environment specifically for this workshop. To do this, run

 ``python3 -m pip install virtualenv
 ``python3 -m virtualenv ./venv``

This will create a folder called venv where we will install all of the python packages needed to run the workshop. You should activate this environment by running:

 ``source venv/bin/activate``

You should also set the number of parallel threads to use, probably to 4:

 ``export OMP_NUM_THREADS=4``

Installing gap_fit
------------------

To install gap_fit, run

 ``python3 -m pip install quippy-ase``

This should install gap_fit and all of its dependencies. To test this has installed correctly, run

 ``gap_fit config_file=gap_config.cfg``

This program should take a few seconds to complete, during which time you should see a lot of text produced, with the words 'Bye Bye' displayed near the end of this text. 

Installing TENSOAP
------------------

To install the dependencies needed to run TENSOAP, run

 ``python3 -m pip install Cython sympy numpy scipy ase``

To install TENSOAP itself, first run:

 ``git clone https://github.com/alanmlewis/TENSOAP.git``

This will create a new folder called TENSOAP in your workshop folder. You need to change directory into ``TENSOAP/soapfast``, and then run

 ``make cython``

to complete the installation. Finally, to get simple access to the programs contained in TENSOAP, return the main directory for the workshop (``cd ../..``), and run

 ``source TENSOAP/env.sh``

To test the installation of TENSOAP, change directory into ``polarizability``, and run the following command:

 ``sagpr_get_PS -f ../gap_input_50.xyz -lm 0 -p -nc 200 -o PS0``

This should take a few seconds, and produce four files: ``PS0.npy``, ``PS0_Amat.npy``, ``PS0_fps.npy``, and ``PS0_natoms.npy``.


Workshop Instructions
=====================

Detailed instructions for completing the full workshop are given in `this pdf`_.

.. _this pdf: https://github.com/alanmlewis/ml-workshop/blob/main/instructions/workshop.pdf
