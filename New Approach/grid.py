import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False


class Grid(object):

    def __init__(self, m=4, n=4):
        self._M = m + 1
        self._N = n + 1
        self._G = []
        self.initializeGrid()

    def initializeGrid(self):
        logging.debug("Initializing Grid with M: {0}, N: {1}".format(self._M,
                                                                     self._N))
        self._G = [[0 for x in range(self.returnN())] \
                   for y in range(self.returnM())]

        # Initial point (0,0)
        self.returnG()[0][0] = "Num/Alph"

        for n in self.returnG()[:][0]:
            n = 

    def returnM(self):
        return self._M

    def returnN(self):
        return self._N

    def returnG(self):
        return self._G

    def printG(self):
        for x in self.returnG():
            print x


def main():
    a = Grid(4, 3)
    a.printG()


if __name__ == '__main__':
    main()
