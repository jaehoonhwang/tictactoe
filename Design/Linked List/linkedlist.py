import logging
from Node.node import Node

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class LinkedList(object):

    # Constructor

    def __init__(self):
        logging.debug('LinkedList::Constructor Initialized')
        self.Head = None
        self.Tail = None
        self.Size = 0
        logging.debug('LinkedList::Constructor Finished')

    # Custom Function

    # Returning Class Variable
    def returnHead(self):
        logging.debug(('LinkedList::Return::Head: ', self.Head))
        return self.Head

    def returnTail(self):
        logging.debug(('LinkedList::Return::Tail: ', self.Tail))
        return self.Tail

    def returnSize(self):
        logging.debug(('LinkedList::Return::Size: ', self.Size))
        return self.Size

    # Setting Class Variable
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

    # Stack Properties: Push and Pop

    # Push as Stack
    def pushS(self, node):
        logging.debug('LinkedList::PushStack Initialized')
        if(self.Head is None):
            logging.debug('LinkedList::PushStack::No Head')
            self.Head = node
            self.Tail = node
            self.Size = self.Size + 1
            logging.debug('LinkedList::PushStack Finished')
        else:
            logging.debug('LinkedList::PushStack::Head Exists')
            target_prev = self.Tail
            self.Tail = node
            target_prev.setNext(node)
            target.setPrev(target_prev)
            self.Size = self.Size + 1
            logging.debug('LinkedList::PushStack Finished')

    # Pop as Stack
    def popS(self):
        logging.debug('LinkedList::PopStack Initialized')
        if(self.Head is None):
            logging.debug('LinkedList::PopStack::Warning - There is nothing to pop')
            logging.debug('LinkedList::PopStack::Finished')
        elif (self.Head is self.Tail):
            logging.debug('LinkedList::PopStack::Head is Tail')
            self.Tail.clear()
            self.Head = None
            self.Tail = None
            self.Size = self.Size -1 
            logging.debug('LinkedList::PopStack::Finished')
        else:
            logging.debug('LinkedList::PopStack::Tail: ', self.Tail)
            tail = self.Tail.returnPrev()
            tail.setNext(None)
            self.Tail.clear()
            self.Tail = tail
            self.Size = self.Size -1
            logging.debug('LinkedList::PopStack::Finished')

    # Search Custom Function   

    # Search by Index
    def searchIndex(self, index):
        logging.debug('LinkedList::searchIndex Initialized')
        if(index > self.Size):
            logging.debug('LinkedList::searchIndex Requested Index is greater than Size')
        else:
            logging.debug('LinkedList::searchIndex Initialized')
            head = self.Head
            for i in range(0, index):
                head = head.returnNext()
            logging.debug('LinkedList::searchIndex Finished')
            return head

    # Search by Value
    def searchValue(self, value):
        logging.debug('LinkedList::searchValue Intiailized')
        holder_node = self.Head
        holder = None
        while(holder_node.returnNext() is not None):
            if holder_node.returnValue() is value:
                holder = holder_node
                break
            else:
                holder_node = holder_node.returnNext()
        if(holder is None):
            logging.debug(('LinkedList::searchValue::Search Failed, Particular Value has not been found: ', value))
            return
        else:
            logging.debug(('LinkedList::searchValue::Search Succeded::Returning: ', holder))
            return holder

    def searchName(self, name):
        logging.debug('LinkedList::searchName Intiailized')
        holder_node = self.Head
        holder = None
        while(holder_node.returnNext() is not None):
            if holder_node.returnName() is name:
                holder = holder_node
                break
            else:
                holder_node = holder_node.returnNext()
        if(holder is None):
            logging.debug(('LinkedList::searchName::Search Failed, Particular Name has not been found: ', name))
            return
        else:
            logging.debug(('LinkedList::searchName::Search Succeded::Returning: ', holder))
            return holder
