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

class MaxStack:
    def __init__(self):
        self.arrStack = ArrayStack()
        self.maxNum = None

    def __len__(self):
        return len(self.arrStack.data)

    def is_empty(self):
        if self.arrStack.is_empty():
            return True
        else:
            return False

    def push(self, e):
        if self.maxNum == None or self.maxNum < e:
            self.maxNum = e
        array_tuple = (e, self.maxNum)
        self.arrStack.data.append(array_tuple)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.arrStack.data[-1][0]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        array_tuple = self.arrStack.data[-1]
        self.arrStack.data.pop()
        return array_tuple[0]

    def max(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        maxNumber = self.arrStack.data[-1]
        return maxNumber[1]

def test_code():
    maxs = MaxStack()
    maxs.push(3)
    maxs.push(1)
    maxs.push(6)
    maxs.push(4)
    print(maxs.max())
    print(maxs.pop())
    print(maxs.pop())
    print(maxs.max())