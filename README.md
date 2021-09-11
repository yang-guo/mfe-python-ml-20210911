# Development
## Installation
### Conda
1. Download conda for your platform: `https://www.anaconda.com/products/individual-d`
2. Run through installer 

## Setup
1. Create new conda env: `conda create --name mfe-python-ml python=3.8`
2. Active env: `conda activate mfe-python-ml`
3. Install dependencies: `pip install -r requirements.txt`

## Starting notebooks
1. Active env: `conda activate mfe-python-ml`
2. Run `jupyter-lab`

## Installing Kepler
1. Run `jupyter nbextension install --py --sys-prefix keplergl`
2. Run `jupyter nbextension enable --py --sys-prefix keplergl`
3. Run `jupyter labextension install @jupyter-widgets/jupyterlab-manager keplergl-jupyter`
