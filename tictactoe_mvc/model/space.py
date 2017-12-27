import string


class Space(object):
    """Space class.
    """

    def __init__(self, x=None, y=None):
        self._x = x
        self._y = y

        self._isvalid = self._validation_check()
        self.value = 0
        self.string = _create_string() if self._isvalid else ""

    def set_coordinate(self, x, y):
        self._x = x
        self._y = y
        self._isvalid = self._validation_check()

    def set_value(self, value):
        self.value = value

    def _validation_check(self):
        if self._x is None:
            return False

        if self._y is None:
            return False

        return True

    def _create_string(self):
        alphbets = string.ascii_uppercase
        return alphbets[self._x] + str(self._y)

    def __str__(self):
        return "Space Coordinate: {0} and value: {1}".format(self.string, self.value)
