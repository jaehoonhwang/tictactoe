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

root_logger = logging.getLogger()
root_logger.disabled = True

# Class Grid Start
class Grid(object):

    def __init__(self, m = None, n = None):
        logging.debug('Grid::Constructor Initialized')
        if (m == None or n == None):
            m = 3
            n = 3
        self._M = m
        self._N = n
        self._X = []
        self._Y = []
        self.initializeGrid()
        logging.debug('Grid::Constructor Finished')

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
        logging.debug('Grid::initializeGrid::X = %d', self._M)

        logging.debug('Grid::initializeGrid::Creating Y Index')

        logging.debug('Grid::initializeGrid::Linked List for Y Index')

        alph_list = list(string.ascii_uppercase)
        alph_list = alph_list[0:self.returnN()]

        for y in range(0, self.returnN() + 1):
            self.returnY().append(LinkedList())

        G0 = Node('Alph/#')
        self.returnX().append(LinkedList())

        self.returnX()[0].pushS(G0)
        self.returnY()[0].pushS(G0)

        i = 1
        for alph in alph_list:
            logging.debug('Grid::initializeGrid::Putting Alphabet %d time', i)
            node = Node(alph, 0)
            self.returnY()[i].pushS(node)
            self.returnX()[0].pushS(node)
            i = i + 1

        logging.debug('Grid::initializeGrid::Initialize X')
        for x in range(1, self.returnM() + 1):
            logging.debug('Grid::initializeGrid::Initializing X: %d', x)
            foo = Node(str(x))
            self.returnX().append(LinkedList())
            self.returnX()[x].pushS(foo)

        logging.debug('Grid::initializeGrid::%d Initialized: ')
        
        for x in range(1, self.returnM() + 1):
            for y in range(1, self.returnN() + 1):
                logging.debug('Grid::initializeGrid::Setting up Y Axis: %s%s' % (self.returnY()[y].returnHead().returnName(), self.returnX()[x].returnHead().returnName()))
                node = Node(self.returnY()[y].returnHead().returnName() + self.returnX()[x].returnHead().returnName(), 0)
                self.returnX()[x].pushS(node)
                self.returnY()[y].pushS(node)

        logging.debug('Grid::initializeGrid Finished')

    def printRow(self, row = None):
        if row == None:
            row = 0
        logging.debug('Grid::printRow Initialized')
        string_holder = ''
        space = '\t - \t'
        for i in range(0, self.returnM()):
            string_holder = string_holder + self.returnX()[row].searchIndex(i).returnName() + space
            logging.debug('Grid::printRow::string_holder: %s', string_holder)
        print (string_holder)


    def printRowAll(self):
        for x in range(0, len(self.returnX())):
            self.printRow(x)