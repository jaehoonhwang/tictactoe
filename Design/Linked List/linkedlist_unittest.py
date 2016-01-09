import logging
import unittest
from linkedlist import LinkedList
from Node.node import Node

root_logger = logging.getLogger()
root_logger.disabled = True


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.LinkedL = LinkedList()
        self.test1 = Node('test1', 123)
        self.test2 = Node('test2', 345)
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

        head = self.LinkedL.Head
        test1 = head
        test2 = test1.returnNext()
        test3 = test2.returnNext()
        self.assertEqual(test1, self.test1)
        self.assertEqual(test2, self.test2)
        self.assertEqual(test3, self.test3)

        tail = self.LinkedL.Tail
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

        self.LinkedL.exchangeNode(self.LinkedL.Head, self.LinkedL.Tail)
        self.assertEqual(self.LinkedL.returnHead(), self.test3)
        self.assertEqual(self.LinkedL.returnTail(), self.test1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
