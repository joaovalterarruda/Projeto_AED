class Node:
    """ Represents a linked node"""

    def __init__(self, data, next=None):
        """
        Sets the initial state of self.
        :param data: the value of the node
        :param next: the next node
        """
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, value):
        self._data = value

    def set_next(self, value):
        self._next = value

    def __str__(self):
        return str(self._data)
