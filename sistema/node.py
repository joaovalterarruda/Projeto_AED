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
        """
        Get data
        :return:
        """
        return self._data

    def get_next(self):
        """
        Get next node
        :return:
        """
        return self._next

    def set_data(self, value):
        """
        Set data to new value
        :param value: New value
        :return:
        """
        self._data = value

    def set_next(self, value):
        """
        Set next node to value
        :param value: New value
        :return:
        """
        self._next = value

    def __str__(self):
        """
        Represent str
        :return:
        """
        return str(self._data)
