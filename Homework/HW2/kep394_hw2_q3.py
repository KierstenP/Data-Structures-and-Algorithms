def factors(num):
    factorRange = int(num**0.5) + 1
    factorList = []
    for possibleFactor in range(1, factorRange):
        if num % possibleFactor == 0:
            factorList += [possibleFactor]
            yield possibleFactor
    j = len(factorList) - 1
    if len(factorList) == 1:
        yield num
    else:
        for k in range(0, j):
            j -= 1
            yield (num // factorList[j])

def main():
    for curr_factor in factors(100):
        print(curr_factor)


