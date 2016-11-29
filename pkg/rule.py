# /usr/local/bin/python3

import logging
from grid import Grid
from player import Player

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.propagate = False
logger.disabled = False


class Rule(object):

    def __init__(self, grid, player1, player2):
        self._Grid = grid
        self._P1 = player1
        self._P2 = player2
        self._winCond = False

    def setGrid(self, grid):
        """Set Grid member"""
        self._Grid = grid

    def setP1(self, p1):
        """Set Player1 member"""
        self._P1 = p1

    def setP2(self, p2):
        """Set Player2 member"""
        self._P2 = p2

    def setwinCond(self, wc=False):
        """Set Win Condition member"""
        self._winCond = wc

    def returnGrid(self):
        """Return Grid member"""
        return self._Grid

    def returnP1(self):
        """Return Player1 member"""
        return self._P1

    def returnP2(self):
        """Return Player2 member"""
        return self._P2

    def returnwinCond(self):
        """Return Win Condition member"""
        return self._winCond

    def rowCheck(self, mark):
        """Checking each row with a mark

        Using Grid's returnRow function to check each row by checking set
        length of the grid and if it has one of mark.

        Args:
            mark (chr): Mark of a player
        """
        for row in range(1, self.returnGrid().returnM()):
            if len(set(self.returnGrid().returnRow(row))) is 1 and
            self.returnGrid().returnRow()[0] is mark:
                self.setwinCond(True)
                break

    def colCheck(self, mark):
        """Checking each column with a mark

        Using Grid's returnCol function to check each row by checking set
        length of the grid and if it has one of mark.

        Args:
            mark (chr): Mark of a player
        """
        for col in range(1, self.returnGrid().returnN()):
            if len(set(self.returnGrid().returnCol(col))) is 1 and
            self.returnGrid().returnRow()[0] is mark:
                self.setwinCond(True)
                break

    def diagCheck(self, mark):
        """Checking two diagonal condition with a mark

        Checking forward and backward diagonal by using Grid' searchCoor.
        Checking it by using set length and mark.

        Args:
            mark (chr): Mark of a player

        """
        if self.returnGrid().returnM() == self.returnGrid().returnN():
            diag_ls = []
            rdiag_ls = []
            for x in range(1, self.returnGrid().returnM()):
                diag_ls.append(self.returnGrid().searchCoor(x, x))
                rdiag_ls.append(self.returnGrid().
                                searchCoor(x, self.returnGrid().returnM() - x))
            if set(len(diag_ls)) is 1 and diag_ls is mark:
                self.setwinCond(True)
                return

            if set(len(rdiag_ls)) is 1 and rdiag_ls is mark:
                self.setwinCond(True)
                return
