#/usr/local/bin/python3

import logging
import string

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False


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
        if self.evalGrid(x, y) and self.typeCheck(target, int):
            logging.info("Grid::changeCoor: Target has been verified")
            self.returnG[y][x] = target
            return True
        else:
            logging.warning("Grid::changeCoor has failed")
            logging.warning("Grid::changeCoor: Check type/value of x, y, \
                            target")
            return False

    def changeName(self, target_str=None, nums=None, target=None):
        logging.debug("Grid::changeName: Initialized")
        foo = self.searchName(target_str, nums)
        if foo is not -1:
            foo = target
            return True
        else:
            return False

    # Search Functions

    def searchCoor(self, x=None, y=None):
        logging.debug("Grid::searchCoor: Initialized")
        logging.debug("Grid::searchCoor: {0}, {1}".format(x, y))
        if self.evalGrid(x, y):
            logging.info("Grid::searchCoor: Successful.")
            return self.returnG()[y][x]
        else:
            logging.warning("Grid::searchCoor: Failed")
            return -1

    def searchName(self, target_str=None, nums=None):
        logging.debug("Grid::searchName: Initialized")
        logging.info("Grid::searchName: target_str type = {0} num type = {1}".
                     format(type(target_str), type(nums)))
        if target_str is None or self.typeCheck(target_str, str):
            logging.warning("Grid::searchName: Correct Input required")
            return -1
        if self.typeCheck(target_str, str) and nums is None:
            if len(target_str) != 2:
                logging.warning("Grid::searchName: str length not permiitted")
                return -1
            firstStr = list(target_str)[0]
            secondStr = list(target_str)[1]

            firstpt = ord(firstStr) - 64
            secondpt = ord(secondStr) - 48
            logging.debug("Grid::searchName: {0} and {1}".format(firstpt,
                                                                 secondpt))
            return self.returnG()[secondpt][firstpt]
        if self.typeCheck(target_str, str) and self.typeCheck(nums, int):
            if len(target_str) != 1:
                logging.warning("Grid::searchName: str length not permiited")
                return -1
            firstStr = ord(target_str) - 64
            return self.returnG()[nums][firstStr]
        logging.warning("Grid::searchName: Unknown Error")
        return -1

    # Helper Functions

    # Filter Functions
    def evalGrid(self, x=None, y=None):
        if not(self.typeCheck(x, int) and self.typeCheck(y, int)):
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
    print(a.changeName("A1",None ,2))
    a.printG()

if __name__ == '__main__':
    main()
