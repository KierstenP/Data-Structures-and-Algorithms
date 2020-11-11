#part a
def sumOfSquares(n):
    sum = 0
    for i in range(n):
        sum += (i**2)
    return sum

#part b
def singleCommandSum(n):
    return sum([(j**2) for j in range(0, n)])

#part c
def sumOfOddsSquared(n):
    sum = 0
    for i in range(n):
        if i % 2 != 0:
            sum += (i**2)
    return sum

#part d
def singleCommandOddSum(n):
    return sum([(j**2) for j in range(0, n) if ((j % 2) != 0)])

def main():
    print(sumOfSquares(10))
    print(singleCommandSum(10))
    print(sumOfOddsSquared(10))
    print(singleCommandOddSum(10))











