# python 2

import sys
import random

def list_swap(array, x, y):

    array[x], array[y] = array[y], array[x]


def partition3(a, l, r):

    x = a[l]
    j = l
    num_equal = 0

    for i in range(l + 1, r + 1):
        if a[i] < x:
            j += 1
            list_swap(a, i, j)
        elif a[i] == x:
            j += 1
            num_equal += 1
            list_swap(a, i, j)
    list_swap(a, l, j)

    # Re-arrange the values equal to the pivot in the left (<) partition
    rearranged = 0
    while rearranged < num_equal:
        for z in reversed(range(l, j - rearranged)):
            if a[z] == x:
                rearranged += 1
                list_swap(a, z, j - rearranged)
    return j - num_equal, j


def randomized_quick_sort(a, l, r):

    while l < r:

        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)


        if (m1 - l) < (r - m2):
            randomized_quick_sort(a, l, m1 - 1)
            l = m2 + 1
        else:
            randomized_quick_sort(a, m2 + 1, r)
            r = m1 - 1
    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    l = list(map(int, input.split()))
    n, a = l[0], l[1:]
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print x,