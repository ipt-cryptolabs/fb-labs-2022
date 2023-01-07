import math
import random


def generate_prime_number(bits):
    def get_random_number(bits):
        return random.randint(2 ** bits, 2 ** (bits + 1) - 1)

    def test_miller_rabin(p):
        if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0:
            return False

        s, d = 0, p - 1

        while d % 2 == 0:
            d //= 2
            s += 1
        assert (p - 1 == d * (2 ** s))

        x = random.randint(2, p - 2)

        if math.gcd(x, p) > 1:
            return False

        if pow(x, d, p) == 1 or pow(x, d, p) == -1:
            return True

        for _ in range(1, s - 1):
            x = (x * x) % p
            if x == -1:
                return True
            if x == 1:
                return False

        return False

    num = get_random_number(bits)
    while not test_miller_rabin(num):
        num = get_random_number(bits)

    return num


def get_pair(bits):
    pair = (generate_prime_number(bits), generate_prime_number(bits))
    return pair


def generate_keys(pair):
    n = pair[0] * pair[1]
    f = (pair[0] - 1) * (pair[1] - 1)
    e = 2**16 + 1
    d = pow(e, -1, f)
    open_key = (n, e)
    secret_key = (d, pair[0], pair[1])
    return open_key, secret_key


def encrypt(message, key):
    encrypted_message = pow(message, key[0][1], key[0][0])
    return encrypted_message


def sign(message, key):
    signed_message = (message, pow(message, key[1][0], key[0][0]))
    return signed_message


def decrypt(encrypted, key):
    decrypted_message = pow(encrypted, key[1][0], key[0][0])
    return decrypted_message


def verify(signed, message, key):
    if message == pow(signed[1], key[0][1], key[0][0]):
        print('Message is verified!')
    else:
        print('Fake sign!')


s_numbers = get_pair(256)
r_numbers = get_pair(256)

while s_numbers[0] * s_numbers[1] > r_numbers[0] * r_numbers[1]:
    s_numbers = get_pair(256)
    r_numbers = get_pair(256)

s_keys = generate_keys(s_numbers)
r_keys = generate_keys(r_numbers)
print(f'Sender public and private keys: {s_keys[0]}\n{s_keys[1]}')
print(f'Receiver public and private keys: {r_keys[0]}\n{r_keys[1]}')
msg = random.randint(3, 999999)
encrypted = encrypt(msg, r_keys)
signed = sign(msg, s_keys)
decrypted = decrypt(encrypted, r_keys)
print(f'Original message: {msg}')
print(f'Encrypted message: {encrypted}')
print(f'Signed message: {signed}')
print(f'Decrypted message: {decrypted}')
print(verify(signed, msg, s_keys))
