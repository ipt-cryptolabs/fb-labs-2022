from random import getrandbits, randint, randrange
from math import gcd

def reverse_a(a: int, b: int) -> int:
    u_0, u_1 = 1, 0
    while a % b:
        r = a % b
        q = a // b
        a, b = b, r
        u = u_0 - q * u_1
        u_0, u_1 = u_1, u
    return u_1

def MillerRabin(p: int, k: int = 16) -> bool:
    for i in (2, 3, 5, 7, 11, 13, 17):
        if not p % i and p != i:
            return False
    d = p - 1
    s = 0
    while not d % 2:
        d //= 2
        s += 1
    for i in range(k):
        # Step 1
        x = randint(2, p - 1)
        if gcd(x, p) > 1:
            return False
        # Step 2.1
        if pow(x, d, p) in (1, p - 1):
            continue
        # Step 2.2
        xi = pow(x, d, p)
        for i in range(s-1):
            xi = pow(xi, 2, p)        
            if xi == p - 1:
                break
            if xi == 1:
                return False
        return False
    return True

def pqGenerator(_len: int):
    p = getrandbits(_len)
    print('Bad p')
    while not MillerRabin(p):
        print(str(hex(p)))
        p = getrandbits(_len)
    q = getrandbits(_len)
    print('\nBad q')
    while not MillerRabin(q):
        print(str(hex(q)))
        q = getrandbits(_len)
    print('\n')
    return p, q

def GenerateKeyPair(_len: int = 256):
    p, q = pqGenerator(_len)
    n = p * q
    e = pow(2, 16) + 1
    oiler = (p - 1) * (q - 1)
    d = reverse_a(e, oiler) % oiler
    return (n, e), (d, p, q)

def Encrypt(message: int, e: int, n: int) -> int:
    return pow(message, e, n)

def Decrypt(cryptogram: int, d: int, n: int) -> int:
    return pow(cryptogram, d, n)

def Sign(message: int, d: int, n: int) -> tuple[int, int]:
    return message, pow(message, d, n)

def Verify(message: int, sign: int, e: int, n: int) -> bool:
    return message == pow(sign, e, n)

def SendKey(k: int, d: int, n: int, e1: int, n1: int) -> tuple[int, int]:
    """return: k1, S1"""
    S = pow(k, d, n)
    S1 = pow(S, e1, n1)
    k1 = pow(k, e1, n1)
    print(f"""S = {hex(S)}
S1 = {hex(S1)}
k1 = {hex(k1)}""")
    return k1, S1

def ReceiveKey(k1: int, S1: int, d1: int, n1: int, e: int, n: int) -> bool:
    k = pow(k1, d1, n1)
    S = pow(S1, d1, n1)
    print(f"""k = {hex(k)}
S = {hex(S)}""")
    return k == pow(S, e, n)