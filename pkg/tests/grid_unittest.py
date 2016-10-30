import logging
import unittest
from grid import Grid

"""
Command to run: python3 -m unittest tests.grid_unittest
"""

class GridUnittest(unittest.TestCase):

    def setUp(self):
        self.test1 = Grid()
        self.test2 = Grid(2, 4)

    def testreturnAttr(self):
        self.assertEqual(self.test1.returnM(), 4)
        self.assertEqual(self.test1.returnN(), 4)
        self.assertEqual(self.test1.returnX(), 4)
        self.assertEqual(self.test1.returnY(), 4)

        self.assertEqual(self.test2.returnM(), 3)
        self.assertEqual(self.test2.returnN(), 5)
        self.assertEqual(self.test2.returnX(), 5)
        self.assertEqual(self.test2.returnY(), 3)

    def testInitializeGrid(self):
        self.assertEqual(self.test1.returnRow(0), ['A', 'B', 'C'])
        self.assertEqual(self.test1.returnCol(0), ['1', '2', '3'])

        self.assertEuqal(self.test2.returnRow(0), ['A', 'B', 'C', 'D'])
        self.assertEqual(self.test2.returnCol(0), ['1', '2'])

    def testFilterFunctions(self):
        pass
