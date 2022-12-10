from random import getrandbits, randint


# task 1
def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

def findDigitIntervOrLen(length=0, interval=None):
    if length > 0:
        digit = getrandbits(length)
    elif interval is not None:
        digit = randint(interval[0], interval[1])
    else:
        return 0
    return digit


def millerRabin(digit, k= 14):
    if 1 <= digit <= 3:
        return True

    if digit % 2 == 0:
        return False
    l = 0
    d = digit - 1
    while d % 2 == 0:
        l += 1
        d //= 2
    while k:
        x = randint(2, digit - 1)
        temp = pow(x, d, digit)
        if temp == 1 or temp == digit - 1:
            k -= 1
            continue
        for i in range(l - 1):
            if pow(temp, 2, digit) == digit - 1:
                break
        else:
            return False

    return True


def genPrimeDigit(length=0, interval=None):
    digit = findDigitIntervOrLen(length, interval)
    while not millerRabin(digit):
        #print("Composite:")
        #print(digit)
        digit = findDigitIntervOrLen(length, interval)
    return digit


def rsa(pair):
    n = pair[0] * pair[1]
    phi_n = (pair[0] - 1) * (pair[1] - 1)
    #e = pow(2, 16) + 1
    e = randint(2, phi_n-1)
    while gcd(e, phi_n) !=1:
        e = randint(2, phi_n - 1)
    d = pow(e, -1, phi_n)
    priv_key = (d, pair[0], pair[1])
    pub_key = (e, n)
    keys = [priv_key, pub_key]
    return keys


def rsaEncr(number, keys):
    res = pow(number, keys[1][0], keys[1][1])
    return res


def rsaDecr(c, keys):
    res = pow(c, keys[0][0], keys[0][1] * keys[0][2])
    return res


def rsaDigitalSign(m, keys):
    res = pow(m, keys[0][0], keys[0][1] * keys[0][2])
    return m, res


def rsaSignVerific(m, s, keys):
    if m == pow(s, keys[1][0], keys[1][1]):
        return True
    else:
        return False


# task 1-2
print("task 1-2")
pair_temp_1 = [genPrimeDigit(256), genPrimeDigit(256)]
pair_temp_2 = [genPrimeDigit(256), genPrimeDigit(256)]

if pair_temp_1[0]*pair_temp_1[1] <= pair_temp_2[0]*pair_temp_2[1]:
    pair_a = pair_temp_1
    pair_b = pair_temp_2
else:
    pair_a = pair_temp_2
    pair_b = pair_temp_1
print("p,q:")
print(pair_a)
print("p1,q1:")
print(pair_b)
print("task 3")
#task3
keys_a = rsa(pair_a)
keys_b = rsa(pair_b)
print("A secret key:")
print(keys_a[0])
print("A open key:")
print(keys_a[1])
print("B secret key:")
print(keys_b[0])
print("B open key:")
print(keys_b[1])
print("task 4")
#task4
m = randint(0, keys_a[0][1] * keys_a[0][2])
print("Message")
print(m)
crypt_a = rsaEncr(m, keys_a)
print("Cryptograma A")
print(crypt_a)
crypt_b = rsaEncr(m, keys_b)
print("Cryptograma B")
print(crypt_b)
decrypt_a = rsaDecr(crypt_a, keys_a)
print("Decrypt A")
print(decrypt_a)
decrypt_b = rsaDecr(crypt_b, keys_b)
print("Decrypt B")
print(decrypt_b)

signed_a = rsaDigitalSign(m, keys_a)
print("Digital sign A")
print(signed_a[1])

signed_b = rsaDigitalSign(m, keys_b)
print("Digital sign B")
print(signed_b[1])

sign_verific_a = rsaSignVerific(signed_a[0], signed_a[1], keys_a)
print("Digital sign verification A")
print(sign_verific_a)

sign_verific_b = rsaSignVerific(signed_b[0], signed_b[1], keys_b)
print("Digital sign verification B")
print(sign_verific_b)

print("task 5")
#A (open_key_a, secret_key_a, open_key_b)
open_key_a = keys_a[1]
secret_key_a = keys_a[0]
open_key_b = keys_b[1]
k = randint(1, open_key_a[1] - 1)
print("A k:")
print(k)
s = pow(k, secret_key_a[0], open_key_a[1])
print("A S:")
print(s)
k_1 = pow(k, open_key_b[0], open_key_b[1])
s_1 = pow(s, open_key_b[0], open_key_b[1])
#B (open_key_b, secret_key_b, open_key_a)
mes = (k_1, s_1)
print("message (k1, S1):")
print(mes)
secret_key_b = keys_b[0]
k_b = pow(mes[0], secret_key_b[0], open_key_b[1])
print("B k:")
print(k_b)
s_b = pow(mes[1], secret_key_b[0], open_key_b[1])
print("B S:")
print(s_b)
k_a = pow(s_b, open_key_a[0], open_key_a[1])
print("Verify A k:")
print(k_a)
if k_a == k_b:
    print("Verified")
