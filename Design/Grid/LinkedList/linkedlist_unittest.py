# Importing official modules
import os
import sys
import logging
import unittest

# Directories of Node
dir = os.path.dirname(__file__)
dir = dir + '/Node'
sys.path.insert(1, dir)

# Importing custom modules
from linkedlist import LinkedList
from node import Node

root_logger = logging.getLogger()
root_logger.disabled = False

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.LinkedL = LinkedList()
        self.test1 = Node('test1', 123)
        self.test2 = Node('test2', 456)
        self.test3 = Node('test3', 789)

    def testReturn(self):
        self.LinkedL.pushS(self.test1)
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test1)
        self.assertEqual(self.LinkedL.returnSize(), 1)

    def testPush(self):
        self.LinkedL.pushS(self.test1)
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test1)
        self.assertEqual(self.LinkedL.returnSize(), 1)
        self.LinkedL.pushS(self.test2)
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test2)
        self.assertEqual(self.LinkedL.returnSize(), 2)
        self.LinkedL.pushS(self.test3)
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test3)
        self.assertEqual(self.LinkedL.returnSize(), 3)

        head = self.LinkedL.returnHead()
        test1 = head
        test2 = test1.returnNext()
        test3 = test2.returnNext()
        self.assertEqual(test1, self.test1)
        self.assertEqual(test2, self.test2)
        self.assertEqual(test3, self.test3)

        tail = self.LinkedL.returnTail()
        test3 = tail
        test2 = test3.returnPrev()
        test1 = test2.returnPrev()

    def testPop(self):
        self.LinkedL.pushS(self.test1)
        self.LinkedL.pushS(self.test2)
        self.LinkedL.pushS(self.test3)

        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test3)
        self.assertEqual(self.LinkedL.returnSize(), 3)

        self.LinkedL.popS()
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test2)
        self.assertEqual(self.LinkedL.returnSize(), 2)

        self.LinkedL.popS()
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test1)
        self.assertEqual(self.LinkedL.returnSize(), 1)

        self.LinkedL.popS()
        self.assertEqual(self.LinkedL.returnHead(), None)
        self.assertEqual(self.LinkedL.returnTail(), None)
        self.assertEqual(self.LinkedL.returnSize(), 0)

    def testExchange(self):
        self.LinkedL.pushS(self.test1)
        self.LinkedL.pushS(self.test2)
        self.LinkedL.pushS(self.test3)
        self.assertEqual(self.LinkedL.returnHead(), self.test1)
        self.assertEqual(self.LinkedL.returnTail(), self.test3)
        self.assertEqual(self.LinkedL.returnSize(), 3)

        self.LinkedL.exchangeNode(self.LinkedL.returnHead(), self.LinkedL.returnTail())
        self.assertEqual(self.LinkedL.returnHead(), self.test3)
        self.assertEqual(self.LinkedL.returnTail(), self.test1)

    def testSearchIndex(self):
        self.LinkedL.pushS(self.test1)
        self.LinkedL.pushS(self.test2)
        self.LinkedL.pushS(self.test3)

        index = self.LinkedL.searchIndex(0)
        self.assertEqual(index, self.test1)

        index2 = self.LinkedL.searchIndex(1)
        self.assertEqual(index2, self.test2)

        index3 = self.LinkedL.searchIndex(2)
        self.assertEqual(index3, self.test3)

        ind = self.LinkedL.searchIndex(3)
        self.assertEqual(ind, None)

    def testSearchValue(self):
        self.LinkedL.pushS(self.test1)
        self.LinkedL.pushS(self.test2)
        self.LinkedL.pushS(self.test3)

        val1 = self.LinkedL.searchValue(123)
        self.assertEqual(val1, self.test1)

        val2 = self.LinkedL.searchValue(456)
        self.assertEqual(val2, self.test2)

        val3 = self.LinkedL.searchValue(789)
        self.assertEqual(val3, self.test3) 

        val4 = self.LinkedL.searchValue(0)
        self.assertEqual(val4, None)

    def testSearchName(self):
        self.LinkedL.pushS(self.test1)
        self.LinkedL.pushS(self.test2)
        self.LinkedL.pushS(self.test3)

        nam1 = self.LinkedL.searchName('test1')
        self.assertEqual(nam1, self.test1)

        nam2 = self.LinkedL.searchName('test2')
        self.assertEqual(nam2, self.test2)

        nam3 = self.LinkedL.searchName('test3')
        self.assertEqual(nam3, self.test3)

        nam4 = self.LinkedL.searchName('test')
        self.assertEqual(nam4, None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
