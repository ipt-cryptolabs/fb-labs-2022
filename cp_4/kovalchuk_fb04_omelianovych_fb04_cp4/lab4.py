from math import gcd
from random import getrandbits
from random import randint

def inversed_by_modulo(a, m):
    a0, a1 = 1, 0
    while a % m:
        q = a // m
        a0, a1 = a1, a0 - q * a1
        a, m = m, a % m
    return a1


def MilleraRabina(p):
    k = 25
    #croc0
    for i in [2, 3, 5, 7, 11, 13, 17]:
        if not p % i and p != i:
            return False
    d = p-1
    s = 0
    while not d % 2:
        d //= 2
        s += 1
    for i in range(k):
        x = randint(1, p)
        g = gcd(x, p)
        if(g > 1):
            return False
        if pow(x, d, p) in (1, p - 1):
            continue
        xr = pow(x, d, p)
        for r in range(1, s-1):
            xr = pow(xr, 2, p)
            if xr == p-1:
                break
            if xr == 1:
                return False
        return False
    return True

def Get_couple_of_numbers_length(length):
    p = getrandbits(length)
    print("bad p's")
    while MilleraRabina(p) == False:
        print(p)
        p = getrandbits(length)
    q = getrandbits(length)
    print("bad q's")
    while MilleraRabina(q) == False:
        print(q)
        q = getrandbits(length)
    return p, q

def gen_two_pairs():
    p, q = Get_couple_of_numbers_length(256)
    p1, q1 = Get_couple_of_numbers_length(256)
    while not (p * q <= p1 * q1):
        p, q = Get_couple_of_numbers_length(256)
        p1, q1 = Get_couple_of_numbers_length(256)
    return p, q, p1, q1


def GenerateKeyPair(p, q):
    n = p * q
    phi = (p-1)*(q-1)
    e = randint(2, phi-1)
    while not (gcd(phi, e) == 1):
        e = randint(2, phi-1)
    d = inversed_by_modulo(e, phi)
    return n, e, d


def gen_keys_2pairs():
    p, q, p1, q1 = gen_two_pairs()
    n, e, d = GenerateKeyPair(p, q)
    n1, e1, d1 = GenerateKeyPair(p1, q1)
    return p, q, e, n, d, p1, q1, e1, n1, d1

def Encrypt(M, e, n):
    return pow(M, e, n)

def Decrypt(C, d, n):
    return pow(C, d, n)

def Sign(M, d, n):
    return pow(M, d, n)

def Verify(S, e, n):
    return pow(S, e, n)

def SendKey(k, d, n, e1, n1):
    S = pow(k, d, n)
    k1 = pow(k, e1, n1)
    S1 = pow(S, e1, n1)
    return k1, S1

def ReceiveKey(k1, S1, d1, n1, e, n):
    k = pow(k1, d1, n1)
    S = pow(S1, d1, n1)
    return k == pow(S, e, n)


p, q, e, n, d, p1, q1, e1, n1, d1 = gen_keys_2pairs()

M = 3408372540834758034
print("Message = ", M)
print(f"Public e = {e}\nPublic n = {n}")
print(f"Public e1 = {e1}\nPublic n1 = {n1}")
C_A = Encrypt(M, e, n)
C_B = Encrypt(M, e1, n1)
print("Encrypted from A = ", C_A)
print("Encrypted from B = ", C_B)
M_A = Decrypt(C_A, d, n)
M_B = Decrypt(C_B, d1, n1)
print("Decrypted from A = ", M_A)
print("Decrypted from B = ", M_B)
sign_A = Sign(M, d, n)
sign_B = Sign(M, d1, n1)
print("Sign from A = ", sign_A)
print("Sign from B = ", sign_B)
Verify_A = Verify(sign_A, e, n)
Verify_B = Verify(sign_B, e1, n1)
print("Verify Message sign from A = ", Verify_A == M)
print("Verify Message sign from B = ", Verify_B == M)
k = 23123123
k1, S1 = SendKey(k, d, n, e1, n1)
receiveKey = ReceiveKey(k1, S1, d1, n1, e, n)
print("Is key okay? - ", receiveKey)



