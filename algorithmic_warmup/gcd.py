# python2


def greatest_common_divisor(a, b):

    if b == 0:
        return a
    else:
        ap = a % b

    return greatest_common_divisor(b, ap)


if __name__ in '__main__':
    values = sorted(map(int, raw_input().split(' ')), reverse=True)
    print greatest_common_divisor(values[0], values[1])