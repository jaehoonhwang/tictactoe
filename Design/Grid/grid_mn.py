#!/usr/bin/env python3

# Importing Standard Libraries
import os
import sys
import logging
import string

# Jay, you are not using below call because it is a RELATIVE PATHING
# You will get an error when calling this from sub sub sub sub sub dir.
# from Linkedlist.linkedlist import LinkedList
# from Linkedlist.Node.node import Node

# Directories of Node and LinkedList
dir = os.path.dirname(__file__)
dir = dir + '/Linkedlist'
sys.path.insert(1, dir)

dir = os.path.dirname(__file__)
dir = dir + '/Linkedlist/Node'
sys.path.insert(1, dir)

# Importing custom modules

from node import Node
from linkedlist import LinkedList


logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False

# TODO: Proper Logging needed

# Class Grid Start


class Grid(object):

    def __init__(self, m=None, n=None):
        logging.debug('Grid::Constructor Initialized')
        if (m is None or n is None):
            m = 3
            n = 3
        self._M = m     # Row
        self._N = n     # Column
        self._G = []    # Grid
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
        alph_list = alph_list[0:self.returnN()]

        for x in range(0, self.returnN() + 1):
            self.returnG().append(LinkedList())

        G0 = Node('Alph/#')     # First Node of a grid. Index

        self.returnG()[0].pushS(G0)

        # Alphabetize X Axis
        i = 1
        for alph in alph_list:
            logging.debug('Grid::initializeGrid::Putting Alphabet %d time', i)
            logging.debug('Grid::initializeGrid::Alphabet: alph')
            node = Node(alph)
            logging.debug('Grid::initializeGrid::Axis Label X: %c', alph)
            self.returnG()[i].pushS(node)
            i = i + 1

        logging.debug('Grid::initializeGrid::Axis X Label Finished')

        logging.debug('Grid::initializeGrid::Initialize Axis Y Label')
        for x in range(1, self.returnM() + 1):
            logging.debug('Grid::initializeGrid::Initializing Y: %d', x)
            node = Node(str(x))
            self.returnG()[0].pushS(node)

        logging.debug('Grid::initializeGrid::Axis Y Label Finished')

        for y in range(1, self.returnN() + 1):
            for x in range(1, self.returnM() + 1):
                logging.debug('Grid::initializeGrid::Setting up Axis: %s%s' %
                              (self.returnG()[y].returnHead().returnName(),
                               self.returnG()[0].searchIndex(x).returnName()))

                node = Node(self.returnG()[y].returnHead().returnName(
                ) + self.returnG()[0].searchIndex(x).returnName(), 0)
                self.returnG()[y].pushS(node)

        logging.debug('Grid::initializeGrid Finished')

    def searchPt(self, xcoor, ycoor):
        logging.debug('Grid::searchPt Initialized')
        logging.debug('Grid::searchPt: (%d,%d)', xcoor, ycoor)
        if xcoor > self.returnM():
            logging.debug('Grid::searchPt: X range exceeds')
            return
        if ycoor > self.returnN():
            logging.debug('Grid::searchPt: Y range exceeds')
            return

        logging.debug('Grid::searchPt: %s',
                      self.returnG()[ycoor].searchIndex(xcoor))
        logging.debug('Grid::searchPt Finished')
        return self.returnG()[ycoor].searchIndex(xcoor)

    def searchTup(self, tup):
        xcoor = tup[0]
        ycoor = tup[1]
        logging.debug('Grid::searchTup: (%d,%d)', xcoor, ycoor)
        if xcoor > self.returnN():
            logging.debug('Grid::searchTup: X range exceeds')
            return
        if ycoor > self.returnM():
            logging.debug('Grid::searchTup: Y range exceeds')
            return

        logging.debug('Grid::searchTup: %s',
                      self.returnG()[xcoor].searchIndex(ycoor))

        return self.returnG()[xcoor].searchIndex(ycoor)

    def searchName(self, name):
        firsthalf, secondhalf = name[:len(string) / 2], name[len(string) / 2:]
        xcoor = ord(firsthalf) - 64
        ycoor = int(secondhalf)

        return self.searchPt(xcoor, ycoor)

    def changeValCoor(self, xcoor, ycoor, value):
        # Changing Target Node Value using X-coordinate and Y-Coordinate
        self.searchPt(xcoor, ycoor).setValue(value)

    def changeValTup(self, tups, value):
        # Changing Target Node Value using tuples.
        self.searchTup(xcoor, ycoor).setValue(value)

    def changeValName(self, name, vaule):
        # Changing Target Node Value using its name
        self.searchName(name).setValue(value)

    def returnColVal(self, col=None):
        # Returning (col)th column values in array
        if col is None:
            col = 0
        holder = []

        for i in range(1, self.returnN() + 1):
            holder.append(self.returnG()[i].searchIndex(col).returnValue())

        return holder

    def returnRowVal(self, row=None):
        # Returning (row)th row values in array
        if row is None:
            row = 0
        holder = []

        for i in range(1, self.returnM() + 1):
            holder.append(self.returnG()[row].searchIndex(i).returnValue())

        return holder

    def returnGridArr(self):
        # Returnig Grid in m by n array
        logging.debug('Grid::returnGrid Initialized')
        holder = [[0 for x in range(self.returnN())]
                  for y in range(self.returnM())]

        for i in range(0, self.returnM()):
            for j in range(0, self.returnN()):
                holder[i][j] = self.returnG()[j + 1].searchIndex(
                    i + 1).returnValue()
        logging.debug('Grid::returnGrid Ended')
        return holder

    def printCol(self, col=None):
        if col is None:
            col = 0
        logging.debug('Grid::printRow Initialized')
        string_holder = ''
        space = '\t - \t'
        for i in range(0, self.returnN() + 1):
            if i == self.returnN():
                string_holder = string_holder + \
                    self.returnG()[i].searchIndex(col).returnName()
                logging.debug('Grid::printCol::Last string_holder: %s',
                              string_holder)
            else:
                string_holder = string_holder + \
                    self.returnG()[i].searchIndex(col).returnName() + space
                logging.debug('Grid::printCol::string_holder: %s',
                              string_holder)
        print(string_holder)

    def printRow(self, row=None):
        if row is None:
            row = 0
        logging.debug('Grid::printRow Initialized')
        string_holder = ''
        space = '\t - \t'
        for i in range(0, self.returnM() + 1):
            if i == self.returnM():
                string_holder = string_holder + \
                    self.returnG()[row].searchIndex(i).returnName()
                logging.debug('Grid::printRow::Last string_holder: %s',
                              string_holder)
            else:
                string_holder = string_holder + \
                    self.returnG()[row].searchIndex(i).returnName() + space
                logging.debug(
                    'Grid::printRow::string_holder: %s', string_holder)
        print(string_holder)

    def printRowAll(self):
        logging.debug('Grid::printRowAll Initialized')
        for x in range(0, self.returnN() + 1):
            self.printRow(x)
        logging.debug('Grid::printRowAll Finished')

    # Use PrintColAll for correct orientation.
    def printColAll(self):
        logging.debug('Grid::printColAll Initialized')
        for x in range(0, self.returnM() + 1):
            self.printCol(x)
        logging.debug('Grid::printRowAll Finished')

    def printGrid(self):
        logging.debug('Grid::printGrid Initialized')
        self.printColAll()
        logging.debug('Grid::printGrid Finished')
