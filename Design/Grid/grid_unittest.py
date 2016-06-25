import os
import sys
import logging
import string

# Directories of Node
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
root_logger.disabled = True


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.Grid = Grid()
