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
import pandas as pd

if 'centerofgravity' not in sys.path:
    sys.path.insert(1, 'C:\\centerofgravity')
    
# the above code will all be deprecated as soon as this is ready to be
# published out to PyPi and a normal pip install can be used

from centerofgravity import centerofgravity as cog

# for now, all the code is in the centerofgravity.py file
# this will likely change as functionality increases

import unittest

# using unittest for now, can't see a reason not to

options = dict()
options['numClusters'] = 5
options['latCol'] = 'LAT'
options['lonCol'] = 'LON'
options['splitCol'] = 'SCENARIO'
options['weightCol'] = 'WEIGHT'
options['randomSeed'] = 0
options['distanceCol'] = 'X_DISTANCE'
options['clusterAssignmentCol'] = 'X_CLUSTER'
options['centroidsCol'] = 'X_CENTROIDS'

# above is the sample dict used in the example provided with the package

class TestCase(unittest.TestCase):
    def test_type_check_same(self):
        self.assertEqual(cog.type_check("abc", str), None, "Function should not return anything")
        self.assertEqual(cog.type_check(1234, int), None, "Function should not return anything")
        self.assertEqual(cog.type_check(1.2, float), None, "Function should not return anything")
        self.assertEqual(cog.type_check(dict({'a': 123, 'b':234}), dict), None, "Function should not return anything")
        self.assertEqual(cog.type_check(pd.DataFrame([[0,1],[1,0]]), pd.DataFrame), None, "Function should not return anything")
    
    def test_type_check_differences(self):
        with self.assertRaises(TypeError) as cm:
            cog.type_check(1234, dict)
        the_exception = cm.exception
        self.assertEqual(type(the_exception), TypeError)
        self.assertEqual(the_exception.args[0], 'Expected dict; got int')
        with self.assertRaises(TypeError) as cm:
            cog.type_check([[1,0], [0,1]], pd.DataFrame)
        the_exception = cm.exception
        self.assertEqual(type(the_exception), TypeError)
        self.assertEqual(the_exception.args[0], 'Expected DataFrame; got list')
        
    def test_CenterOfGravityModel_init(self):
        with self.assertRaises(TypeError) as cm:
            cog.CenterOfGravityModel('Hi!')
        the_exception = cm.exception
        self.assertEqual(type(the_exception), TypeError)
        self.assertEqual(the_exception.args[0], 'Expected dict; got str')
        
        options = dict()
        x = cog.CenterOfGravityModel(options)
        self.assertEqual(options, x.options, 'The options attribute and the dictionary passed in as an option should be equal')
        
    def test_CenterOfGravityModel_train(self):
        
        x = cog.CenterOfGravityModel(options)
        
        with self.assertRaises(TypeError) as cm:
            x.train(124)
        the_exception = cm.exception
        self.assertEqual(type(the_exception), TypeError)
        self.assertEqual(the_exception.args[0], 'Expected DataFrame; got int')
        
        
if __name__ == '__main__':
    unittest.main()
    

