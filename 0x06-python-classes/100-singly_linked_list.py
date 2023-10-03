#!/usr/bin/python3
"""
Defines class Node (with private data and next_node)
Defines class SinglyLinkedList (with private head and public sorted_insert)
"""


class Node:
    """
    class Node definition
    """

    def __init__(self, data, next_node=None):
        """
        Initializes node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an int")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList definition
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """
        String representation of singly linked list needed to print
        """
        string = ""
        tmpry= self.__head
        while tmpry is not None:
            string += str(tmpry.data)
            tmpry = tmpry.next_node
            if tmpry is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        n = Node(value)
        if self.__head is None:
            self.__head = n
            return

        tmpry = self.__head
        if n.data < tmpry.data:
            n.next_node = self.__head
            self.__head = n
            return

        while (tmpry.next_node is not None) and (n.data > tmpry.next_node.data):
            tmpry = tmpry.next_node
        n.next_node = tmpry.next_node
        tmpry.next_node = n
        return
