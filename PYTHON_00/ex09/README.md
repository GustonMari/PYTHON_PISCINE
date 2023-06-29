Inside the ft_package directory, create a ft_package subdirectory. This will serve as the package's root directory.

Create a Python file named count_in_list.py inside the ft_package subdirectory.

Update your setup.py file to include the necessary information for your package, such as the package name, version, author, license, etc. Make sure to specify the package directory as 'ft_package'.

pip install setuptools wheel

BUILD:
python setup.py sdist bdist_wheel

INSTALL:
pip install ./dist/ft_package-0.0.1.tar.gz

or

pip install ./dist/ft_package-0.0.1-py3-none-any.whl
