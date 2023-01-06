from math import gcd


def euclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = euclid(b % a, a)
        return g, y - (b // a) * x, x


def solver(a, b, mod=31):
    g = gcd(a, mod)
    if g == 1:
        return [(euclid(a, mod)[1] * b) % mod]
    elif g > 1:
        if b % g != 0:
            return None
        x0 = (euclid(a // g, mod // g)[1] * (b // g)) % (mod // g)
        roots = []
        for i in range(g):
            roots.append(x0 + i * (mod // g))
        return roots

