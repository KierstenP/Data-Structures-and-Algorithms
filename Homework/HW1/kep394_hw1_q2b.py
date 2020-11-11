def shift(lst, k, direction = "left"):
    numOfShifts = k
    if direction == "right":
        while (numOfShifts > 0 ):
            valueToMove = lst[((len(lst))-1)]
            lst.insert(0, valueToMove)
            lst.pop(len(lst)-1)
            numOfShifts -= 1
        return lst
    else:
        while (numOfShifts > 0):
            currentNumber = lst[0]
            lst.remove(currentNumber)
            lst.append(currentNumber)
            numOfShifts -= 1
        return lst

def main():
    print(shift([1, 2, 3, 4, 5, 6], 2))
    print(shift([1, 2, 3, 4, 5, 6], 2, "left"))
    print(shift([1, 2, 3, 4, 5, 6], 2, "right"))



