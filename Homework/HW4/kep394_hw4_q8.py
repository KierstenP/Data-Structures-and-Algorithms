def flat_list(lst, low, high, isCtrl = True):
    if isCtrl == True:
        lst = lst[low:high + 1]
        flag = False
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        return flat_list(lst[0], low, high, flag) + flat_list(lst[1:], low, high, flag)
    return lst[:1] + flat_list(lst[1:], low, high, isCtrl)