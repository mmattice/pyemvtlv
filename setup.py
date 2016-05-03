#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='pyemvtlv',
      version='0.1.0',
      setup_requires=["setuptools_git >= 0.3", ],
      install_requires=["future >= 0.15.2", ],
      description='Python EMV TLV Encoder/decoder',
      author='Mike Mattice',
      author_email='mike.mattice@gmail.com',
      url='https://github.com/mmattice/pyemvtlv/',
      packages=find_packages(),
      include_package_data=True,
      )
