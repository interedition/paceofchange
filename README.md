# Defactoring Pace of Change


This repository is a heavily modified *fork* of a [repository](https://github.com/tedunderwood/paceofchange) by Ted Underwood and Jordan Sellers associated with their paper ["How quickly do literary standards change?"](http://figshare.com/articles/How_Quickly_Do_Literary_Standards_Change_/1418394).

This repository has cleared out most of their code and replaced it with a single [Jupyter Notebook](http://jupyter.org) that *defactors* their code. *Defactoring* is a process that (TODO). Essentially, we have taken the code that replicates their analysis, put it into an easier to execute format (the Juypter Notebook), and added our own commentary on the code (using the affordances of the Notebook).

## Reading our Analysis

You can read a static version of our analysis of Underwood and Sellers's code by [visiting the notebook on Github](defactoring-pace-of-change.ipynb). However, if you are interested in *running* the notebook and the code, follow the instructions below.


### Running the Dockered Version

To make the execution of the code as easy as possible we have include a `Dockerfile` that describes an immutable runtime environment

First, install [Docker](https://www.docker.com/products/docker). Docker provides an easy installer for [Mac](https://www.docker.com/products/docker#/mac) and [Windows](https://www.docker.com/products/docker#/windows). Once this is up and running you will have everything you need to be able to recreate the environment we used to defactor pace of change.

**IMPORTANT NOTE**: To execute this notebook you need to allocate at least **4 gigabytes** to Docker. This mainly affects Docker for Mac and Windows. By default Docker only allocates 2 gigabytes so you need to go into the Docker preferences and boost the amount of memory to 4 gigabytes.
Mac - https://docs.docker.com/docker-for-mac/#/preferences  
Windows - https://docs.docker.com/docker-for-windows/#advanced

From the root directory of the repository run the following command:

`docker build --rm -t paceofchange .`

The first time you run this command it will *take a long time.* This is because the Docker engine needs to download the virtual images containing the execution environment. At some point you'll see the terminal spit out something resembling:

`Successfully built 596404121e02`

This means the Docker image containing the environment, data, and code has been successfully built into a Docker image. Now you can run this Docker image as a Docker container and interact the Jupyter Notebook we assembled. To run the container execute the following command:

```
docker-compose up paceofchange
```


Now you can open up a browser and visit [http://localhost:8888](http://localhost:8888) and see the Jupyter Notebook server with the defactoring-pace-of-change.ipynb notebook file. [Open the notebook directly with this link](http://localhost:8888/notebooks/defactoring-pace-of-change.ipynb)

EVEN THOUGH THIS VERSION OF THE NOTEBOOK IS LIVE, IT IS IMMUTABLE. Any changes you make to this notebook will not be reflected in the Notebook file in the repository directory. To make changes follow the instructions for developers below.


## For Developers

Folks wishing to edit the notebook and have those changes be saved on their local machine will need to mount current director inside the running docker container. Any changes made to the notebook will change the copy of the notebook on the users machine (rather than the copy inside the Docker container). We have included a `docker-compose.yml` file that will launch the container and mount the current directory in the running container.

```
docker-compose up paceofchange-dev
```

When you visit [http://localhost:8888](http://localhost:8888) you should see all of the files in the current directory (including the `Dockerfile` and `docker-compose.yml` files).

If you make any changes to the Notebook (or other files) they will be tracked in git. You can commit those changes and issue a pull-request (if you don't have repository permissions.)
