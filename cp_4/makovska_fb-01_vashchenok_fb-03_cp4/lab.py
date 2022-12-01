import random


def test_miller_rabin(k):
    s = 0
    d = int(k) - 1
    while ( d % 2 == 0 ):
        s = s + 1
        d = d // 2

    for n in range(3):
        x = random.randint(2, k - 1)
        if gcd(x, k) != 1:
            return False
        if horner(x, d, k) == 1 or horner(x, d, k) == k-1:
            continue
        else:
            for i in range(0, s):
                deg = d * (2 ** i)
                xr = horner(x, deg, k)
                if xr == 1:
                    return False
                elif xr == (k-1):
                    break
                if i == s-1:
                    return False
    return True


def horner(x, a, m):
    x_pow = 1
    bin_a = str(bin(a)[2:])
    c = 0
    for n in bin_a:
        x_tmp = (x ** int(n))
        x_pow = ((x_pow ** 2) * x_tmp) %m
        c = c+1
    return x_pow


def gen_prime_numb(length):
    primes = []
    while True:
        f = open('new.txt', 'a')
        n_max = int('1' + '0' * (length+1))
        n_min = int('1' + '0' * length)
        e = random.randint(n_min, n_max)
        if (e % 2 == 0):
            e = e + 1
        res = test_miller_rabin(e)
        if res == True:
            primes.append(e)
        else:
            bad_result = "Число не пройшло перевірку на простоту: " + str(e) + "\n"
            f.write(bad_result)
        if len(primes) == 4:
            break
    primes.sort()
    f.close()
    return primes


def euclid_gcd(a, b):
    if (a==0):
        return b,0,1
    gcd, x, y = euclid_gcd(b % a, a)
    return gcd, y - (b//a) * x, x

def inverse(a, mod):
    if a < 0:
        a += mod
    d, x, y = euclid_gcd(a, mod)
    if d == 1:
        return x
    else:
        print("Неможливо знайти обернений")
        return

def mod_gcd(a, b):
    if b == 0:
        return a
    return mod_gcd(b, a % b)





#numbers = gen_prime_numb(77)
#print(numbers)
