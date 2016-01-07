import logging
import unittest
from linkedlist import LinkedList
from Node.node import Node

# root_logger = logging.getLogger()
# root_logger.disabled = False


class TestLinkedList(unittest.TestCase):

    def setup(self):
        self.LinkedL = LinkedList()
        self.test1 = Node('test1', 123)
        self.test2 = Node('test2', 345)
        self.test3 = Node('test3', 789)

    def testReturn(self):
        self.LinkedL.pushS(test1)
        self.assertEqual(self.LinkedL.returnHead(), test1)



if __name__ == '__main__':
    unittest.main(verbosity=2)
