# ft_package

A sample test package for Training Piscine Python for datascience

(1). Your main directory should have the following structure:

    ├── ft_package
    │   ├── count_in_list.py
    │   └── __init__.py
    ├── README.md
    ├── setup.py

    Within the ft_package directory, ensure that you include an __init__.py
    file where you import the functions you wish to include in your package.
    Additionally, all source code files (*.py) for your package must be
    located within this directory.
    
(2). setup.py

    a. Module Importation
    
    Import the setup and find_packages functions from the setuptools module.
    These functions are used to configure and build the package.

    b. Version Definition
    The VERSION variable is defined to store the package version.
    This allows for easy specification of the version in different places within the file while maintaining consistency.

    c. Package Configuration
    The setup() function is used to configure the package.
    Various important parameters are specified, such as the package name, version, a brief summary, the URL of the homepage, author and email address, license, classifiers, and Python requirements. These parameters provide information about the package and how it can be used.

    Classifiers: Classifiers are tags that describe different aspects of the package, such as its development status, intended audience, license, and programming language used. These classifiers help users understand the purpose and quality of the package.

    Python Requirements: The python_requires parameter specifies the minimum version of Python required to run the package. This ensures that the package is compatible with the specified versions of Python.

(3). Run this command to create your own package.

    python setup.py sdist bdist_wheel

(4). Install your own package locally with the following command

    pip install ./dist/ft_package-0.0.1.tar.gz

(5). Test

    python tester.py




