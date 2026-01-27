# Defactoring Pace of Change


This repository is a heavily modified *fork* of a GitHub [repository](https://github.com/tedunderwood/paceofchange) created by Ted Underwood and Jordan Sellers to host the code associated with their paper ["How quickly do literary standards change?"](http://figshare.com/articles/How_Quickly_Do_Literary_Standards_Change_/1418394)

This fork *defactors* their code into a single, executable [Jupyter Notebook](http://jupyter.org). Essentially, we have taken the code that replicates their analysis, put it into an easier to execute format (the Juypter Notebook), and added our own commentary on the code (using the affordances of the Notebook).

## Reading our Analysis

You can read a static version of our analysis of Underwood and Sellers's code by [visiting the notebook on Github](defactoring-pace-of-change.ipynb). However, if you are interested in *running* the notebook and the code, you should set up your Python environment with the following libraries:

* [numpy](https://numpy.org) 
* [pandas](https://pandas.pydata.org) 
* [matplotlib](https://matplotlib.org) 
* [sklearn](https://scikit-learn.org/stable/)
* [multiprocess](https://pypi.org/project/multiprocess/)

Most of the libraries are part of the standard python data science stack and are already installed by the [Anaconda Python Distribution](https://www.anaconda.com/products/individual).

The `multiprocess` library has been added by the defactoring process as a drop-in replacement to the `multiprocessing` module in the standard library. Due to the architecture of the `multiprocessing`, the Notebook will hang when executing the data analysis portion of the code (something to with allowing the other python threads to import `__main__` which is tricky in a Notebook environment). The third-party library `multiprocess` fixes this issue and allows the code execute correctly in a Jupyter Notebook environment. The `multiprocess` library can be installed via conda or pip using the following commands:

```bash
conda install -c conda-forge multiprocess
```
or

```bash
pip install multiprocess
```

Alternatively, you can use [uv](https://docs.astral.sh/uv/) to run the notebook with all dependencies automatically managed:

```bash
uv run jupyter notebook defactoring-pace-of-change.ipynb
```

Executing the entire notebook takes about 20 minutes on a reasonably modern laptop. It has been successfully executed in OS X, but not recently tested on Linux or Windows. 


