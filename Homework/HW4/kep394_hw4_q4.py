def list_min(lst, low, high):
    if low == high:
        return lst[low]
    if low < high:
        min1 = list_min(lst, low + 1, high)
        min2 = lst[low]
        if min1 < min2:
            min2 = min1
        return min2
