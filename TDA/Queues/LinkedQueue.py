from typing import Optional

from TDA.LinkedNodes.node import Node


class LinkedQueue:
    """ implementation of ADT queue based on a linked structure. """

    def __init__(self, source_collection=None):
        """
        Sets the initial state of self, which includes the
        contents of source_collection, if it's present.
        :param source_collection: initial content of self
        """
        self._front: Optional[Node] = None
        self._rear: Optional[Node] = None
        self._size: int = 0

    # collection accessor methods

    def is_empty(self):
        """
        Tests if self is empty.
        :return: True if len(self) is 0, otherwise False
        """
        return self._size == 0

    def __len__(self):
        """
        Gets the number of items in self.
        :return: the number of items in self
        """
        return self._size

    def __str__(self):
        """
        Builds the string representation of self.
        :return: String representation of self
        """
        s = ""
        cursor = self._front
        while cursor is not None:
            s += str(cursor.get_data())
            cursor = cursor.get_next()
        return s

    def __iter__(self):
        """
        Supports iteration over a view of self.
        :return: an iteration of self
        """
        cursor: Node = self._front
        while cursor is not None:
            yield cursor.get_data()
            cursor = cursor.get_next()

    # collection mutator methods

    def clear(self):
        """
        Makes self become empty.
        :return: None
        """
        self._front: Optional[Node] = None
        self._rear: Optional[Node] = None
        self._size: int = 0

    # Queue accessor methods

    def peek(self):
        """
        Gets the item at the top of the queue, assuming the queue is not empty.
        :return: the top item
        """
        return self._front.get_data()

    # Queue mutator methods

    def add(self, item):
        """
        Inserts item at the rear of the queue.
        :param item: the item to insert
        :return: None
        """
        new_node = Node(item)
        if not self.is_empty():
            self._rear.set_next(new_node)
            self._rear = new_node
        else:
            self._rear = new_node
            self._front = new_node
        self._size += 1

    def pop(self):
        """
        Removes the item at top of the queue, assuming the queue is not empty
        :return the item removed
        """
        front = self._front.get_data()
        self._front = self._front.get_next()
        if self._front is None:
            self._rear = None
        self._size -= 1
        return front
