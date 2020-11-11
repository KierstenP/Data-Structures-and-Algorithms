from DoublyLinkedList import *
class Empty(Exception):
    pass

class LinkedQueue:
    def __init__(self):
        self.que = DoublyLinkedList()

    def __len__(self):
        return len(self.que)

    def is_empty(self):
        return self.que.is_empty()

    def enqueue(self, elem):
        self.que.add_last(elem)

    def dequeue(self):
        if self.que.is_empty():
            raise Empty
        temp = self.que.first_node().data
        self.que.delete_node(self.que.header.next)
        return temp

    def first(self):
        return self.que.first_node().data
