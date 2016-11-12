import logging
import unittest
from grid import Grid



class GridUnittest(unittest.TestCase):
    """ Grid Unit Test

    Command to run: python3 -m unittest tests.grid_unittest

    """

    def setUp(self):
        """Setting up Testing Environment

        Attributes:
            test1 (list of list) =
                    [['Alph/Num', 'A', 'B', 'C'],
                    [1, 0, 0, 0],
                    [2, 0, 0, 0],
                    [3, 0, 0, 0]]
            test2 (list of list) =
                    [['Alph/Num', 'A', 'B', 'C', 'D'],
                    [1, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0]]

        """
        self.test1 = Grid()
        self.test2 = Grid(2, 4)

    def testreturnAttr(self):
        """Testing Class Attributes Return Functions"""
        self.assertEqual(self.test1.returnM(), 4)
        self.assertEqual(self.test1.returnN(), 4)
        self.assertEqual(self.test1.returnX(), 4)
        self.assertEqual(self.test1.returnY(), 4)

        self.assertEqual(self.test2.returnM(), 3)
        self.assertEqual(self.test2.returnN(), 5)
        self.assertEqual(self.test2.returnX(), 5)
        self.assertEqual(self.test2.returnY(), 3)

    def testreturnRowCol(self):
        """Testing Returning Row and Column Functions"""
        self.assertEqual(self.test1.returnRow(0), ['A', 'B', 'C'])
        self.assertEqual(self.test1.returnCol(0), ['1', '2', '3'])

        self.assertEqual(self.test2.returnRow(0), ['A', 'B', 'C', 'D'])
        self.assertEqual(self.test2.returnCol(0), ['1', '2'])

    def testFilterFunctions(self):
        pass
