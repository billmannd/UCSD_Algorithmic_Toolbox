# Uses python 2
import numpy as np

def edit_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    D = np.zeros((m, n))

    for x in xrange(m):
        D [x, 0] = x
    for y in xrange(n):
        D [0, y] = y

    for i in xrange(1, m):
        for j in xrange(1, n):
            if s[i - 1] == t[j - 1]:
                D[i, j] = min(
                    D[i-1, j] + 1,
                    D[i-1, j-1],
                    D[i, j-1] + 1
                )
            else:
                D[i, j] = min(
                    D[i - 1, j] + 1,
                    D[i - 1, j - 1] + 1,
                    D[i, j - 1] + 1
                )
    return int(D[m-1, n-1])

if __name__ == "__main__":
    first = raw_input()
    second = raw_input()

    print edit_distance(first, second)
