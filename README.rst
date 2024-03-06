Creating a Python environment
=============================

You may want to create a python environment specifically for this workshop. To do this, run

:code: `python -m venv ./venv`

This will create a folder called venv which will contain all of the python packages needed to run the workshop. You should activate this by running:

:code: `source venv/bin/activate`

Installing gap_fit
==================

To install gap_fit, run

:code: `pip install quippy-ase`

This should install gap_fit and all of its dependencies. To test this has installed correctly, run

:code: `gap_fit config_file=gap_config.cfg`

This program should take around 1 minute to complete, during which time you should see a lot of text produced, with the words 'Bye Bye' displayed near the end of this text. 

Installing TENSOAP
==================

To install the dependencies needed to run TENSOAP, run

:code: `pip install Cython sympy`

To install TENSOAP itself, first run:

:code: `git clone https://github.com/alanmlewis/TENSOAP.git`

This will create a new folder called TENSOAP in your workshop folder. You need to change directory into :code: `TENSOAP/soapfast`, and then run

:code: `make cython`

to complete the installation. Finally, to get simple access to the programs contained in TENSOAP, return the main directory for the workshop, and run

:code: `source TENSOAP/env.sh`


