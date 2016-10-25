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
    """Grid class using M by N grid

    Making a grid by using list

    Attributes:
        M (int): M-row as in M by N, (creates M + 1 due to axis label)
        N (int): N-column as in M by N (creates N + 1 due to axis label)
        X (int): X axis, M-row
        Y (int): Y axis, N-column
        G (`list` of `list`): Grid

    """

    def __init__(self, m=3, n=3):
        """Grid class __init__ method (Constructor)

        Note:
            Default Size, if not configured, is a 3 by 3 grid.

        Args:
            m (int, optional): Specifying M
            n (int, optional): Specifying N

        """
        logging.debug("Grid::Constructor Initialized")
        self._M = m + 1
        self._N = n + 1
        self._X = self._N
        self._Y = self._M
        self._G = []
        self.initializeGrid()
        logging.debug("Grid::Constructor Finished")

    def initializeGrid(self):
        """ Initialize the grid (Labeling)

        Initialize Grid and set-up the Attributes, x and y.
        X-axis will be Alphbaetic labeling and Y-axis will be numeric labeling.

        Examples:
            >> Grid(3,3):
            [["Num/Alph", "A", "B", "C"],
             ["1", 0, 0, 0],
             ["2", 0, 0, 0],
             ["3", 0, 0, 0]]

        Note:
            Grid creates M by N, where M doesn't have to equal to N
            Grid M or N can't exceed 26, due to alphabet restriction

        """
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
        """Change grid value with cartesian coordinate value

        Change Grid value at Coordinate (x,y). It uses `Coor2Ind` function to
        locate target value to be changed.

        Example:
            Before
            G = [['Alph/Num', A, B, C],
                 [1, 0, 0, 0],
                 [2, 0, 0, 0],
                 [3, 0, 0, 0]]
            changeCoor(2, 3, 1)
            After
            G = [['Alph/Num', A, B, C],
                 [1, 0, 0, 0],
                 [2, 0, 0, 1],
                 [3, 0, 0, 0]]

        Args:
            x (int): X-coordinate
            y (int): Y-coordinate
            target (any type): Target value to be changed

        """
        logging.debug("Grid::changeCoor: Initialized")
        x, y = self.Coor2Ind(x, y)
        self.returnG()[y][x] = target
        logging.debug("Grid::changeCoor: Finished")

    def changeName(self, target_str=None, target=None):
        """Change grid value with name value

        Change Grid by Name value ("A1") for example. It uses `Name2Ind`
        function to locate target value to be changed

        Example:
            Before
            G = [['Alph/Num', A, B, C],
                 [1, 0, 0, 0],
                 [2, 0, 0, 0],
                 [3, 0, 0, 0]]
            changeName("B3", 1)
            G = [['Alph/Num', A, B, C],
                 [1, 0, 0, 0],
                 [2, 0, 0, 1],
                 [3, 0, 0, 0]]

        Args:
            target_str (str): Name to be changed
            target (any type): Target value to be changed

        """
        logging.debug("Grid::changeName: Initialized")
        x, y = self.Name2Ind(target_str)
        self.returnG()[y][x] = target
        logging.debug("Grid::changeName: Finished")

    # Search Functions

    def searchCoor(self, x=None, y=None):
        """Search grid by coordinates and return value

        Search grid by cartesian coordinate values (x,y) and return the value
        of the grid at the target location. The function uses `Coor2Ind` to
        locate Coordinates

        Example:
            G = [['Alph/Num', A, B, C],
                 [1, 0, 1, 2],
                 [2, 3, 4, 5],
                 [3, 6, 7, 8]]
            searchCoor(2, 3) # Returns 5

        Args:
            x (int): X-coordinate
            y (int): Y-coordinate

        Returns:
            any type: Value at (x,y)

        """
        logging.debug("Grid::searchCoor: Initialized")
        logging.debug("Grid::searchCoor: {0}, {1}".format(x, y))
        x, y = self.Coor2Ind(x, y)
        return self.returnG()[y][x]

    def searchName(self, target_str=None):
        """Search grid by name and return value

        Search grid by name values, "A1", and return the value of the grid at
        the grid at the target location. THe function uses `Name2Ind` to locate
        Name.

        Example:
        G = [['Alph/Num', A, B, C],
             [1, 0, 1, 2],
             [2, 3, 4, 5],
             [3, 6, 7, 8]]
        searchName("A2") # Returns 1

        Args:
            name (str): Name to locate Target

        Returns:
            any type: Value at Name

        """
        logging.debug("Grid::searchName: Initialized")
        logging.info("Grid::searchName: target_str type = {0}".
                     format(type(target_str)))
        x, y = self.Name2Ind(target_str)
        return self.returnG()[y][x]

    # Helper Functions

    def Coor2Ind(self, x=None, y=None):
        """Return Cartesian coordinates for coordinates

        Returns two values as x and y location. `evalGrid` is used for checking
        valid types of the arguments.

        Args:
            x (int): X-coordinate, range 1 ~ N +1
            y (int): Y-coordinate, range 1 ~ M +1

        Returns:
            x, y (int, int): x and y Coordinates

        """
        logging.debug("Grid::Coor2Ind: Initialized")
        logging.debug("Grid::Coor2Ind: x = {0}, y = {1}".format(x, y))
        if self.evalGrid(x, y):
            logging.info("Grid::Coor2Ind: evalGrid Sucessful")
            return x, y

    def Name2Ind(self, target_str=None):
        """Return Cartesian coordinates for name

        Returns two values as x and y location. `typeCheck` is used for
        checking valid types for the name. Also `evalGrid` is used for
        checking valid x,y coordinates.

        Args:
            target_str (str): Target string, length of 2

        Returns:
            x, y (int, int): x and y Coordinates

        Raises:
            AssertionError: If length of target_str is not 2, raise an error.

        """
        logging.debug("Grid::Name2Ind: Initialized")
        logging.info("Grid::Name2Ind: target_str type = {0}".
                     format(type(target_str)))
        if self.typeCheck(target_str, str):
            if len(target_str) != 2:
                logging.warning("Grid:: Name2Ind: Assertion Error, \
                                length of target_str={0} != 2".
                                format(len(target_str)))
                raise AssertionError(
                    "Grid::Name2Ind: Target string length is not 2")
            firstStr = list(target_str)[0]
            secondStr = list(target_str)[1]

            firstpt = ord(firstStr) - 64
            secondpt = ord(secondStr) - 48
            logging.debug("Grid::searchName: {0} and {1}".format(firstpt,
                                                                 secondpt))
            if self.evalGrid(firstpt, secondpt):
                return firstpt, secondpt

    # Filter Functions
    def evalGrid(self, x=None, y=None):
        """Evalute Grid for possible wrong error

        Check type and index errors for Cartesian coordinates type.

        Args:
            x (int): X-coordinate
            y (int): Y-coordinate

        Returns:
            bool: If x and y passes index, type tests.

        Raises:
            TypeError: Int type checking for x and y
            IndexError: x and y are out of range (positive)
            IndexError: x and y are negative values

        """
        logging.info("Grid::evalGrid: x = {0}, type: {1}".format(x, type(x)))
        logging.info("Grid::evalGrid: y = {0}, type: {1}".format(y, type(y)))
        self.typeCheck(x, int)
        self.typeCheck(y, int)
        try:
            self.returnG()[y][x] == 0
        except IndexError("Grid::evalGrid: x or y is out of range"):
            logging.warning("Grid::evalGrid::IndexError: Input x or/and y \
                            is/are greater than Grid's X")
        if x < 0 or y < 0:
            logging.warning("Grid::evalGrid: Input x or y is negative value.")
            raise IndexError("Grid::evalGrid: Input x or y is negative value.")
        logging.info("Grid::evalGrid: Correct Input")

        return True

    def typeCheck(self, target, target_type):
        """Type Checking against target type

        Checks type of the arguments

        Args:
            target (any type): Target
            target_type (type): Target type

        Return:
            boo: True if type check succeeds

        Raises:
            TypeError: Checks if the target is None Type
            TypeError: Checks if the target is target type.

        """
        try:
            isinstance(target, target_type)
        except TypeError:
            logging.warning("Grid::typeCheck: TypeError. Maybe you are trying \
                            to check None Type?")
        if isinstance(target, target_type):
            logging.info("Grid::typeCheck: Correct type, {0}.".
                         format(target_type))
            return True
        else:
            logging.warning("Grid::typeCheck: Wrong type, {0}.".
                            format(target_type))
            raise TypeError("Grid::typeCheck: Wrong type")

    # Return Attributes
    def returnM(self):
        """Return Attribute: M"""
        return self._M

    def returnN(self):
        """Return Attribute: N"""
        return self._N

    def returnX(self):
        """Return Attribute: X"""
        return self._X

    def returnY(self):
        """Return Attribute: Y"""
        return self._Y

    def returnG(self):
        """Return Attribute: G"""
        return self._G

    def returnRow(self, row):
        """Return m row"""
        return self.returnG()[row][1:]

    def returnCol(self, col):
        """Return n column"""
        return self.returnG()[1:][col]

    # Print Attributes
    def printG(self):
        """Print the grid"""
        for item in self.returnG():
            print(str(item[0]) + "\t - \t", '\t - \t'.join(map(str, item[1:])))


def main():
    a = Grid()
    a.printG()
    print(a.searchName("A1"))
    print(a.changeName("A1", 2))
    a.printG()
    print(a.returnRow(0))


if __name__ == '__main__':
    main()
