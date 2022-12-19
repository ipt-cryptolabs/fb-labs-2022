from random import getrandbits, randint

def gorner(arg, power, mod):
    coefs = str(bin(power)[2:])
    y = 1
    for i in coefs:
        y = y ** 2 % mod
        y = (y * arg ** int(i)) % mod
    return y

def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def inverted_element(a, n):
    x0, x1 = 1, 0
    while a % n:
        q = a // n
        a, n = n, a % n
        x0, x1 = x1, x0 - q * x1
    return x1

def miller_rabin(p, k) -> bool:
    for i in (2, 3, 5, 7, 11):
        if not p % i and p != i:
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
        if gorner(x, d, p) in (1, p - 1):
            continue
        xi = gorner(x, d, p)
        for i in range(s-1):
            xi = gorner(xi, 2, p)        
            if xi == p - 1:
                break
            if xi == 1:
                return False
        else:
            return False
    return True

def pqCreate(llen):
    f = open('numbers.txt', 'w', encoding='utf-8')
    p = getrandbits(llen)
    while not miller_rabin(p, 21):
        f.write(str(hex(p)) + '\n')
        p = getrandbits(llen)
    q = getrandbits(llen)
    while not miller_rabin(q, 21):
        f.write(str(hex(q)) + '\n')
        q = getrandbits(llen)
    f.close()
    return p, q

def GenerateKeyPair(llen):
    p, q = pqCreate(llen)
    n = p * q
    e = pow(2, 16) + 1
    oiler = (p - 1) * (q - 1)
    d = inverted_element(e, oiler) % oiler
    return (n, e), (d, p, q)

def Encrypt(message, e, n):
    return gorner(message, e, n)

def Decrypt(cryptogram, d, n) -> int:
    return gorner(cryptogram, d, n)

def Sign(message, d, n):
    return message, gorner(message, d, n)

def Verify(message, sign, e, n):
    return message == gorner(sign, e, n)

def SendKey(k, d, n, e1, n1):
    S = gorner(k, d, n)
    S1 = gorner(S, e1, n1)
    k1 = gorner(k, e1, n1)
    print(f"S = {hex(S)} \nS1 = {hex(S1)} \nk1 = {hex(k1)}")
    return k1, S1

def ReceiveKey(k1, S1, d1, n1, e, n):
    k = gorner(k1, d1, n1)
    S = gorner(S1, d1, n1)
    print(f"k = {hex(k)} \nS = {hex(S)}")
    return k == gorner(S, e, n)

(n, e), (d, p, q) = GenerateKeyPair(256)
(n1, e1), (d1, p1, q1) = GenerateKeyPair(256)
print(f"n = {hex(n)} \ne = {hex(e)} \nd = {hex(d)} \np = {hex(p)} \nq = {hex(q)}")
print(f"n1 = {hex(n1)} \ne1 = {hex(e1)} \nd1 = {hex(d1)} \np1 = {hex(p1)} \nq1 = {hex(q1)}")


messageA = 0xafafafafafafaf
messageB = 0xb3b3b3b3b3b3b3
cryptA = Encrypt(messageA, e, n)
signA = Sign(messageA, d, n)
cryptB = Encrypt(messageB, e1, n1)
signB = Sign(messageB, d1, n1)
print(f"message A = {hex(messageA)} \nmessage B = {hex(messageB)} \nencrypted A = {hex(cryptA)} \nencrypted B = {hex(cryptB)}")
print(f"decrypted A = {hex(Decrypt(cryptA, d, n))} \ndecrypted B = {hex(Decrypt(cryptB, d1, n1))}")
print(f"sign A = {tuple((str(hex(i))) for i in signA)} \nsign B = {tuple((str(hex(i))) for i in signB)}")
print(f"Verified = {Verify(signA[0], signA[1], e, n)} \nVerified = {Verify(signB[0], signB[1], e1, n1)}")

k = 0x50505050505050
if n1 >= n:
    k1, S1 = SendKey(k, d, n, e1, n1)
    res = ReceiveKey(k1, S1, d1, n1, e, n)
    print(f"Is everything ok = {res}")
else:
    k1, S1 = SendKey(k, d1, n1, e, n)
    res = ReceiveKey(k1, S1, d, n, e1, n1)
    print(f"Is everything ok = {res}")