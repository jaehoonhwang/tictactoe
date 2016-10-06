#/usr/local/bin/ python3

import logging
import string

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False


class Grid(object):

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
        for x in xrange(1, self.returnX()):
            self.returnG()[0][x] = alph_list[x - 1]

        for y in xrange(1, self.returnY()):
            self.returnG()[y][0] = y

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

    def printG(self):
        for x in self.returnG():
            print x


def main():
    a = Grid()
    a.printG()


if __name__ == '__main__':
    main()
