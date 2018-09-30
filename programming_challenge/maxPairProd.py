#python2


def max_pair_prod(a):
    x = 0
    y = 0
    c = 0
    for k in range(n):
        if a[k] > x:
            x = a[k]
            c = k
    for j in range(n):
        if j != c:
            if a[j] > y:
                y = a[j]

    return x * y


if __name__ == '__main__':
    n = int(raw_input())
    a = [int(i) for i in raw_input().split()]
    print(max_pair_prod(a))

