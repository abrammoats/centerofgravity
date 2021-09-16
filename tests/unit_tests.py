# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 14:40:47 2021

@author: Abram Moats
"""
#
# Download https://github.com/abrammoats/centerofgravity as a ZIP file and
# put subfolder into C:\
#
# You should have a directory at this path when done correctly: 
# C:\centerofgravity\centerofgravity\centerofgravity.py

import sys

if 'centerofgravity' not in sys.path:
    sys.path.insert(1, 'C:\\centerofgravity')
    
# the above code will all be deprecated as soon as this is ready to be
# published out to PyPi and a normal pip install can be used

from centerofgravity import centerofgravity as cog

# for now, all the code is in the centerofgravity.py file
# this will likely change as functionality increases

import unittest

# using unittest for now, can't see a reason not to

class tests(unittest.TestCase):
    """
    I actually have very little understanding of what this class does on a
    nuts and bolts level but it seems like it's just a container for a
    bunch of different tests
    """

    

if __name__ == '__main__':
    unittest.main()
