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

    # Search Functions

    def searchCoor(self, x=None, y=None):
        logging.debug("Grid::searchCoor: {0}, {1}".format(x, y))
        if x < 0 or y < 0:
            logging.warning(
                "Grid::searchCoor: Inputs are less than 0, x = {0} & y = {1}".
                format(x, y))
            return -1
        if x > self.returnX() or y > self.returnY():
            logging.warning(
                "Grid::searchCoor: Inputs are bigger than its size")
            return -1
        if x is None or y is None:
            logging.warning("Grid::searchCoor: Need input for the function")
            return -1

        logging.debug("Grid::searchCoor::returnValue: {0}".format(
            self.returnG()[y][x]))
        return self.returnG()[y][x]

    def searchName(self, target_str=None, nums=None):
        logging.debug("Grid::searchName: Initialized")
        if target_str is None or type(target_str) is not str:
            logging.warning("Grid::searchName: Input required")
            return -1
        if type(target_str) is str and type(nums) is None:
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
        if type(target_str) is str and type(nums) is int:
            if len(target_str) != 1:
                logging.warning("Grid::searchName: str length not permiited")
                return -1
            firstStr = ord(target_str) - 64
            return self.returnG()[nums][firstStr]
        return -1

    # Helper Functions

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


if __name__ == '__main__':
    main()
