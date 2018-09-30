# Uses python 2

import sys


def largest_number(a):
    # write your code here
    x = True
    for i in a:
        if len(i) == 1:
            x = True
            break
    if x == True:
        a = sorted([int(i) for i in a])
    else:
        a = sorted([int(i) for i in a], reverse=True)
    b = map(str, a)
    c = ''.join([i for i in b])
    return c


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
