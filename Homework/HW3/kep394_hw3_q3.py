def find_duplicates(lst):
    res_list = [0]*max(lst)
    repeat_lst = []
    for i in lst:
        res_list[i-1] += 1
    for j in range(len(res_list)):
        if res_list[j] > 1:
            repeat_lst += [j + 1]
    return repeat_lst

def main():
    print(find_duplicates([2, 4, 4, 1, 2]))
