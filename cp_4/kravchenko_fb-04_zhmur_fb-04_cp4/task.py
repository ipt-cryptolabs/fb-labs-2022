from random import getrandbits, randint
from math import gcd

def Gorner(base, exp, mod):
    c = bin(exp)[2:]
    y = 1
    for i in c:
        y = pow(y, 2, mod)
        if i == '1':
            y = y * base % mod
    return y

def reverse(a, n):
    a0, a1 = 1, 0
    while a % n:
        q, a, n = a // n, n, a % n
        a0, a1 = a1, a0 - q * a1
    return a1

def MillerRabin(p):
    k = 15
    if p in (2, 3 ,5, 7, 11, 13, 17):
        return True
    for i in (2, 3 ,5, 7, 11, 13, 17):
        if not p % i:
            return False
    d = p - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    while k:
        k -= 1
        x = randint(2, p - 1)
        if gcd(x, p) > 1:
            return False
        if Gorner(x, d, p) in (1, p - 1):
            continue
        xi = Gorner(x, d, p)
        for i in range(s-1):
            xi = Gorner(xi, 2, p)        
            if xi == p - 1:
                break
            if xi == 1:
                return False
        else:
            return False
    return True

def GimmySimple():
    with open('num.txt', 'w', encoding='utf-8') as f:
        p = getrandbits(256)
        while not MillerRabin(p):
            f.write(str(hex(p)) + '\n')
            p = getrandbits(256)
    return p

def GenerateKeyPair():
    p, q = GimmySimple(), GimmySimple()
    oil = (p - 1) * (q - 1)
    e = pow(2, 16) + 1
    n = p * q
    d = reverse(e, oil) % oil
    return (n, e), (d, p, q)

def Encrypt(msg, e, n):
    return Gorner(msg, e, n)

def Decrypt(cpt, d, n) -> int:
    return Gorner(cpt, d, n)

def Sign(msg, d, n):
    return msg, Gorner(msg, d, n)

def Verify(msg, sign, e, n):
    return msg == Gorner(sign, e, n)

def SendKey(k, d, n, e1, n1):
    S = Gorner(k, d, n)
    S1 = Gorner(S, e1, n1)
    k1 = Gorner(k, e1, n1)
    print(f"S = {hex(S)} \nS1 = {hex(S1)} \nk1 = {hex(k1)}")
    return k1, S1

def ReceiveKey(k1, S1, d1, n1, e, n):
    k = Gorner(k1, d1, n1)
    S = Gorner(S1, d1, n1)
    print(f"k = {hex(k)} \nS = {hex(S)}")
    return k == Gorner(S, e, n)

(n1, e1), (d1, p1, q1) = GenerateKeyPair()
(n2, e2), (d2, p2, q2) = GenerateKeyPair()

print(f"""
n1 = {hex(n1)}
e1 = {hex(e1)}
d1 = {hex(d1)}
p1 = {hex(p1)}
q1 = {hex(q1)}

n2 = {hex(n2)}
e2 = {hex(e2)}
d2 = {hex(d2)}
p2 = {hex(p2)}
q2 = {hex(q2)}
""")

msg1, msg2 = 0x7734773477347734, 0x5100510051005100
cpt1, cpt2 = Encrypt(msg1, e1, n1), Encrypt(msg2, e2, n2)
sig1, sig2 = Sign(msg1, d1, n1), Sign(msg2, d2, n2)

print(f"""
dsg1 = {hex(cpt1)}
dsg2 = {hex(cpt2)}
emsg1 = {hex(Decrypt(cpt1, d1, n1))}
emsg2 = {hex(Decrypt(cpt2, d2, n2))}
sig1 = {tuple((str(hex(i))) for i in sig1)}
sig2 = {tuple((str(hex(i))) for i in sig2)}
verify1 = {Verify(sig1[0], sig1[1], e1, n1)}
verify2 = {Verify(sig2[0], sig2[1], e2, n2)}
""")

k = 0xc00deedc00f
if n2 >= n1:
    k1, S1 = SendKey(k, d1, n1, e2, n2)
    res = ReceiveKey(k1, S1, d2, n2, e1, n1)
    print(f"Is everything ok = {res}")
else:
    k1, S1 = SendKey(k, d2, n2, e1, n1)
    res = ReceiveKey(k1, S1, d1, n1, e2, n2)
    print(f"Is everything ok = {res}")