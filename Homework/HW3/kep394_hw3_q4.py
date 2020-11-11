def remove_all(lst, value):
    positionList = []
    position = 0
    countOfRemovedItems = 1
    while(position <= (len(lst) - 1)):
        if lst[position] == value:
            positionList.append(position)
            position += 1
        else:
            position += 1
    try:
        if len(positionList) == 0:
            raise ValueError
        if len(positionList) == 1:
            position = positionList[0]
            lst.pop(position)
        else:
            while(len(positionList) != 0):
                listIndex = positionList[0]
                lst.pop(listIndex)
                positionList.pop(0)
                if len(positionList) == 0:
                    break
                else:
                    positionList[0] = (positionList[0] - countOfRemovedItems)
                    countOfRemovedItems += 1
    except ValueError:
        return("The value was not present in the list.")
    return lst

def main():
    print(remove_all([1, 2, 2, 3, 4, 5], 2))
    print(remove_all([1, 2, 3, 2, 4, 5], 2))
    print(remove_all([1, 2, 2, 3, 4], 5))
