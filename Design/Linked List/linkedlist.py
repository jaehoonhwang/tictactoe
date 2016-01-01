import logging
from Node.node import Node

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class LinkedList(object):

	# Constructor
	def __init__(self):
		logging.debug('LinkedList::Constructor Intiailized')
		self.Head = None
		self.Tail = None
		self.Size = 0
		logging.debug('LinkedList::Constructor Finished')

	# Custom Function

	## Returning Class Variable
	def returnHead(self):
		logging.debug(('LinkedList::Return::Head: ', self.Head))
		return self.Head

	def returnTail(Self):
		logging.debug(('LinkedList::Return::Tail: ', self.Tail))
		return self.Tail

	def returnSize(self):
		logging.debug(('LinkedList::Return::Size: ', self.Size))

	## Setting Class Variable
	def setHead(self, head):
		logging.debug('LinkedList::Set::Head Initialized')
		logging.debug(('LinkedList::Set::Head Current: ', self.Head))
		logging.debug(('LinkedList::Set::Head Target : ', head))
		self.Head = head
		logging.debug(('LinkedList::Set::Head Changed: ', self.Head))
		logging.debug('LinkedList::Set::Head Finished')

	def setTail(self, tail):
		logging.debug('LinkedList::Set::Tail Initialized')
		logging.debug(('LinkedList::Set::Tail Current: ', self.Tail))
		logging.debug(('LinkedList::Set::Tail Target : ', tail))
		self.Tail = tail
		logging.debug(('LinkedList::Set::Tail Changed: ', self.Tail))
		logging.debug('LinkedList::Set::Tail Finished')

	## Exchange Node
	def exchangeNode(self, node1, node2):
		logging.debug('LinkedList::Exchange::Node Initialized')
		name = node1.returnName()
		value = node1.returnValue()
		p = node1.returnPrev()
		n = node1.returnNext()
		
		logging.debug('LinkedList::Exchange::Node, First one')
		node1.setAll(node2.returnName(), node2.returnValue(), 
			node2.returnPrev(), node2.returnNext())

		logging.debug('LinkedList::Exchange::Node, Second one')
		node2.setAll(name, value, p, n)
		logging.debug('LinkedList::Exchange::Node Finished')

	## 