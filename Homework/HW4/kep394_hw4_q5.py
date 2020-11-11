def count_lowercase(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    if low < high:
        x = 0
        if s[low].islower():
            x = 1
        return count_lowercase(s, low + 1, high) + x


def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    if low < high:
        x = 0
        if s[low].islower():
            x = 1
        return (count_lowercase(s, low + 1, high) + x) % 2 == 0