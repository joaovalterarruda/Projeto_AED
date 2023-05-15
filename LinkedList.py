import json

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            if self.head is None:
                self.tail = None
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None

    def update(self, old_data, new_data):
        node = self.find(old_data)
        if node is not None:
            node.data = new_data

    def insertion_sort(self, key=lambda x: x):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            sorted_head = self.__insert_sorted(sorted_head, current, key)
            current = next_node

        self.head = sorted_head

    def __insert_sorted(self, sorted_head, node, key):
        if sorted_head is None or key(node.data) <= key(sorted_head.data):
            node.next = sorted_head
            return node

        current = sorted_head
        while current.next and key(node.data) > key(current.next.data):
            current = current.next

        node.next = current.next
        current.next = node

        return sorted_head

    def to_list(self):
        lst = []
        node = self.head
        while node is not None:
            lst.append(node.data)
            node = node.next
        return lst


    def load_from_json(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        for item in data:
            self.add(item)

    def save_to_json(self, file_name):
        with open(file_name, 'w') as f:
            data = []
            current = self.head
            while current is not None:
                data.append(current.data)
                current = current.next
            json.dump(data, f, indent=4)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def __str__(self):
        current = self.head
        items = []
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return ' -> '.join(items)
