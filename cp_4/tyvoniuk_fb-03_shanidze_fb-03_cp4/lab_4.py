from random import getrandbits, randint
# from Crypto.Util.number import bytes_to_long, long_to_bytes


def gen_int_size(size): #generate int number sized ""size"" bits
    return getrandbits(size)


def gen_int_limits(start, finish): #generate int number between the limits start/finish
    return randint(start, finish)


def linear_gcd(a: int, b: int): #returns gcd of nums
    rest = a % b
    while rest != 0:
        a = b
        b = rest
        rest = a - (b * int(a / b))
    return b


def miller_rabin(number):
    #first check basic division
    k = 8 # 2^k = 256
    if number == 2 or number == 3 or number == 5 or number == 7 or number == 11 or number == 13:
        return True
    elif number <= 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0 or number % 13 == 0:
        return False
    else: #miler-rabin
        #step 0: number - 1 = d * 2 ^ s
        s = 0
        d = number - 1
        while d % 2 == 0:
            s += 1
            d //= 2
        #step 1
        for iterations in range(k):
            random_x = gen_int_limits(2, number - 1) #important rand
            if linear_gcd(random_x, d) != 1:
                return False
            else:
                #step 2
                xd = pow(random_x, d, number) #xd = x ^ d mod number
                # step 2.1
                if xd == 1 or xd == number - 1:
                    continue
                # step 2.2
                xr = random_x #iteration parameter
                for r in range(1, s):
                    xr = pow(xr, 2, number) #xr = x(r - 1) ^ 2 mod number
                    if xr == number - 1:
                        break
                    elif xr == 1:
                        return False
                return False
        return True


def generate_prime(size):
    while True:
        number = gen_int_size(size)
        # print(f"{number} is {miller_rabin(number)}")
        is_prime = miller_rabin(number)
        if is_prime:
            return number


def generate_primes_for_keys():
    p = generate_prime(256)
    q = generate_prime(256)
    p1 = generate_prime(256)
    q1 = generate_prime(256)
    if p * q > p1 * q1:
        p, q, p1, q1 = p1, q1, p, q
    return [p, q], [p1, q1]


def private_public_keys(A, B):
    p, q, p1, q1 = A[0], A[1], B[0], B[1]
    e = 65537 #ferma prime 2^2^n + 1
    n, n1 = p * q, p1 * q1
    f, f1 = (p - 1) * (q - 1), (p1 - 1) * (q1 - 1)
    d, d1 = pow(e, -1, f), pow(e, -1, f1)
    private_A, public_A, private_B, public_B = (d, p, q), (n, e), (d1, p1, q1), (n1, e)
    return private_A, public_A, private_B, public_B


def Encrypt(M, public_B):
    n, e = public_B
    return pow(M, e, n) #C


def Decrypt(C, private_B):
    d, p, q = private_B
    return pow(C, d, p * q) #M


def Generate_Sign(k, private_A, public_B):#генерація
    d, p, q = private_A
    n1, e1 = public_B
    n = p * q
    k1 = pow(k, e1, n1)
    S = pow(k, d, n)
    S1 = pow(S, e1, n1)
    return k1, S1


def Sign(k1, S1, private_B):#конфіденційність
    d1, p1, q1 = private_B
    n1 = p1 * q1
    k = pow(k1, d1, n1)
    S = pow(S1, d1, n1)
    return k, S


def Verify(k, S, public_A):#автентифікація
    n, e = public_A
    k_ = pow(S, e, n)
    if k_ == k:
        return True
    else:
        return False


def main():
    print(f'===Keys Generation===')
    A, B = generate_primes_for_keys()
    private_A, public_A, private_B, public_B = private_public_keys(A, B)
    print(f'private_A: {private_A}')
    print(f'public_A: {public_A}')
    print(f'private_B: {private_B}')
    print(f'public_A: {public_B}')

    # print(f'===hello oleg black===')
    # cipher_word = b'hello oleg black'
    # M1 = bytes_to_long(cipher_word)
    # print(f'Message M1: {long_to_bytes(M1)}')
    # C1 = Encrypt(M1, public_B)
    # print(f'Encrypted C1: {long_to_bytes(C1)}')
    # D1 = Decrypt(C1, private_B)
    # print(f'Decrypted C1: {long_to_bytes(D1)}')

    print(f'===RSA Message Decryption===')
    #A encrypts, B decrypts
    M = gen_int_limits(1, public_A[0] - 1)
    print(f'Message M: {M}')
    C = Encrypt(M, public_B)
    print(f'Encrypted C: {C}')
    D = Decrypt(C, private_B)
    print(f'Decrypted C: {D}')
    if D == M:
        print("Correct decryption!")
    else:
        print("Incorrect decryption!")
    print(f'===RSA Signature Verification Protocol===')
    k = gen_int_limits(0, public_A[0])
    print(f'Message k: {k}')
    k1, S1 = Generate_Sign(k, private_A, public_B)
    print(f'Signed A k1, S1: {k1} {S1}')
    k, S = Sign(k1, S1, private_B)
    print(f'Designed B k, S: {k} {S}')
    verified = Verify(k, S, public_A)
    print(f'Verified B: {verified}')

if __name__ == "__main__":
    main()