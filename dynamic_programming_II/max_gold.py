# Uses python2
import sys
import numpy as np
# no repetitions

def optimal_weight(W, w):

    matrix = np.zeros(shape=(len(w), W + 1), dtype=int)

    for j in range(0, len(w)):
        for x in range(1, W + 1):
            if w[j] > x:
                matrix[j, x] = matrix[j - 1, x]
            else:
                matrix[j, x] = max(w[j] + matrix[j - 1, x - w[j]] , matrix[j - 1, x])
            print matrix
    return matrix[len(w) - 1, W]

if __name__ == '__main__':
    input = sys.stdin.read()
    inputs = list(map(int, input.split()))
    W, n, w = inputs[0], inputs[1], inputs[2:]
    print optimal_weight(W, w)

