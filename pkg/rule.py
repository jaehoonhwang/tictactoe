# /usr/local/bin/python3

import logging
from grid import Grid

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False


class Rule(Grid):

    def __init__(self, grid):
        self._Grid = grid

    def setGrid(self, grid):
        self._Grid = grid

    def returnGrid(self):
        return self._Grid
