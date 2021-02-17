# Parametrized Testing
> A parametrized testing example using pytest

## Required packages
```
pip install pytest pytest-tornasync
```

## How to use
The folder structure of this repository is as follows:
```
📦 .
 ┣ 📂myapp
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜triangles.py
 ┣ 📂tests
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜test_triangle_type.py
 ┣ 📜pytest.ini
 ┗ 📜setup.py
```
- `myapp` contains all functions
- `tests` contains all testing functions

Run following command to execute pytest
```
pytest tests/test_triangle_type.py
```
