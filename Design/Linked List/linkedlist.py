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

        ## Exhcnage Two Nodes
        def exchangeNode(self, node1, node2):
                logging.debug('LinkedList::Exchange Initialized')
                logging.debug('LinkedList::Exchange::Node1 Save in Local Variables')

                logging.debug(('LinkedList::Exchange::Node1::Name: ', node1.returnName()))
                name = node1.returnName()
                logging.debug(('LinkedList::Exchange::Node1::Value: ', node1.returnValue()))
                value = node1.returnValue()
                logging.debug(('LinkedList;:Exchange::Node1::Next: ', node1.returnNext()))
                n = node1.returnNext()
                logging.debug(('LinkedList::Exchange::Node1::Prev: ', node1.returnPrev()))
                p = node1.returnPrev()

                logging.debug('LinkedList::Exchange::Node1::Exchange with Node2')
                node1.setAll(node2.returnName(), node2.returnValue(), node2.returnPrev(), node2.returnNext())

                logging.debug('LinkedList::Exchange::Node2::Exhcnage with Node1')
                node2.setAll(name, value, n, p)

        ## Stack Properties: Push and Pop
        def pushS(self, node):
                if(self.Head is None):
                        logging.debug('LinkedList::Push::No Head')
                        self.Head = node
                        self.Tail = node
                        self.Size = self.Size + 1
                else:
                        logging.debug('LinkedList::Push::Head Exists')
                        target_prev = self.Tail
                        self.Tail = node
                        target_prev.setNext(node)
                        target.setPrev(target_prev)
                        self.Size = self.Size + 1

        def popS(self):
                if(self.Head is None):
                        logging.debug('LinkedList::Pop::Warning - There is nothing to pop')
        else:
            logging.debug('LinkedList::Pop::Tail: ', self.Tail)
            tail = self.Tail.returnPrev()
            tail.setNext(None)
            self.Tail.setPrev(None)
            self.Tail = tail
            if tail is self.Head: