# python 2

import numpy as np

def merge(B, C):
    p = len(B)
    q = len(C)
    D = [None]*(p+q)
    while B and C:
        if B[0] <= C[0]:
            D[-1] = B[0]
            D = D[1:] + [D[0]]
            B.pop(0)
        else:
            D[-1] = C[0]
            D = D[1:] + [D[0]]
            C.pop(0)

    # move the rest of B or C to the end of D
    E = B + C
    z = len(E)
    D = D[z-1:] + D[:z-1]
    D[-z:] = E

    return D

def merge_sort(A):
    n = len(A)
    if n<=1:
        return A

    m = n // 2
    B = merge_sort(A[:m])
    C = merge_sort(A[m:])
    return merge(B,C)


if __name__ in "__main__":
    A = [9,8,7,7,6,5]
    R = np.random.randint(10000,size=100000000)
    R = R.tolist()
    print merge_sort(R)
