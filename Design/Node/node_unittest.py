import logging
import unittest
from node import Node

root_logger = logging.getLogger()
root_logger.disabled = True

class TestNode(unittest.TestCase):

	def setUp(self):
		self.test1 = Node('test1', 123)
		self.test2 = Node('test2', 345, self.test1)
		self.test3 = Node('test3', 789, self.test2)
		self.test1.setNext(self.test2)
		self.test2.setNext(self.test1)


	def testReturn(self):
		self.assertEqual(self.test1.returnName(), 'test1')
		self.assertEqual(self.test1.returnValue(), 123)
		self.assertEqual(self.test1.returnPrev(), None)
		self.assertEqual(self.test1.returnNext(), self.test2)


	def testSet(self):
		self.test1.setName('foo1')
		self.assertEqual(self.test1.returnName(), 'foo1')
		self.test1.setValue(321)
		self.assertEqual(self.test1.returnValue(), 321)
		self.test1.setPrev(self.test2)
		self.assertEqual(self.test1.returnPrev(), self.test2)
		self.test1.setNext(self.test3)
		self.assertEqual(self.test1.returnNext(), self.test3)


	def testSetAll(self):
		name = 'setAll'
		value = 1337
		prev = self.test2
		n = self.test3
		
		self.test1.setName(name)
		self.test1.setValue(value)
		self.test1.setPrev(prev)
		self.test1.setNext(n)

		self.assertEqual(self.test1.returnName(), name)
		self.assertEqual(self.test1.returnValue(), value)
		self.assertEqual(self.test1.returnPrev(), prev)
		self.assertEqual(self.test1.returnNext(), n)

if __name__ == '__main__':
    unittest.main(verbosity=2)