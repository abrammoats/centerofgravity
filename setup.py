# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:19:49 2021

@author: Abram Moats
"""
  
from setuptools import setup

setup(name='centerofgravity',
      version='1.0.0',
      description='Automated Center of Gravity Mappying',
      url='http://github.com/smutchler/src',
      author='Scott Mutchler, Abram Moats',
      author_email='smutchler@trilabyte.com, abramdanielmoats@gmail.com',
      license='GPLv3',
      packages=['centerofgravity'],
      install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',
        'json',
        'math',
        'folium'
      ],
      zip_safe=False)


