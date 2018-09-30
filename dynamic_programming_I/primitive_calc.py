# Uses python2
import sys

def optimal_sequence(n):
    c = [0] * (n + 1)
    if n == 1: return [0, [1]]
    for i in range(2, n + 1):
        x = c[i - 1] + 1
        y = c[i // 2] + 1 if i % 2 == 0 else float("inf")
        z = c[i // 3] + 1 if i % 3 == 0 else float("inf")
        sp = min(x, y, z)
        c[i] = c[i - 1] + 1 if sp == x else c[i // 2] + 1 if sp == y else c[i // 3] + 1
    return [c[n], write_sequence(n, c)]


def write_sequence(n, c):
    j, sequence = n, [n]
    while j > 1:
        x = c[j - 1] + 1
        y = c[j // 2] + 1 if j % 2 == 0 else float("inf")
        z = c[j // 3] + 1 if j % 3 == 0 else float("inf")
        fp = min(x, y, z)
        if fp == x:
            sequence.append(j - 1)
            j -= 1
        elif fp == y:
            sequence.append(j // 2)
            j //= 2
        elif fp == z:
            sequence.append(j // 3)
            j //= 3
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
[num, sequence] = (optimal_sequence(n))
print(num)
for x in sequence:
    print x,
