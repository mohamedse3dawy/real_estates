# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in real_estates/__init__.py
from real_estates import __version__ as version

setup(
	name='real_estates',
	version=version,
	description='Real Estates property management system',
	author='Ramoletane Lekhanya',
	author_email='ramoletane@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
