""" Linked List Practice Implementation """

class Node:
    """ Node of a LinkedList """
    def __init__(self, data, next_node=None):
        self._data = data
        self.next_node = next_node

    def __next__(self):
        return self.next_node

    @property
    def data(self) -> object:
        """ Allow dot-method access to data property """
        return self._data

    @data.setter
    def data(self, val: object):
        self._data = val

class LinkedList:
    """ A linked list of nodes containing data and pointers to the next node """
    def __init__(self, head=None):
        self.head = head

    def __next__(self):
        if self.head is None:
            raise StopIteration

        return self.head
