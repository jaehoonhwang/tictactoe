from space import Space
from tictactoe_mvc.exceptions import InvalidRangeException


class Grid(object):
    """Grid Class.
    """

    def __init__(self, m=3, n=3):
        self._m = 3
        self._n = 3
        self.grid = []
        self._initialize_grid()

    def change_value_on_coordinate(self, x, y, value):
        pass

    def _initialize_grid(self):

        for i in xrange(self._m):
            row = []
            for j in xrange(self._n):
                row.append(Space(i, j))
            self.grid.append(row)

    def _range_check(self, x, y):

        if x < 0 or x > self._m:
            return False

        if y < 0 or y > self._n:
            return False

        return True
