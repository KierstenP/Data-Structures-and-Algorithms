#part a
def powersOfTen():
    return [10**i for i in range(6)]

#part b
def consecutiveNumberProducts():
    return [n * (n+1) for n in range(10)]

#part c
def alphabet():
    return [chr(n) for n in range(97, 123)]

def main():
    print(powersOfTen())
    print(consecutiveNumberProducts())
    print(alphabet())
