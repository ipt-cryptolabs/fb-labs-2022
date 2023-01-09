from random import getrandbits, randint
from math import gcd
from textwrap import wrap

class RSA:
    def __init__(self):
        self.p = 0
        self.q = 0
        self.oiler = 0
        self.n = 0
        self.e = 0
        self.d = 0

    def inverted_by_mod(self, a, n):
        u0, u1 = 1, 0
        while a % n:
            q = a // n
            u0, u1 = u1, u0 - q * u1
            a, n = n, a % n
        return u1
    
    def Gorner(self, base, exp, mod):
        coefs = wrap(str(bin(exp)[2:]), 1)
        coefs = (int(i) for i in coefs)
        y = 1
        for i in coefs:
            y = y ** 2 % mod
            y = (y * base ** i) % mod
        return y

    def MillerRabin(self, p, k=20):
        if p in (2, 3, 5, 7, 11):
            return True
        for i in (2, 3, 5, 7, 11):
            if not p % i:
                return False
        d = p - 1
        s = 0
        while not d % 2:
            d //= 2
            s += 1
        for i in range(k):
            x = randint(2, p - 1)
            if gcd(x, p) > 1:
                return False
            if self.Gorner(x, d, p) in (1, p - 1):
                continue
            xi = self.Gorner(x, d, p)
            for i in range(s-1):
                xi = self.Gorner(xi, 2, p)        
                if xi == p - 1:
                    break
                if xi == 1:
                    return False
            return False
        return True

    def PQCreate(self, bits):
        self.p = getrandbits(bits)
        while not self.MillerRabin(self.p):
            print(str(hex(self.p)))
            self.p = getrandbits(bits)
        self.q = getrandbits(bits)
        while not self.MillerRabin(self.q):
            print(str(hex(self.q)))
            self.q = getrandbits(bits)

    def GenerateKeyPair(self, bits=512):
        self.PQCreate(bits//2)
        self.n = self.p * self.q
        self.e = 2 ** 16 + 1
        self.oiler = (self.p - 1) * (self.q - 1)
        self.d = self.inverted_by_mod(self.e, self.oiler) % self.oiler
        return (self.n, self.e), self.d

    def Encrypt(self, msg, e, n):
        return self.Gorner(msg, e, n)

    def Decrypt(self, crpt):
        return self.Gorner(crpt, self.d, self.n)

    def Sign(self, msg):
        return msg, self.Gorner(msg, self.d, self.n)

    def Verify(self, msg, sign, e, n):
        return msg == self.Gorner(sign, e, n)

    def SendKey(self, k, e, n):
        S = self.Gorner(k, self.d, self.n)
        S1 = self.Gorner(S, e, n)
        k1 = self.Gorner(k, e, n)
        print('S =', hex(S), '\nS1 =', hex(S1), '\nk1 =', hex(k1))
        return k1, S1

    def ReceiveKey(self, k1, S1, e, n):
        k = self.Gorner(k1, self.d, self.n)
        S = self.Gorner(S1, self.d, self.n)
        print('k =', hex(k), '\nS =', hex(S))
        return k == self.Gorner(S, e, n)

if __name__ == '__main__':
    A, B = RSA(), RSA()
    A.GenerateKeyPair()
    B.GenerateKeyPair()

    print('A: p =', hex(A.p), '\nq =', hex(A.q))
    print('public A:', (hex(A.n), hex(A.e)), '\nprivate:', hex(A.d))
    print('B: p =', hex(B.p), '\nq =', hex(B.q))
    print('public B:', (hex(B.n), hex(B.e)), '\nprivate:', hex(B.d))

    msgA = 0x3f3f3f3f3f
    msgB = 0xafafafafaf
    crptA = A.Encrypt(msgA, B.e, B.n)
    crptB = B.Encrypt(msgB, A.e, A.n)
    print('msgA =', hex(msgA), '\ncrptA = ', hex(crptA), '\ndcrpA =', hex(B.Decrypt(crptA)))
    print('msgB =', hex(msgB), '\ncrptB = ', hex(crptB), '\ndcrpB =', hex(A.Decrypt(crptB)))

    sigA = A.Sign(msgA)
    sigB = B.Sign(msgB)
    print('sign A =', tuple(hex(i) for i in sigA), '\nVerify:', B.Verify(sigA[0], sigA[1], A.e, A.n))
    print('sign B =', tuple(hex(i) for i in sigB), '\nVerify:', A.Verify(sigB[0], sigB[1], B.e, B.n))

    k = 0xc00feec00fee
    print('k =', hex(k))
    if A.n > B.n:
        k1, S1 = A.SendKey(k, B.e, B.n)
        B.ReceiveKey(k1, S1, A.e, A.n)
    else:
        k1, S1 = B.SendKey(k, A.e, A.n)
        A.ReceiveKey(k1, S1, B.e, B.n)