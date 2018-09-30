# python 2


import sys


def get_change(m):
    coins = [1,3,4]
    if m == 0:
        return 0
    min_coin_count = [1000] * (m+1)
    min_coin_count[0] = 0


    for i in range(1, m + 1):
        for coin in coins:

            if m - coin > -1:
                min_coin_count[i] = min(min_coin_count[i], min_coin_count[i - coin] + 1)

    #write your code here
    return min_coin_count[m]

if __name__ == '__main__':
    m = int(raw_input())
    print get_change(m)
