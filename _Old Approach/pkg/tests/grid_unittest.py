import logging
import unittest
from grid import Grid

# TODO: Create AssertRaise cases


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

    def testchangeValue(self):
        """Testing Change Value Functions"""
        self.test1.changeCoor(1, 3, 5)
        self.test1.changeCoor(2, 2, 3)
        self.test1.changeCoor(3, 1, 1)
        self.assertEqual(self.test1.returnG()[3][1], 5)
        self.assertEqual(self.test1.returnG()[2][2], 3)
        self.assertEqual(self.test1.returnG()[1][3], 1)

        self.test2.changeCoor(1, 1, 1)
        self.test2.changeCoor(2, 2, 2)
        self.test2.changeCoor(3, 1, 3)
        self.test2.changeCoor(4, 2, 4)
        self.assertEqual(self.test2.returnG()[1][1], 1)
        self.assertEqual(self.test2.returnG()[2][2], 2)
        self.assertEqual(self.test2.returnG()[1][3], 3)
        self.assertEqual(self.test2.returnG()[2][4], 4)

        self.test1.changeName("A1", 2)
        self.test1.changeName("B3", 4)
        self.test1.changeName("C2", 6)
        self.assertEqual(self.test1.returnG()[1][1], 2)
        self.assertEqual(self.test1.returnG()[3][2], 4)
        self.assertEqual(self.test1.returnG()[2][3], 6)

        self.test2.changeName("A2", 5)
        self.test2.changeName("B1", 6)
        self.test2.changeName("C2", 7)
        self.test2.changeName("D1", 8)
        self.assertEqual(self.test2.returnG()[2][1], 5)
        self.assertEqual(self.test2.returnG()[1][2], 6)
        self.assertEqual(self.test2.returnG()[2][3], 7)
        self.assertEqual(self.test2.returnG()[1][4], 8)
