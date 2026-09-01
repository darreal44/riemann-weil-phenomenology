"""Kronecker symbol (d/n), integer d,n."""

def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError('jacobi modulus must be odd positive')
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def kronecker(d, n):
    if n == 0:
        return 1 if abs(d) == 1 else 0
    sign = 1
    if n < 0:
        n = -n
        if d < 0:
            sign = -sign
    while n % 2 == 0:
        n //= 2
        if d % 2 == 0:
            return 0
        if abs(d) % 8 in (3, 5):
            sign = -sign
    if n == 0:
        return sign
    return sign * jacobi(d, n)


def chi_tab(d, q):
    return [kronecker(d, n) for n in range(q)]


if __name__ == '__main__':
    assert chi_tab(-8, 8) == [0, 1, 0, 1, 0, -1, 0, -1]
    # dscan chi20 table
    t20 = [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1]
    assert chi_tab(-20, 20) == t20
    t23 = chi_tab(-23, 23)
    assert t23[0] == 0 and t23[1] == 1 and t23[22] == -1
    print('kronecker self-check ok')
    print('chi-23 tab', t23)
