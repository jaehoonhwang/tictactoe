
class Player(object):
    """Player class.
    """

    def __init__(self, name, marker, value):
        self._name = name
        self._marker = marker
        self._value = value

    def get_name(self):
        return self._name

    def get_marker(self):
        return self._marker

    def player_value(self):
        return self._value

    def __str__(self):
        return "Player Name: {0} and Player Marker: {1}".format(self._name, self._marker)
