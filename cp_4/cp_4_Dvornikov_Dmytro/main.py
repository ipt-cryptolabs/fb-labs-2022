from random import randint
from math import log2

interval = [pow(2, 255), pow(2, 256)]
e = 2 ** 16 + 1


def euclid_gcd(a: int, b: int) -> int:
    if b == 0:
        return abs(a)
    else:
        return euclid_gcd(b, a % b)


def euclid(num: int, mod: int) -> [int, int, int]:
    if num == 0:
        return mod, 0, 1
    else:
        gcd, x, y = euclid(mod % num, num)

        return gcd, y - (mod // num) * x, x


def find_inverse(f_inv: int, num: int) -> int:
    gcd, x, _ = euclid(f_inv, num)
    if gcd == 1:
        return x % num


def fast_pow(base: int, degree: int, module: int) -> int:
    degree = bin(degree)[2:]
    res = 1
    for i in range(len(degree) - 1, -1, -1):
        res = (res * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return res


def prep_div(p: int) -> bool:
    prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    for num in prime_nums:
        if p % num == 0 and p // num != 1:
            return False
    return True


def rabin(p: int) -> bool:
    d = p - 1
    s = 0
    while d % 2 == 0:
        s = s + 1
        d = d // 2
    if prep_div(p):
        for k in range(round(log2(p))):
            x = randint(1, p)
            print(x)
            gcd = euclid_gcd(x, p)
            if gcd == 1:
                if (fast_pow(x, d, p)) == 1 or (
                        fast_pow(x, d, p)) == -1:
                    return True
                else:
                    for r in range(1, s - 1):
                        x_in_r = fast_pow(x, d * (2 ** r),
                                          p)
                        if x_in_r == -1:
                            return True
                        elif x_in_r == 1:
                            return False
                        else:
                            continue
            else:
                return False
    return False


def find_pair(min: int, max: int) -> [int, int, int, int]:
    while True:
        rnd = []
        while len(rnd) < 4:
            prev_rnd = randint(min, max)
            print(prev_rnd)
            if rabin(prev_rnd):
                rnd.append(prev_rnd)
            else:
                continue
        pairs = [num for num in rnd]
        if pairs[0] * pairs[1] <= pairs[2] * pairs[3]:
            return pairs


def find_params(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int, int]]:
    fi_n = (p - 1) * (q - 1)
    n = p * q
    while True:
        if euclid_gcd(e, fi_n) == 1:
            d = find_inverse(e, fi_n)
            return (e, n), (d, p, q)
        else:
            continue


class CryptoSystem:
    def __init__(self, name: str, e: int, n: int, d: int):
        self.name = name
        self.e = e
        self.n = n
        self.d = d

    def encrypt(self, msg: int) -> int:
        return fast_pow(msg, self.e, self.n)

    def decrypt(self, encrypted_msg: int) -> int:
        return fast_pow(encrypted_msg, self.d, self.n)

    def sign(self, msg: int) -> int:
        return self.decrypt(msg)

    def verify(self, msg: int, sing_msg: int) -> bool:
        return True if self.encrypt(sing_msg) == msg else False

    def send_key(self, e_an_abonent: int, n_an_abonent: int, k: int) -> (int, int):
        k1 = fast_pow(k, e_an_abonent, n_an_abonent)
        s = self.sign(k)
        s1 = fast_pow(s, e_an_abonent, n_an_abonent)
        return k1, s1

    def check_sign(self, msg: int, sign_msg: int) -> bool:
        if self.verify(msg, sign_msg):
            return True
        else:
            return False

    def create_sign(self, message: int) -> int:
        return self.sign(message)

    def recieve_key(self, k1: int, s1: int, e_an_abonent: int, n_an_abonent: int) -> str:
        k = self.decrypt(k1)
        s = self.decrypt(s1)
        if fast_pow(s, e_an_abonent, n_an_abonent) == k:
            return "User auth " + str(k)
        else:
            return "User not auth " + str(k)
