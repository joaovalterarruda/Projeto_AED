class Node:
    def __init__(self, data, next_node = None):
        self._data = data
        self._next = next_node

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, new_node):
        self._next = new_node
