def permutation(lst, low, high, empty = True):
    if empty:
        lst[low:high]
        empty = False
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        lst = []
        for i in range(len(lst)):
            x = lst[i]
            y = lst[:i] + lst[i+1:]
            for j in permutation(y, low, high, empty):
                lst.append([x] + j)
        return lst