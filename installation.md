# Data Analysis Using [Python](https://www.python.org) - Environment Setup

## Install miniconda

- Download [Miniconda](https://docs.conda.io/en/latest/miniconda.html) based on your operating system
- Install Miniconda, please accept the default directory suggested by the installer

## Configure conda environment

- Add conda-forge channel
``` bash
conda config --show
conda config --show channels
conda config --add channels conda-forge
```
- Optional Setp: Add following proxy_server settings if necessary
```bash
conda config --set proxy_servers.http http://user:pass@corp.com:8080
conda config --set proxy_servers.https https://user:pass@corp.com:8080
```

## Create virtual environment

- Create virtual environment by name "training" using following command
``` bash
conda create -n training python=3.7
```
- Activate the environment
```bash
conda activate training
```

## Install necessary packages based on your project requirements

- install following packages
```bash
conda install jupyterlab pandas scikit-learn matplotlib
```



