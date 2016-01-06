import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class Node(object):

    # Constructor

    def __init__(self, name=None, value=None, prev=None, next=None):
        logging.debug('Node::Constructor Initialized')

        self.Name = name
        logging.debug(('Node::Constructor::Name: ', self.Name))
        self.Value = value
        logging.debug(('Node::Constructor::Value: ', self.Value))
        self.Prev = prev
        logging.debug(('Node::Constructor::Prev: ', self.Prev))
        self.Next = next
        logging.debug(('Node::Constructor::Next: ', self.Next))

        logging.debug('Node::Consturctor Finalized')

    # Return Variables

    def returnName(self):
        logging.debug(('Node::Return::Name: ', self.Name))
        return self.Name

    def returnValue(self):
        logging.debug(('Node::Return::Value: ', self.Value))
        return self.Value

    def returnPrev(self):
        logging.debug(('Node::Return::Prev: ', self.Prev))
        return self.Prev

    def returnNext(self):
        logging.debug(('Node::Return::Next: ', self.Next))
        return self.Next

    # Set Variables

    def setName(self, n):
        logging.debug('Node::Set::Name Initialized')
        logging.debug(('Node::Set::Name Current: ', self.Name))
        logging.debug(('Node::Set::Name Target : ', n))
        self.Name = n
        logging.debug(('Node::Set::Name Changed: ', self.Name))
        logging.debug('Node::Set::Name Finished')

    def setValue(self, v):
        logging.debug('Node::Set::Value Initialized')
        logging.debug(('Node::Set::Value Current: ', self.Value))
        logging.debug(('Node::Set::Value Target : ', v))
        self.Value = v
        logging.debug(('Node::Set::Value Changed: ', self.Value))
        logging.debug('Node::Set::Value Finished')

    def setPrev(self, p):
        logging.debug('Node::Set::Prev Initialized')
        logging.debug(('Node::Set::Prev Current: ', self.Prev))
        logging.debug(('Node::Set::Prev Target:  ', p))
        self.Prev = p
        logging.debug(('Node::Set::Prev Changed: ', self.Prev))
        logging.debug('Node::Set Prev Finished')

    def setNext(self, n):
        logging.debug('Node::Set::Next Initialized')
        logging.debug(('Node::Set::Next Current: ', self.Next))
        logging.debug(('Node::Set::Next Target : ', n))
        self.Next = n
        logging.debug(('Node::Set::Next Changed: ', self.Next))
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
        self.Name = None
        self.Value = None
        self.Prev = None
        self.Next = None
        logging.debug('Node::Clear Finished')
