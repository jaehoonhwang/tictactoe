# /usr/local/bin/python3

import logging
import string

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False


class Player(object):

    def __init__(self, name=None):
        self._Name = name
        self._Turn = False

    def returnName(self):
        return self._Name

    def returnTurn(self):
        return self._Turn

    def setName(self, name=None):
        if name is None:
            raise TypeError("Player::setName: Input for the name is None Type")
        else:
            if isinstance(name, str):
                self._Name = name
            else:
                raise TypeError("Player::setName: Check the type for the name \
                                 (str)")

    def setTurn(self, turn=None):
        if turn is None:
            raise TypeError("Player::setTurn: Input is None Type")
        else:
            if isinstance(turn, bool):
                self._Turn = turn
            else:
                raise TypeError("Player::setTurn: Input is not Bool Type")
