# python 2


def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        ap = a % b

    return greatest_common_divisor(b, ap)


def least_common_multiple(a, b):
    return (a * b) / greatest_common_divisor(a, b)


if __name__ in '__main__':
    values = sorted(map(int, raw_input().split(' ')), reverse=True)
    print least_common_multiple(values[0], values[1])