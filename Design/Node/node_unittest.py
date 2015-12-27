import unittest
from node import Node

class TestNode(unittest.TestCase):
	def setUp(self):
		self.test1 = Node('test1', 123)
		self.test2 = Node('test2', 345, self.test1)
		self.test3 = Node('test3', 789, self.test2)
		self.test1.setNext(self.test2)
		self.test2.setNext(self.test1)

	def test_return(self):
		self.assertEqual(self.test1.returnName(), 'test1')
		self.assertEqual(self.test1.returnValue(), 123)
		self.assertEqual(self.test1.returnPrev(), None)
		self.assertEqual(self.test1.returnNext(), self.test2)

	def test_set(self):
		self.test1.setName('foo1')
		self.assertEqual(self.test1.returnName(), 'foo1')
		self.test1.setValue(321)
		self.assertEqual(self.test1.returnValue(), 321)
		self.test1.setPrev(self.test2)
		self.assertEqual(self.test1.returnPrev(), self.test2)
		self.test1.setNext(self.test3)
		self.assertEqual(self.test1.returnNext(), self.test3)

if __name__ == '__main__':
    unittest.main()