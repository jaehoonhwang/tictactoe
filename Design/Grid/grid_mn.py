# Importing official modules
import os
import sys
import logging
import string

# Directories of Node
dir = os.path.dirname(__file__)
dir = dir  + '/LinkedList'
sys.path.insert(1, dir)

dir = os.path.dirname(__file__)
dir = dir + '/LinkedList/Node'
sys.path.insert(1, dir)

# Importing custom modules
from linkedlist import LinkedList
from node import Node

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Class Grid Start
class Grid(object):

    def __init__(self, m = None, n = None):
        logging.debug('Grid::Constructor Initialized')
        self._Grid = LinkedList()
        if (m == None or n == None):
            m = 3
            n = 3
        self._M = m
        self._N = n
        self._X = []
        self._Y = []
        self.initializeGrid()
        logging.debug('Grid::Constructor Finished')

    def returnGrid(self):
        logging.debug(('Grid::returnGrid: ', self._Grid))
        return self._Grid

    def returnM(self):
        logging.debug('Grid::returnM: %d', self._M)
        return self._M

    def returnN(self):
        logging.debug('Grid::returnN: %d', self._N)
        return self._N

    def returnX(self):
        logging.debug(('Grid::returnX: ', self._X))
        return self._X

    def returnY(self):
        logging.debug(('Grid::returnY: ', self._Y))
        return self._Y

    def initializeGrid(self):
        logging.debug('Grid::initializeGrid Initialized')

        logging.debug('Grid::initializeGrid::X Axis Grid Initialized')
        logging.debug('Grid::initializeGrid::X = %d', self._N)

        logging.debug('Grid::initializeGrid::Creating X Axis')
        G0 = Node('Alph/#')
        self._X.append(G0)
        self._Grid.pushS(G0)
        for x in range(1, self._N+1):
            logging.debug('Grid::initializeGrid::Creating X: %d', x)
            foo = Node(str(x))
            self._Grid.pushS(foo)
            self._X.append(foo)

        logging.debug('Grid::initializeGrid::%d Initialized: ')
        alph_list = list(string.ascii_uppercase)
        alph_list = alph_list[0:self.returnM()]

        for x in alph_list:
            logging.debug('Grid::initializeGrid::Setting up Y: %s list', x)
            foo_ll = LinkedList()
            self._Y.append(foo_ll)
            foo_ll.pushS(Node(x))
            for y in range(1, len(self._X)):
                logging.debug('Grid::initializeGrid::Setting up Y Axis: %s%s' % (x, self._X[y].returnName()))
                foo_ll.pushS(Node(x + self._X[y].returnName(), 0))


        logging.debug('Grid::initializeGrid Finished')
