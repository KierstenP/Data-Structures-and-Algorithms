from DoublyLinkedList import *

class EmptyCollection(Exception):
    pass


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        self.orig_str = orig_str
        temp = DoublyLinkedList()
        if len(self.orig_str) != 0:
            temp.add_first([self.orig_str[0], 1])
            for i in range(1, len(self.orig_str)):
                if temp.last_node().data[0] != self.orig_str[i]:
                    temp.add_last([self.orig_str[i], 1])
                else:
                    temp.last_node().data[1] += 1
        for elem in temp:
            self.data.add_last(tuple(elem))


    def __add__(self, other):
        if len(self.data) == 0 and len(other.data) !=0:
            return other
        elif len(other.data) == 0 and len(self.data) !=0:
            return self
        elif len(self.data) == 0 and len(other.data) == 0:
            return CompactString("")
        else:
            temp = CompactString(other.orig_str)
            if self.data.last_node().data[0] == temp.data.first_node().data[0]:
                num = self.data.last_node().data[1] + temp.data.first_node().data[1]
                self.data.add_last((self.data.delete_node(self.data.last_node())[0], num))
                temp.data.delete_node(temp.data.first_node())
            for elem in temp.data:
                self.data.add_last(elem)
            return self


    def __lt__(self, other):
        if len(self.data) == 0 and len(other.data) != 0:
            return True
        elif len(other.data) == 0 and len(self.data) != 0 :
            return False
        elif len(self.data) == 0 and len(other.data) != 0:
            return False
        else:
            cursor1 = self.data.first_node()
            cursor2 = other.data.first_node()
            while True:
                if cursor1 == self.data.trailer and cursor2 != other.data.trailer:
                    return True
                elif cursor1 != self.data.trailer and cursor2 == other.data.trailer:
                    return False
                elif cursor1 == self.data.trailer and cursor2 == other.data.trailer:
                    return False
                if cursor1.data[0] == cursor2.data[0]:
                    if cursor1.data[1] == cursor2.data[1]:
                        cursor1 = cursor1.next
                        cursor2 = cursor2.next
                    elif cursor1.data[1] > cursor2.data[1]:
                        cursor2 = cursor2.next
                    elif cursor1.data[1] < cursor2.data[1]:
                        cursor1 = cursor1.next
                elif cursor1.data[0] > cursor2.data[0]:
                    return False
                else:
                    return False
    def __le__(self, other):
        if len(self.data) == 0 and len(other.data) != 0:
            return True
        elif len(other.data) == 0 and len(self.data) != 0:
            return False
        elif len(self.data) == 0 and len(other.data) == 0:
            return True
        else:
            cursor1 = self.data.first_node()
            cursor2 = other.data.first_node()
            while True:
                if cursor1 == self.data.trailer and cursor2 != other.data.trailer:
                    return False
                elif cursor1 != self.data.trailer and cursor2 == other.data.trailer:
                    return True
                elif cursor1 == self.data.trailer or cursor2 == other.data.trailer:
                    return True
                if cursor1 == self.data.trailer or cursor2 == other.data.trailer:
                    return True
                if cursor1.data[0] == cursor2.data[0]:
                    if cursor1.data[1] == cursor2.data[1]:
                        cursor1 = cursor1.next
                        cursor2 = cursor2.next
                    elif cursor1.data[1] > cursor2.data[1]:
                        cursor2 = cursor2.next
                    elif cursor1.data[1] < cursor2.data[1]:
                        cursor1 = cursor1.next
                elif cursor1.data[0] > cursor2.data[0]:
                    return False
                else:
                    return True

    def __gt__(self, other):
        if len(self.data) == 0 and len(other.data) != 0:
            return False
        elif len(other.data) == 0 and len(self.data) != 0:
            return True
        elif len(self.data) == 0 and len(other.data) == 0:
            return False
        else:
            cursor1 = self.data.first_node()
            cursor2 = other.data.first_node()
            while True:
                if cursor1 == self.data.trailer and cursor2 != other.data.trailer:
                    return False
                elif cursor1 != self.data.trailer and cursor2 == other.data.trailer:
                    return True
                elif cursor1 == self.data.trailer and cursor2 == other.data.trailer:
                    return True
                if cursor1 == self.data.trailer or cursor2 == other.data.trailer:
                    return False
                if cursor1.data[0] == cursor2.data[0]:
                    if cursor1.data[1] == cursor2.data[1]:
                        cursor1 = cursor1.next
                        cursor2 = cursor2.next
                    elif cursor1.data[1] > cursor2.data[1]:
                        cursor2 = cursor2.next
                    elif cursor1.data[1] < cursor2.data[1]:
                        cursor1 = cursor1.next
                elif cursor1.data[0] > cursor2.data[0]:
                    return True
                else:
                    return False

    def __ge__(self, other):
        if len(self.data) == 0 and len(other.data) != 0:
            return False
        elif len(other.data) == 0 and len(self.data) != 0:
            return True
        elif len(self.data) == 0 and len(other.data) == 0:
            return True
        else:
            cursor1 = self.data.first_node()
            cursor2 = other.data.first_node()
            while True:
                if cursor1 == self.data.trailer and cursor2 != other.data.trailer:
                    return False
                elif cursor1 != self.data.trailer and cursor2 == other.data.trailer:
                    return True
                elif cursor1 == self.data.trailer and cursor2 == other.data.trailer:
                    return True
                if cursor1 == self.data.trailer or cursor2 == other.data.trailer:
                    return True
                if cursor1.data[0] == cursor2.data[0]:
                    if cursor1.data[1] == cursor2.data[1]:
                        cursor1 = cursor1.next
                        cursor2 = cursor2.next
                    elif cursor1.data[1] > cursor2.data[1]:
                        cursor2 = cursor2.next
                    elif cursor1.data[1] < cursor2.data[1]:
                        cursor1 = cursor1.next
                elif cursor1.data[0] > cursor2.data[0]:
                    return True
                else:
                    return False

    def __str__(self):
        string = ""
        for lst in self.data:
            string += lst[0] * lst[1]
        return string

    def __repr__(self):
        return str(self)


def test_code():
    s1 = CompactString('aaaaabbbaaac')
    s2 = CompactString('aaaaaaacccaaaa')
    s3 = s2 + s1
    print(s1 > s2)
    print(s3)


