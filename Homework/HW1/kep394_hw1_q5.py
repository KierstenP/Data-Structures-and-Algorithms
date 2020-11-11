def fibs(n):
    fibonacciList = []
    for i in range(0, n):
        if i < 2:
            fibonacciList.append(1)
            yield(1)

        else:
            firstNum = fibonacciList[i-1]
            secondNum = fibonacciList[i-2]
            fibonacciList.append(firstNum + secondNum)
            yield(firstNum + secondNum)

def main():
    for curr in fibs(8):
        print(curr)
