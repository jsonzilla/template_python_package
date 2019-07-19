# template python package

Simple template of package OS independent for Python 3.7

## Publish
Int [The Python Package Index (PyPI)](https://pypi.org/) [register an account](https://pypi.org/account/register/).

### More info about package
[Packaging-projects](https://packaging.python.org/tutorials/packaging-projects/)

### Build
Require setuptools
```bash
python3 -m pip install --user --upgrade setuptools wheel
```

### Send
Require twine 
```nbash
python3 -m pip install --user --upgrade twine
```

```bash
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
