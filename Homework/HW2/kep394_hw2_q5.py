def split_parity(lst):
    positionOne = 0
    positionTwo = 0

    for i in range(len(lst)):
        valueOne = lst[positionOne]
        valueTwo = lst[positionTwo]

        if lst[i] % 2 == 1:
            lst[positionOne] = valueTwo
            lst[positionTwo] = valueOne
            positionOne += 1
            positionTwo += 1

        else:
            positionTwo = positionTwo + 1

    return lst

def main():
    print(split_parity([1, 2, 3, 4]))



