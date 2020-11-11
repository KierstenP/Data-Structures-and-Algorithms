def split_by_sign(lst, low, high, empty = None):
    if empty == None:
        low = 0
        high = len(lst) - 1
    if len(lst) == 1:
        return lst[0:1]
    if low < high:
        if lst[0] < 0:
            return split_by_sign(lst[1:], low, high, 1) + lst[0:1]
        if lst[0] > 0:
            return split_by_sign(lst[0:1], 0, 0, 1) + split_by_sign(lst[1:], low, high, 1)
    return lst
