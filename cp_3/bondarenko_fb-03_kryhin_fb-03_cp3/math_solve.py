def _inverse_element(a: int, mod: int) -> tuple:
    if a == 0:
        return mod, 0, 1
    gcd, x1, y1 = _inverse_element(mod % a, a)
    x = y1 - (mod // a) * x1
    y = x1
    return gcd, x, y


def inverse_element(a: int, mod: int) -> int:
    return _inverse_element(a, mod)[1]


def _gcd(a: int, b: int):
    if b == 0:
        return abs(a)
    else:
        return _gcd(b, a % b)


def equation_solver(a: int, b: int, mod: int) -> list or None:
    gcd = _gcd(a, mod)
    if gcd == 1:
        return [inverse_element(a, mod) * b % mod]
    elif gcd > 1:
        if b % gcd != 0:
            return None
        else:
            a1 = a // gcd
            b1 = b // gcd
            mod1 = mod // gcd
            x0 = inverse_element(a1, mod1) * b1 % mod1
            result = list()
            for i in range(gcd):
                result.append(x0 + mod1 * i)
            return result
    else:
        return None


if __name__ == "__main__":
    print(f"x = {equation_solver(5, 7, 31)[0]}")

