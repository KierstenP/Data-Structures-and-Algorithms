def two_sum(srt_lst, target):
    indexOne = 0
    indexTwo = (len(srt_lst) - 1)

    for i in range(len(srt_lst)):
        sum = (srt_lst[indexOne] + srt_lst[indexTwo])

        if sum < target:
            indexOne = indexOne + 1
        elif sum > target:
            indexTwo = indexTwo - 1
        elif sum == target:
            return(indexOne, indexTwo)
        else:
            return None
def main():
    print(two_sum([-2, 7, 11, 15, 20, 21], 22))

