# python 2

import sys

def get_optimal_value(capacity, values, weights):
    value = 0.
    a = 0
    ratios = sorted([[v / float(w), w] for v, w in zip(values, weights)], reverse=True)

    for i, item in enumerate(ratios):
        a = min(capacity, ratios[i][1])
        value += a * ratios[i][0]
        capacity -= a

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, values, weights)
    print("{:.10f}".format(opt_value))


