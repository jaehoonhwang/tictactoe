# Importing official modules
import os
import sys
import logging

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

    def __init__(self):
        logging.debug('Grid::Constructor Initialized')
        self._Grid = LinkedList()
        self._A = LinkedList()
        self._B = LinkedList()
        self._C = LinkedList()
        self.initializeGrid()
        logging.debug('Grid::Constructor Finished')

    def returnGrid(self):
        logging.debug(('Grid::returnGrid: ', self._Grid))
        return self._Grid

    def returnA(self):
        logging.debug(('Grid::returnA: ', self._A))
        return self._A

    def returnB(self):
        logging.debug(('Grid::returnB: ', self._B))
        return self._B

    def returnC(self):
        logging.debug(('Grid::returnC: ', self._C))
        return self._C

    def initializeGrid(self):
        logging.debug('Grid::initializeGrid Initialized')

        logging.debug('Grid::initializeGrid::Grid Initialized')
        G0 = Node('Alph/#')
        G1 = Node('1')
        G2 = Node('2')
        G3 = Node('3')
        self._Grid.pushS(G0)
        self._Grid.pushS(G1)
        self._Grid.pushS(G2)
        self._Grid.pushS(G3)

        logging.debug('Grid::initializeGrid::A Initialized')
        A0 = Node('A')
        A1 = Node('A1', 0)
        A2 = Node('A2', 0)
        A3 = Node('A4', 0)
        self._A.pushS(A0)
        self._A.pushS(A1)
        self._A.pushS(A2)
        self._A.pushS(A3)

        logging.debug('Grid::initializeGrid::B Initialized')
        B0 = Node('B')
        B1 = Node('B1', 0)
        B2 = Node('B2', 0)
        B3 = Node('B3', 0)
        self._B.pushS(A0)
        self._B.pushS(A1)
        self._B.pushS(A2)
        self._B.pushS(A3)

        logging.debug('Grid::initializeGrid::C Initialized')
        C0 = Node('C')
        C1 = Node('C1', 0)
        C2 = Node('C2', 0)
        C3 = Node('C3', 0)
        self._C.pushS(C0)
        self._C.pushS(C1)
        self._C.pushS(C2)
        self._C.pushS(C3)

        logging.debug('Grid::initializeGrid Finished')
