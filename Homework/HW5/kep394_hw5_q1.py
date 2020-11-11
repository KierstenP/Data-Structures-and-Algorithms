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


def findIndex(lst, elem):
    counter = 0
    for i in lst:
        if i == elem:
            return counter
        counter += 1
    raise("ERROR")

def post_fix_calculator():
    lstVariable = []
    lstVariableNumber = []
    userInput = input("-->")
    firstTime = None
    operations = "-+*/"
    stack = ArrayStack()
    newVariable = False
    reAssign = False
    while userInput != "done()":
        if firstTime is None:
            lstVariable = []
            lstVariableNumber = []

        if userInput not in lstVariable:
            for i in userInput.split():
                if i not in operations and i not in lstVariable and i != "=":
                    stack.push(i)
                # OPERATION CODE
                if i in operations and not stack.is_empty():
                    second = int(stack.pop())
                    first = int(stack.pop())
                    if i == "+":
                        stack.push(first + second)
                    elif i == "-":
                        stack.push(first - second)
                    elif i == "*":
                        stack.push(first * second)
                    elif i == "/":
                        stack.push(first / second)
                if i == "=":
                    if not stack.is_empty():
                        # stack.pop()
                        lstVariable.append(stack.pop())
                        newVariable = True

                if (i in lstVariable and len(userInput) == 1) or (i in lstVariable and reAssign == True) or (
                        i in lstVariable and newVariable == True):
                    indexInVariable = findIndex(lstVariable, i)
                    stack.push(lstVariableNumber[indexInVariable])
                elif i in lstVariable and len(userInput) > 1 and "=" in userInput:
                    reAssign = True
                    reAssignIndex = findIndex(lstVariable, i)
                if i in lstVariable and "=" not in userInput:
                    stack.push(lstVariableNumber[findIndex(lstVariable, i)])

        if userInput in lstVariable:
            index = findIndex(lstVariable, userInput)
            print(lstVariableNumber[index])
        elif reAssign == True:
            lstVariableNumber[reAssignIndex] = stack.pop()
            print(lstVariable[reAssignIndex])
        elif newVariable == False and reAssign == False:
            print(stack.pop())
        elif newVariable == True:
            temp = stack.top()
            lstVariableNumber.append(stack.pop())
            indexVariable = findIndex(lstVariableNumber, temp)
            print(lstVariable[indexVariable])
        reAssign = False
        newVariable = False
        firstTime = False
        userInput = input("-->")

post_fix_calculator()
