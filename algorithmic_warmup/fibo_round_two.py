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
        return F[1]


def pisano_numbers(x, y):
    two = x % y
    return two

if __name__ in '__main__':
    n = map(int, raw_input().split(" "))
    print pisano_numbers(fib(n[0]), n[1])
