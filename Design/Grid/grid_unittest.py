# Importing Standard Libaries
import os
import sys
import logging
import string
import unittest

# Directories of Node and LinkedList
dir = os.path.dirname(__file__)
dir = dir + '/LinkedList'
sys.path.insert(1, dir)

dir = os.path.dirname(__file__)
dir = dir + '/LinkedList/Node'
sys.path.insert(1, dir)

# Importing custom modules
from linkedlist import LinkedList
from node import Node
from grid_mn import Grid

root_logger = logging.getLogger()
root_logger.disabled = False


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.m = 3
        self.n = 3
        self.Grid = Grid(m, n)
        i = 0
        for x in range(1, 4):
            for y in range(1, 4):
                self.Grid.changeValCoor(x, y, i)
                i += 1

    def testReturn(self):
        # Checking M and N Grid numbers
        self.assertEqual(self.Grid.returnM, self.m)
        self.assertEqual(self.Grid.returnN, self.n)

        # Checking fucntion, Grid::returnColVal
        self.assertEqual(self.Grid.returnColVal(0), [0, 3, 6])
        self.assertEqual(self.Grid.returnColVal(1), [1, 4, 7])
        self.assertEqual(self.Grid.returnColVal(2), [2, 5, 9])

        # Checking function, Grid::returnRowVal
        self.assertEqual(self.Grid.returnRowVal(0), [0, 1, 2])
        self.assertEqual(self.Grid.returnRowVal(1), [3, 4, 5])
        self.assertEqual(self.Grid.returnRowVal(2), [6, 7, 8])

        # Checking function, Grid::returnGridArr
        self.assertEqual(self.Grid.returnGrid(), [[0, 1, 2],
                                                  [3, 4, 5]
                                                  [6, 7, 8]])

    def testSearch(self):
        # Checking function, Grid::searchPt
        for x in range(1,4):
            for y in range(1,4):
                self.assertEqual(self.Grid.searchPt(x,y), )
        # self.assertEqual(self.Grid.searchPt(1,1), 0)
        # self.assertEqual(self.Grid.searchPt(1,2), 1)
        # self.assertEqual(self.Grid.searchPt(1,3), 2)
