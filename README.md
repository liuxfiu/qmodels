# Simulation of Queuing Models with Simulus

<img src="notebooks/figs/queue.jpg" align="left" width="35%" alt="queue">

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/liuxfiu/qmodels.git/master?filepath=notebooks%2Findex.ipynb)

This repository contains a tutorial describing how to use simulus to simulate queuing systems. Simulus is an open-source discrete-event simulator in Python. The tutorial consists of several Jupyter notebooks, on which we develop and run simulation code.

## How to Run this Tutorial

1. Launch a live notebook server with these notebooks using [binder](https://beta.mybinder.org/). Access the binder at the following URL: https://mybinder.org/v2/gh/liuxfiu/qmodels.git/master?filepath=notebooks%2Findex.ipynb

2. Run these notebooks available in this repository's [notebooks](notebooks) directory on your own machine. To do that, you need to install the following packages:
   * **jupyter**: a web application for sharing interactive documents that contain text, code, and data visualization
   * **numpy**: a library for efficient representation of multi-dimensional arrays
   * **scipy**: a library for numerical computations, including linear algebra and statistics
   * **matplotlib**: a 2-D plotting library

   You can install these packages using the `pip` command, such as the following:

   ```
   python -m pip install --user jupyter numpy scipy matplotlib
   ```

   You'll also need to install simulus. Check out [Simulus Quick Start](https://simulus.readthedocs.io/en/latest/readme.html) for installation instructions. The simplest method to install simulus is to run the `pip` command, such as:

   ```
   python -m pip install --user simulus
   ```
