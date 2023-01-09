from math import gcd


def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def articled_element(a, n):
    return gcdExtended(a, n)[1]


def _gcd(a: int, b: int):
    if b == 0:
        return abs(a)
    else:
        return _gcd(b, a % b)


def linear_comparison(a, b, n):
    d = _gcd(a, n)
    u = articled_element(a, n)
    if d == 1:
        return [(u * b) % n]
    elif d > 1:
        if b % d != 0:
            return None
        else:
            ans = []
            a = a // d
            b = b // d
            n = n // d
            x0 = (articled_element(a, n) * b) % n
            for i in range(d):
                ans.append(x0 + (n % d) * i)
            return ans


if __name__ == "__main__":
    print(linear_comparison(6, 20, 31))

