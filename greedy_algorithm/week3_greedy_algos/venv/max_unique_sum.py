# python 2

# positive integer n
# represent as a sum of unique integers
# WANT the most integers possible
# n = 6 | output = 1 2 3
# n = 8 | output = 1 2 5
# n = 2 | output = 2

import sys
from timeit import timeit

def optimal_summands(n):
    vals = [0]*2
    # write your code here
    for i in range(n):
        k = i+1
        v = n-k
        if v <= 0 or (k*2 >= n):
            vals[1] = n
            break
        else:
            vals[0] = k
            n -= k

    return vals

if __name__ == '__main__':
    test = """
    n = int(sys.stdin.read())
    vals = optimal_summands(n)
    val_list = [i + 1 for i in range(vals[0])]
    val_list.append(vals[1])
    print(vals[0]+1)
    for i in val_list:
        print i,"""
    timeit(test)