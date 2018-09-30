# python2
def fib(n):
    F = [None] * (2)
    F[0] = 0
    F[1] = 1
    if n <= 1:
        return F[n]
    else:
        for i in range(2, n+1):
            temp = F[1]
            F[1] = F[0] + F[1]
            F[0] = temp

        return F[1] % 10


if __name__ in '__main__':

    n = int(raw_input())
    print fib(n)
