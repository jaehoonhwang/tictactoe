# /usr/local/bin/python3

import logging
import string

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False

# TODO: Docstring (Sphnix Documentation)
# TODO: Unittest

class Grid(object):
    # Constructors

    def __init__(self, m=3, n=3):
        logging.debug("Grid::Constructor Initialized")
        self._M = m + 1
        self._N = n + 1
        self._X = self._N
        self._Y = self._M
        self._G = []
        self.initializeGrid()
        logging.debug("Grid::Constructor Finished")

    def initializeGrid(self):
        logging.debug("Grid::initializeGrid:: M: {0}, N: {1}".format(self._M,
                                                                     self._N))
        self._G = [[0 for x in range(self.returnN())]
                   for y in range(self.returnM())]

        # Initial point (0,0)
        self.returnG()[0][0] = "N/A"

        logging.debug("Grid::initializeGrid:: Generating Alphabet List")
        alph_list = list(string.ascii_uppercase)[:self.returnX() - 1]

        logging.debug("Grid::initializeGrid:: Generating X and Y axis Label")
        for x in range(1, self.returnX()):
            self.returnG()[0][x] = alph_list[x - 1]

        for y in range(1, self.returnY()):
            self.returnG()[y][0] = str(y)

        logging.debug("Grid:initializedGrid End")

    # Custom Setting Functions

    # Change with Coordinate
    def changeCoor(self, x=None, y=None, target=None):
        logging.debug("Grid::changeCoor: Initialized")
        x, y = self.Coor2Ind(x,y)
        self.returnG()[y][x] = target
        logging.debug("Grid::changeCoor: Finished")

    def changeName(self, target_str=None, target=None):
        logging.debug("Grid::changeName: Initialized")
        x, y = self.Name2Ind(target_str)
        self.returnG()[y][x] = target
        logging.debug("Grid::changeName: Finished")


    # Search Functions

    def searchCoor(self, x=None, y=None):
        logging.debug("Grid::searchCoor: Initialized")
        logging.debug("Grid::searchCoor: {0}, {1}".format(x, y))
        x, y = self.Coor2Ind(x, y)
        return self.returnG()[y][x]

    def searchName(self, target_str=None):
        logging.debug("Grid::searchName: Initialized")
        logging.info("Grid::searchName: target_str type = {0}".
                     format(type(target_str)))
        x, y = self.Name2Ind(target_str)
        return self.returnG()[y][x]

    # Helper Functions

    def Coor2Ind(self, x=None, y=None):
        logging.debug("Grid::Coor2Ind: Initialized")
        logging.debug("Grid::Coor2Ind: x = {0}, y = {1}".format(x, y))
        if self.evalGrid(x, y):
            logging.info("Grid::Coor2Ind: evalGrid Sucessful")
            return x,y
        else:
            raise IndexError("Grid::Coor2Ind: Index failed.")

    def Name2Ind(self, target_str=None):
        logging.debug("Grid::Name2Ind: Initialized")
        logging.info("Grid::Name2Ind: target_str type = {0}".
                     format(type(target_str)))
        if target_str is None:
            logging.warning("Grid::Name2Ind: Type error, param1 is None Type.")
            raise TypeError("Grid::Name2Ind: TypeError. param1 is None Type.")
        if self.typeCheck(target_str, str):
            if len(target_str) != 2:
                logging.warning("Grid::Name2Ind: Assertion Error, \
                                 length of target_str = {0} != 2".format(len(target_str)))
                raise AssertionError("Grid::Name2Ind: Target string length is not 2")
            firstStr = list(target_str)[0]
            secondStr = list(target_str)[1]

            firstpt = ord(firstStr) - 64
            secondpt = ord(secondStr) - 48
            logging.debug("Grid::searchName: {0} and {1}".format(firstpt,
                                                                 secondpt))
            return firstpt, secondpt



    # Filter Functions
    def evalGrid(self, x=None, y=None):
        if not (self.typeCheck(x, int) and self.typeCheck(y, int)):
            return False
        try:
            self.returnG()[y][x] == 0
        except IndexError:
            logging.warning("Grid::evalGrid::IndexError: Input x or/and y \
                            is/are greater than Grid's X")
            return False
        if x < 0 or y < 0:
            logging.warning("Grid::evalGrid: Input x or y is negative value.")
            return False
        logging.info("Grid::evalGrid: Correct Input")

        return True

    def typeCheck(self, target, target_type):
        try:
            isinstance(target, target_type)
        except TypeError:
            logging.warning("Grid::typeCheck: TypeError. Maybe you are trying \
                            to check None Type?")
            return False
        if isinstance(target, target_type):
            logging.info("Grid::typeCheck: Correct type, {0}.".
                         format(target_type))
            return True
        else:
            logging.warning("Grid::typeCheck: Wrong type, {0}.".
                            format(target_type))
            return False

    # Return Attributes
    def returnM(self):
        return self._M

    def returnN(self):
        return self._N

    def returnX(self):
        return self._X

    def returnY(self):
        return self._Y

    def returnG(self):
        return self._G

    # Print Attributes
    def printG(self):
        for x in self.returnG():
            print(x)


def main():
    a = Grid()
    a.printG()
    print(a.searchName("A1"))
    print(a.changeName("A1", 2))
    a.printG()


if __name__ == '__main__':
    main()
