# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testInvalid(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput')

    def testInvalid2(self):
        self.assertEqual(classifyTriangle(-1,0,1),'InvalidInput')

    def testInvalid3(self):
        self.assertEqual(classifyTriangle(2,5,"aghhfdsyhsgdfhs"),'InvalidInput')

    def testNotTriangle(self):
        self.assertEqual(classifyTriangle(3,3,199),'NotATriangle')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(3,3,4),'Isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

