# python 2

# Uses python3
import sys

def optimal_summands(n):
    summands = []
    for i in range(n):
        n -= i
        if n < i or :
            summands.append(i+n)
            break
        elif n == 0:
            summands.append(i+1)
            break
        else:
            summands.append(i+1)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print x,
