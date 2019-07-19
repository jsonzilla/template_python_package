# template python package

Simple template of package OS independent for Python 3.7

## Publish
Int [The Python Package Index (PyPI)](https://pypi.org/) [register an account](https://pypi.org/account/register/).

### More info about package
[Packaging-projects](https://packaging.python.org/tutorials/packaging-projects/)

### Build require setuptools
```bash
python3 -m pip install --user --upgrade setuptools wheel
```

### Send require twine 
```nbash
python3 -m pip install --user --upgrade twine
```

#### Build and upload
```bash
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### Installation
Some environment is pip3, check if get a error 
```bash
pip install your_package_name
```

### Usage from terminal (maybe)
```
python3 -m your_package_name
```

### Usage as a lib (maybe)
```python
from your_package_name import some_function
some_function(magic)
```		
