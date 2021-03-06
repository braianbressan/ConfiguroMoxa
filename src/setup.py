"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
import os

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, '../README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='ConfiguroMoxa',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0',

    description="Obtiene informacion, configuracion y configura Moxa SerialServers",
    long_description=long_description,
    long_description_content_type="text/markdown",

    # The project's main homepage.
    url="https://github.com/braian87b/ConfiguroMoxa",

    # Author details
    author="Braian Bressan",
    author_email="braianbressan@gmail.com",

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        
        # Operating System
        "Operating System :: Linux",
    ],

    # What does your project relate to?
    keywords='balanza moxa serial-server',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    
    scripts=['ConfiguroMoxa.py'] ,

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["ConfiguroMoxa"],

    entry_points='''
        [console_scripts]
        ConfiguroMoxa=ConfiguroMoxa:main
    ''',
    
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': [],
    },
)
