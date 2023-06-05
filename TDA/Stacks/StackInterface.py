class StackInterface:
    """ Interface for all ADT stack types. """

    def __init__(self):
        """
        Sets the initial state of self.
        """
        pass

    # collection accessor methods

    def is_empty(self):
        """
        Tests if self is empty.
        :return: True if len(self) is 0, otherwise False
        """
        return True

    def __len__(self):
        """
        Gets the number of items in self.
        :return: the number of items in self
        """
        return 0

    def __str__(self):
        """
        Builds the string representation of self.
        :return: String representation of self
        """
        return ""

    def __iter__(self):
        """
        Supports iteration over a view of self.
        :return: an iteration of self
        """
        return None

    # collection mutator methods

    def clear(self):
        """
        Makes self become empty.
        :return: None
        """
        pass

    # Stack accessor methods

    def peek(self):
        """
        Gets the item at the top of the stack, assuming the stack is not empty.
        :return: the top item
        """
        return None

    # Stack mutator methods

    def push(self, item):
        """
        Inserts item at the top of the stack.
        :param item: the item to insert
        :return: None
        """
        pass

    def pop(self):
        """
        Removes the item at top of the stack, assuming the stack is not empty.
        :return the item removed
        """
        return None
