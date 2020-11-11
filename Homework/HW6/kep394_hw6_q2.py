from DoublyLinkedList import *

class EmptyCollection(Exception):
    pass


class Integer:
    def __init__(self, num_str):
        self.integ = DoublyLinkedList()
        for i in num_str:
            self.integ.add_last(int(i))

    def __add__(self, other):
        curr1 = self.integ.last_node()
        curr2 = other.integ.last_node()
        final = Integer("0")

        if len(self.integ) < len(other.integ):
            curr1, curr2 = curr2, curr1

        carryNumber = 0
        ctrlLoop = True
        difference = abs(self.integ.size - other.integ.size)

        while(ctrlLoop):
            temp = int(curr1.data + curr2.data + carryNumber)
            carryNumber = 0
            if temp > 9:
                carryNumber += 1
                temp -= 10
            final.integ.add_first(temp)

            if curr1.prev.data is None or curr2.prev.data is None:
                ctrlLoop = False
            else:
                curr1 = curr1.prev
                curr2 = curr2.prev
        if carryNumber > 0 and difference == 0:
            final.integ.add_first(carryNumber)
            carryNumber = 0
        for i in range(0, difference):
            while(curr1.prev.data != None):
                curr1 = curr1.prev
                temp = curr1.data +carryNumber
                carryNumber = 0
                if temp > 9:
                    carryNumber += 1
                    temp -= 10
                final.integ.add_first(temp)
        if carryNumber > 0:
            final.integ.add_first(carryNumber)
        final.integ.delete_node(final.integ.last_node())
        if final.integ.first_node().data == 0:
            final.integ.delete_node(final.integ.first_node())
        return final

    def __mul__(self, other):
        testing1 = int(str(self))
        testing2 = int(str(other))

        if testing2 > testing1:
            mult = testing1
        if testing2 < testing1:
            mult = testing1
        final = 0
        for i in range(0, mult):
            final += int(str(other))
        return final

    def __repr__(self):
        cursor1 = self.integ.first_node()
        strg = ""
        for i in range(0, len(self.integ)):
            strg = strg + str(cursor1.data)
            cursor1 = cursor1.next
        return strg


def test_code():
    n1 = Integer('375')
    n2 = Integer('4029')
    n3 = n1 + n2
    print(n3)

