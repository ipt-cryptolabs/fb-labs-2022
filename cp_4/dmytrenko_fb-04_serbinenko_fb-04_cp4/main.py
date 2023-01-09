import random

def modular_inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x += m0
    return x

def miller_rabin(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(50):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

n = 0
lst = []
while n < 4:
    num = random.randint(2**256-1,2**257)
    if miller_rabin(num):
        if num not in lst:
            lst.append(num)
            n += 1
lst.sort()
# print(lst)

def GenerateKeyPair(p, q):
    n = p*q
    fn = (p-1)*(q-1)
    e = 65537
    d = modular_inverse(e, fn)
    return n, d

def mycal(osn, ed, n):
    ed = bin(ed)[2:]
    res = 1
    for i in range(len(ed)):
        a = int(ed[i])
        if a == 0:
            res = (res**2)%n
        else:
            res = (res**2)%n
            res = (res*osn)%n
    return res

def Encrypt(msg, e, n):
    return mycal(msg, e, n)

def Decrypt(cipher, d, n):
    return mycal(cipher, d, n)

def Sign(msg, d, n):
    return msg, mycal(msg, d, n)

def Verify(msg, sign, e, n):
    return msg == mycal(sign, e, n)

def SendKey(k, d, n, e1, n1):
    S = mycal(k, d, n)
    S1 = mycal(S, e1, n1)
    k1 = mycal(k, e1, n1)
    return k1, S1

def RecieveKey(k1, S1, d1, n1, e, n):
    k = mycal(k1, d1, n1)
    S = mycal(S1, d1, n1)
    return k == mycal(S, e, n)

p = lst[0]
q = lst[1]
p1 = lst[2]
q1 = lst[3]
e = 65537
e1 = 65537

n, d = GenerateKeyPair(p, q)
n1, d1 = GenerateKeyPair(p1, q1)

M = 123456789

C_A = Encrypt(M, e, n)
C_B = Encrypt(M, e1, n1)
M_A = Decrypt(C_A, d, n)
M_B = Decrypt(C_B, d1, n1)
sign_A = Sign(M, d, n)[1]
sign_B = Sign(M, d1, n1)[1]
Verify_A = Verify(M, sign_A, e, n)
Verify_B = Verify(M, sign_B, e1, n1)
k = random.randint(0, n)
k1, S1 = SendKey(k, d, n, e1, n1)
Key = RecieveKey(k1, S1, d1, n1, e, n)

print(f"""=============|RSA START|=============\n
Our message is: {M}
Public e, e1 = {e}
Public n = {n}
Public n1 = {n1}
Encrypted A = {C_A}
Encrypted B = {C_B}
Decrypted A = {M_A}
Decrypted B = {M_B}
Sign A = {sign_A}
Sign B = {sign_B}
Verify sign A = {Verify_A}
Verify sign B = {Verify_B}
Is key okay? - {Key}
\n=============|RSA END|=============""")