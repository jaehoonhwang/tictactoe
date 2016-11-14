import logging
import unittest
from player import Player

# TODO: Create AssertRaise cases


class PlayerUnittest(unittest.TestCase):
    """ Player Unit Test

    Command to run: python3 -m unittest tests.player_unittest --verbose

    """

    def setUp(self):
        self.test1 = Player("John Doe")
        self.test2 = Player("Jane Doe")

    def testreturnAttr(self):
        self.assertEqual(self.test1.returnName(), "John Doe")
        self.assertEqual(self.test2.returnName(), "Jane Doe")
        self.assertEqual(self.test1.returnTurn(), False)
        self.assertEqual(self.test2.returnTurn(), False)

    def testrsetAttr(self):
        self.test1.setName("Johnny Doe")
        self.test1.setTurn(True)
        self.assertEqual(self.test1.returnName(), "Johnny Doe")
        self.assertTrue(self.test1.returnTurn())

        self.test2.setName("Janey Doe")
        self.test2.setTurn(True)
        self.assertEqual(self.test2.returnName(), "Janey Doe")
        self.assertTrue(self.test2.returnTurn())

    def testspecialAttr(self):
        self.assertEqual(str(self.test1), "John Doe")
        self.assertEqual(str(self.test2), "Jane Doe")
        self.assertEqual(bool(self.test1), False)
        self.assertEqual(bool(self.test2), False)

    @unittest.expectedFailure
    def testsetNameErr(self):
        self.test1.setName(123)
        self.test1.setName(True)

    @unittest.expectedFailure
    def testsetTurnErr(self):
        self.test1.setTurn("hellO")
        self.test1.setTurn(1)
