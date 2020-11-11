def e_approx(n):
    e = 0
    denominator = 1
    for i in range(0, n):
        if n == 0:
            e = 1 / 1
            return e
        else:
            e = e + (1 / denominator)
            denominator = denominator * (i + 1)
    return e

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)


main()