# /usr/local/bin/python3

import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False

# TODO: Sanity Check for the inputs, One method to rule them all also logging


class Player(object):
    """Player class

    Attributes:
        Name (str): Name of the user
        Turn (bool): Turn of the player
        Mark (str): Mark of the player

    """

    def __init__(self, name=None, turn=False, mark='O'):
        """Player Class __init__ method

        Args:
            name (str): Name of the player
            turn (bool): Turn of the player

        """

        self._Name = name
        self._Turn = False
        self._Mark = mark

    def setName(self, name=None):
        """Set Name for the player

        Args:
            name (str): Name for the player

        Raises:
            TypeError: No input for the type
            TypeError: Type of input is not string


        """
        if name is None:
            raise TypeError("Player::setName: Input for the name is None Type")
        else:
            if isinstance(name, str):
                self._Name = name
            else:
                raise TypeError("Player::setName: Check the type for the name \
                                 (str)")

    def setTurn(self, turn=None):
        """Set Turn for the player

        Args:
            turn (bool): Yes or No

        Raise:
            TypeError: No Input
            TypeError: Input is not a boolean type
        """
        if turn is None:
            raise TypeError("Player::setTurn: Input is None Type")
        else:
            if isinstance(turn, bool):
                self._Turn = turn
            else:
                raise TypeError("Player::setTurn: Input is not Bool Type")

    def setMark(self, mark=None):
        """Set Mark for the player

        Args:
            mark (str): Mark of the player, default 'O' or 'X'

        Raise:
            TypeError: Input is None
            TypeError: Input is not str Type
        """
        if mark is not None:
            if isinstance(mark, str):
                self._Mark = mark
            else:
                raise TypeError("Player::setMark: Input is not str Type")
        else:
            raise TypeError("Player::setMark: Input is None Type")

    def returnName(self):
        """Return Name"""
        return self._Name

    def returnTurn(self):
        """Return Turn"""
        return self._Turn

    def returnMark(self):
        """Return Mark"""
        return self._Mark

    def __str__(self):
        """Class's String is Name of the player"""
        return self.returnName()

    def __bool__(self):
        """Class's Boolean is Turn of the player"""
        return self.returnTurn()
