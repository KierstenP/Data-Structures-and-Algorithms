class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()


class ArrayDeque:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.front_ind = 0
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def add_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        first = (self.front_ind - 1) % len(self.data)
        self.data[first] = elem
        self.front_ind = first
        self.num_of_elems += 1

    def add_last(self, e):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        back = (self.front_ind + self.num_of_elems) % (len(self.data))
        self.data[back] = e
        self.num_of_elems += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % (len(self.data))
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        val = self.data[back_ind]
        self.data[back_ind] = None
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[(self.front_ind + self.num_of_elems - 1) % (len(self.data))]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

class MidStack:
    def __init__(self):
        self.arrStack = ArrayStack()
        self.arrD = ArrayDeque()
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def __len__(self):
        return self.size

    def push(self, e):
        self.arrD.add_last(e)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise Empty('It is empty')
        return self.arrD.last()

    def pop(self):
        self.size -= 1
        return self.arrD.delete_last()

    def mid_push(self, elem):
        counter = self.size // 2
        counterTogether = 0
        while counterTogether < counter:
            self.arrStack.push(self.arrD.delete_last())
            counterTogether += 1
        self.arrD.add_last(elem)
        while not self.arrStack.is_empty():
            self.arrD.add_last(self.arrStack.pop())
        self.size += 1


def test_code():
    mids = MidStack()
    mids.push(2)
    mids.push(4)
    mids.push(6)
    mids.push(8)
    mids.mid_push(10)
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    mids.push(2)
    mids.push(4)
    mids.push(6)
    mids.push(8)
    mids.push(10)
    mids.mid_push(12)
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
    print(mids.pop())
