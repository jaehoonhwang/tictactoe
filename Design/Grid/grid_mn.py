# Importing official modules
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

# TODO: I need to fix this code

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

root_logger = logging.getLogger()
root_logger.disabled = False

# Class Grid Start


class Grid(object):

    def __init__(self, m=None, n=None):
        logging.debug('Grid::Constructor Initialized')
        if (m is None or n is None):
            m = 3
            n = 3
        self._M = m
        self._N = n
        self._G = []
        self._GwN = []
        self.initializeGrid()
        logging.debug('Grid::Constructor Finished')

    def returnM(self):
        logging.debug('Grid::returnM: %d', self._M)
        return self._M

    def returnN(self):
        logging.debug('Grid::returnN: %d', self._N)
        return self._N

    def returnG(self):
        logging.debug('Grid::returnG')
        return self._G

    def initializeGrid(self):
        logging.debug('Grid::initializeGrid Initialized')

        logging.debug('Grid::initializeGrid Label Initialized')

        alph_list = list(string.ascii_uppercase)
        alph_list = alph_list[0:self.returnM()]

        for x in range(0, self.returnN() + 1):
            self.returnG().append(LinkedList())

        G0 = Node('Alph/#')

        self.returnG()[0].pushS(G0)

        # Alphabetize X Axis
        i = 1
        for alph in alph_list:
            logging.debug('Grid::initializeGrid::Putting Alphabet %d time', i)
            logging.debug('Grid::initializeGrid::Alphabaet: alph')
            node = Node(alph, 0)
            logging.debug('Grid::initializeGrid::Axis Label X: %c', alph)
            self.returnG()[i].pushS(node)
            i = i + 1

        # FIXME: Compiling Errors

        logging.debug('Grid::initializeGrid::Axis X Label Finished')

        logging.debug('Grid::initializeGrid::Initialize Axis Y Label')
        for x in range(1, self.returnN() + 1):
            logging.debug('Grid::initializeGrid::Initializing Y: %d', x)
            node = Node(str(x))
            self.returnG()[0].pushS(node)

        logging.debug('Grid::initializeGrid::Axis Y Label Finished')

        for y in range(1, self.returnM() + 1):
            for x in range(1, self.returnN() + 1):
                logging.debug('Grid::initializeGrid::Setting up XY Axis: %s%s'
                              % (self.returnG()[y].returnHead().returnName(),
                              self.returnG()[0].searchIndex(x).returnName()))

                node = Node(self.returnG()[y].returnHead().returnName(
                ) + self.returnG()[0].searchIndex(x).returnName(), 0)
                self.returnG()[y].pushS(node)

        logging.debug('Grid::initializeGrid Finished')

    def printRow(self, row=None):
        if row is None:
            row = 0
        logging.debug('Grid::printRow Initialized')
        string_holder = ''
        space = '\t - \t'
        for i in range(0, self.returnN() + 1):
            string_holder = string_holder + \
                self.returnG()[i].searchIndex(row).returnName() + space
            logging.debug('Grid::printRow::string_holder: %s', string_holder)
        print(string_holder)

    def printCol(self, col=None):
        if col is None:
            col = 0
        logging.debug('Grid::printCol Initialized')
        string_holder = ''
        space = '\t - \t'
        for i in range(0, self.returnM() + 1):
            string_holder = string_holder + \
                self.returnG()[col].searchIndex(i).returnName() + space
            logging.debug('Grid::printCol::string_holder: %s', string_holder)
        print(string_holder)

    def printRowAll(self):
        for x in range(0, self.returnM() + 1):
            self.printRow(x)

    def printColAll(self):
        for x in range(0, self.returnN() + 1):
            self.printCol(x)
