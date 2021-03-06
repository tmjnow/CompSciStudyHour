"""
Mike McMahon
"""
from typing import List


class LinkedList(object):

    class Node(object):

        def __init__(self, data: any = None, next_node=None):
            self._data = data
            self._next = next_node

        def get_next(self):
            return self._next

        def set_next(self, next_node):
            self._next = next_node

        def set_data(self, data):
            self._data = data

        def get_data(self):
            return self._data

        def __str__(self):
            return str(self._data)

    def __init__(self, initial: List=None):
        self._size = len(initial) if initial else 0
        self._root = None
        self._tail = None

        if initial:
            for i in range(len(initial)):
                if i == 0:
                    self._root = LinkedList.Node(initial[i])
                    self._tail = self._root
                else:
                    self._tail.set_next(LinkedList.Node(initial[i]))
                    self._tail = self._tail.get_next()

    def add(self, value):
        if self._root is None:
            self._root = LinkedList.Node(value)
        else:
            node = self.get(self._size)
            node.set_next(LinkedList.Node(value))
            self._tail = node.get_next()

        self._size += 1

    def __len__(self):
        return self._size

    def remove(self, i=None):
        """
        Removes the element at a given position, if no position
        :param i:
        :return:
        """

        if i:
            if i > self._size or self._size == 0:
                raise IndexError

            if i == 0:
                self._root = self._root.get_next()

            prev = None
            to_remove = self._root
            for _ in range(0, i):
                prev = to_remove
                to_remove = to_remove.get_next()

            prev.set_next(prev.get_next().get_next())
            self._size -= 1
        else:
            self.remove(self._size)

    def get(self, i) -> Node:
        """
        O(N)
        :param i:
        :return:
        """
        if i > self._size or self._size == 0:
            raise IndexError

        if i == 0:
            return self._root

        node = self._root
        for _ in range(0, i):
            node = node.get_next()

        return node

    def search(self, value):
        """
        Given the nature of linked list we're working with O(N) time here...
        :param value:
        :return:
        """
        node = self._root
        for _ in range(0, self._size):
            if node.get_data() == value:
                return node

            node = node.get_next()

        raise ValueError("Value not found in linked list")

    def __str__(self):

        node = self._root
        str_rpr = "["
        for _ in range(0, self._size):
            str_rpr += str(node.get_data()) + ","
            node = node.get_next()

        return str_rpr[:-1] + "]"


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    llist = LinkedList(arr)
    print(len(llist))
    print(llist)
    llist.remove(3)
    print(len(llist))
    print(llist)

if __name__ == "__main__":
    main()
