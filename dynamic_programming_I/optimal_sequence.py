# Uses python2
import sys

A = {}
A[0] = -1
A[1] = 0


def get_leaves(n):

    leaves = [None, None, None]
    # calculations is i

    leaves[0] = n + 1
    leaves[1] = n * 2
    leaves[2] = n * 3



    return


def grow_tree(n):
    unique_vals = [1]
    count = 0

    while n not in A:
        if len(unique_vals) >= 1:
            for u in unique_vals:
                unique = []

                if u not in A:
                    A[u] = count

                else:
                    pass

                unique += get_leaves(u)

            unique_vals += list(set(unique))
        unique_vals = list(set(unique_vals))
        count += 1

    return A

def grow_tree_opt_b(n):
    B = {}
    B[0] = -1
    B[1] = 0

    count = 0

    for i in range(1, n+1):


    return B


def descend_tree(n):

    sequence = [n]
    while n >1:
        C = {}
        if n % 3 == 0:
            x = n / 3
            C[x] = A[x]
        if n % 2 == 0:
            y = n / 2
            C[y] = A[y]
        if n:
            z = n - 1
            try:
                C[z] = A[z]
            except:
                print ""

        n = min(C.items(), key=lambda x: x[1])[0]


        sequence.append(n)
    sequence = reversed(sequence)
    return sequence


input = sys.stdin.read()
n = int(input)

gt = grow_tree_opt_b(n)
# dt = descend_tree(n)

print gt[n]
# for d in dt:
#    print d,
print ""
