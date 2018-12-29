
import os
import sys
from setuptools import setup, find_packages


# Read func for long description
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

requirements = []
with open('requirements.txt') as f:
	requirements = f.read().strip().split('\n')
setup(
	name="datasci",
	author="Navdeep",
	author_email="navdeepghai1@gmail.com",
	description=("A high level framework to work with excel, pdf, and html files"),
	long_description=read("README.rst"),
	license="MIT",
	packages=find_packages(),
	install_requires=requirements,
	zip_safe=False,
	entry_points={"console_scripts":["data-sci = datasci.commands.cli:execute_from_command_line"]}
)
