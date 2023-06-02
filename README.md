# engine

## Install

### Linux

#### OpenVDB

``` sh
dnf install -y openvdb openvdb-devel python3-openvdb
```

#### Python packages

``` sh
python -m venv .venv --system-site-packages
source .venv/bin/activate
pip install "wheel"
pip install ".[dev]"
```
