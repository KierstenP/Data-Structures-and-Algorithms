def shift(lst, k):
    numOfShifts = k
    while(numOfShifts > 0):
        currentNumber = lst[0]
        lst.remove(currentNumber)
        lst.append(currentNumber)
        numOfShifts -= 1
    return lst

def main():
    print(shift([1, 2, 3, 4, 5, 6], 2))


