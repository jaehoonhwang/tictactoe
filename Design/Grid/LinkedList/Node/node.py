import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Node(object):

    # Constructor

    def __init__(self, name=None, value=None, prev=None, next=None):
        logging.debug('Node::Constructor Initialized')

        self._Name = name
        logging.debug(('Node::Constructor::Name: ', self._Name))
        self._Value = value
        logging.debug(('Node::Constructor::Value: ', self._Value))
        self._Prev = prev
        logging.debug(('Node::Constructor::Prev: ', self._Prev))
        self._Next = next
        logging.debug(('Node::Constructor::Next: ', self._Next))

        logging.debug('Node::Consturctor Finalized')

    # Return Variables

    def returnName(self):
        logging.debug(('Node::Return::Name: ', self._Name))
        return self._Name

    def returnValue(self):
        logging.debug(('Node::Return::Value: ', self._Value))
        return self._Value

    def returnPrev(self):
        logging.debug(('Node::Return::Prev: ', self._Prev))
        return self._Prev

    def returnNext(self):
        logging.debug(('Node::Return::Next: ', self._Next))
        return self._Next

    # Set Variables

    def setName(self, n):
        logging.debug('Node::Set::Name Initialized')
        logging.debug(('Node::Set::Name Current: ', self._Name))
        logging.debug(('Node::Set::Name Target : ', n))
        self._Name = n
        logging.debug(('Node::Set::Name Changed: ', self._Name))
        logging.debug('Node::Set::Name Finished')

    def setValue(self, v):
        logging.debug('Node::Set::Value Initialized')
        logging.debug(('Node::Set::Value Current: ', self._Value))
        logging.debug(('Node::Set::Value Target : ', v))
        self._Value = v
        logging.debug(('Node::Set::Value Changed: ', self._Value))
        logging.debug('Node::Set::Value Finished')

    def setPrev(self, p):
        logging.debug('Node::Set::Prev Initialized')
        logging.debug(('Node::Set::Prev Current: ', self._Prev))
        logging.debug(('Node::Set::Prev Target:  ', p))
        self._Prev = p
        logging.debug(('Node::Set::Prev Changed: ', self._Prev))
        logging.debug('Node::Set Prev Finished')

    def setNext(self, n):
        logging.debug('Node::Set::Next Initialized')
        logging.debug(('Node::Set::Next Current: ', self._Next))
        logging.debug(('Node::Set::Next Target : ', n))
        self._Next = n
        logging.debug(('Node::Set::Next Changed: ', self._Next))
        logging.debug('Node::Set::Next Finished')

    def setAll(self, name, value, prev, n):
        logging.debug('Node::Set::All Initialized')
        self.setName(name)
        self.setValue(value)
        self.setPrev(prev)
        self.setNext(n)
        logging.debug('Node::Set::All Finished')

    def clear(self):
        logging.debug('Node::Clear Initialized')
        self._Name = None
        self._Value = None
        self._Prev = None
        self._Next = None
        logging.debug('Node::Clear Finished')
