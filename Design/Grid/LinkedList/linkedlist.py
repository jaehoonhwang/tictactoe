# Importing official modules
import os
import sys
import logging

# # Setting Relative Path to Linked List Module
dir = os.path.dirname(__file__)
dir = dir + '/Node'
sys.path.insert(1, dir)

from node import Node

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# LinkedList Class


class LinkedList(object):

    # Constructor

    def __init__(self):
        logging.debug('LinkedList::Constructor Initialized')
        self._Head = None
        self._Tail = None
        self._Size = 0
        logging.debug('LinkedList::Constructor Finished')

    # Custom Function

    # Returning Class Variable
    def returnHead(self):
        logging.debug(('LinkedList::Return::Head: ', self._Head))
        return self._Head

    def returnTail(self):
        logging.debug(('LinkedList::Return::Tail: ', self._Tail))
        return self._Tail

    def returnSize(self):
        logging.debug(('LinkedList::Return::Size: ', self._Size))
        return self._Size

    # Setting Class Variable
    def setHead(self, head):
        logging.debug('LinkedList::Set::Head Initialized')
        logging.debug(('LinkedList::Set::Head Current: ', self._Head))
        logging.debug(('LinkedList::Set::Head Target : ', head))
        self._Head = head
        logging.debug(('LinkedList::Set::Head Changed: ', self._Head))
        logging.debug('LinkedList::Set::Head Finished')

    def setTail(self, tail):
        logging.debug('LinkedList::Set::Tail Initialized')
        logging.debug(('LinkedList::Set::Tail Current: ', self._Tail))
        logging.debug(('LinkedList::Set::Tail Target : ', tail))
        self._Tail = tail
        logging.debug(('LinkedList::Set::Tail Changed: ', self._Tail))
        logging.debug('LinkedList::Set::Tail Finished')

    # Exhcnage Two Nodes
    def exchangeNode(self, node1, node2):
        logging.debug('LinkedList::Exchange Initialized')
        logging.debug('LinkedList::Exchange::Node1 Save in Local Variables')

        logging.debug(
            ('LinkedList::Exchange::Node1::Name: ', node1.returnName()))
        name = node1.returnName()
        logging.debug(
            ('LinkedList::Exchange::Node1::Value: ', node1.returnValue()))
        value = node1.returnValue()
        logging.debug(
            ('LinkedList;:Exchange::Node1::Next: ', node1.returnNext()))
        n = node1.returnNext()
        logging.debug(
            ('LinkedList::Exchange::Node1::Prev: ', node1.returnPrev()))
        p = node1.returnPrev()

        logging.debug('LinkedList::Exchange::Node1::Exchange with Node2')
        node1.setAll(node2.returnName(), node2.returnValue(),
                     node2.returnPrev(), node2.returnNext())

        logging.debug('LinkedList::Exchange::Node2::Exhcnage with Node1')
        node2.setAll(name, value, n, p)
        if(self._Head is node1):
            self._Head = node2
        if(self._Tail is node2):
            self._Tail = node1

    # Stack Properties: Push and Pop

    # Push as Stack
    def pushS(self, node):
        logging.debug('LinkedList::PushStack Initialized')
        if(self._Head is None):
            logging.debug('LinkedList::PushStack::No Head')
            self._Head = node
            self._Tail = node
            logging.debug(('LinkedList::PushStack::Head: ', self._Head))
            logging.debug(('LinkedList::PushStack::Tail: ', self._Tail))
            self._Size = self._Size + 1
            logging.debug(('LinkedList::PushStack::Size: ', self._Size))
            logging.debug('LinkedList::PushStack Finished')
        else:
            logging.debug('LinkedList::PushStack::Head Exists')
            target_prev = self._Tail
            target_prev.setNext(node)
            node.setPrev(target_prev)
            self._Tail = node
            self._Size = self._Size + 1
            logging.debug('LinkedList::PushStack Finished')

    # Pop as Stack
    def popS(self):
        logging.debug('LinkedList::PopStack Initialized')
        if(self._Head is None):
            logging.debug(
                'LinkedList::PopStack::Warning - There is nothing to pop')
            logging.debug('LinkedList::PopStack::Finished')
        elif (self._Head is self._Tail):
            logging.debug('LinkedList::PopStack::Head is Tail')
            self._Tail.clear()
            self._Head = None
            self._Tail = None
            self._Size = self._Size - 1
            logging.debug('LinkedList::PopStack::Finished')
        else:
            logging.debug(('LinkedList::PopStack::Tail: ', self._Tail))
            tail = self._Tail.returnPrev()
            tail.setNext(None)
            self._Tail.clear()
            self._Tail = tail
            self._Size = self._Size - 1
            logging.debug('LinkedList::PopStack::Finished')

    # Search Custom Function

    # Search by Index
    def searchIndex(self, index):
        logging.debug('LinkedList::searchIndex Initialized')
        if(index > self._Size):
            logging.debug(
                'LinkedList::searchIndex Requested Index is greater than Size')
            return None
        else:
            logging.debug('LinkedList::searchIndex Initialized')
            target = self._Head
            for i in range(0, index):
                target = target.returnNext()
            logging.debug('LinkedList::searchIndex Finished')
            return target

    # Search by Value
    def searchValue(self, value):
        logging.debug('LinkedList::searchValue Intiailized')
        holder_node = self._Head
        holder = None

        while(holder_node is not None):
            if (holder_node.returnValue() == value):
                logging.debug(
                    ('LinkedList::searchValue::Value Found: ', holder_node))
                holder = holder_node
                break
            else:
                holder_node = holder_node.returnNext()
                logging.debug(
                    ('LinkedList::searchValue::Shifting: ', holder_node))

        logging.debug(('LinkedList::searchValue::Holder: ', holder))

        if(holder is None):
            logging.debug(
                ('LinkedList::searchValue::Search Failed, Particular Value has not been found: ', value))
            return None
        else:
            logging.debug(
                ('LinkedList::searchValue::Search Succeded::Returning: ', holder))
            return holder

    # Search by Name
    def searchName(self, name):
        logging.debug('LinkedList::searchName Intiailized')
        holder_node = self._Head
        holder = None

        while(holder_node is not None):
            if (holder_node.returnName() == name):
                logging.debug(
                    ('LinkedList::searchName::Name Found: ', holder_node))
                holder = holder_node
                break
            else:
                holder_node = holder_node.returnNext()

        logging.debug(('LinkedList::searchName::Holder: ', holder))

        if(holder is None):
            logging.debug(
                ('LinkedList::searchName::Search Failed, Particular Name has not been found: ', name))
            return None
        else:
            logging.debug(
                ('LinkedList::searchName::Search Succeded::Returning: ', holder))
            return holder
