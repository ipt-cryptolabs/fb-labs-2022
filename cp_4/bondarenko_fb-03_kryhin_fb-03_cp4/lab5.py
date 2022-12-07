from random import randint, getrandbits


def random_int_search(limits=None, length=None):
    if limits:
        number = randint(limits[0], limits[1])
    elif length:
        number = getrandbits(length)
    else:
        number = 0

    return number


def gen_prime(limits=None, length=None):
    tmp = random_int_search(limits, length)
    while not is_prime(tmp):
        # print(f"Not prime: {tmp}")
        tmp = random_int_search(limits, length)
    return tmp


def is_prime(p, k=10):
    if p <= 1 or p == 4:
        return False
    if p <= 3 or p in (5, 7, 11, 13):
        return True
    if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0 or p % 11 == 0 or p % 13 == 0:
        return False

    d = p - 1
    m = 0
    while d % 2 == 0:
        d = d // 2
        m += 1

    for i in range(k):
        x = randint(2, p - 2)
        b = pow(x, d, p)
        if b == 1 or b == p - 1:
            continue

        for j in range(m - 1):
            b = pow(b, 2, p)
            if b == p - 1:
                break
        else:
            return False
    return True


def key_gen(p: int, q: int):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = pow(2, 16) + 1
    d = pow(e, -1, phi)
    private_key = (d, p, q)
    public_key = (n, e)
    return public_key, private_key


def encrypt(m: int, public_key: tuple):
    return pow(m, public_key[1], public_key[0])


def decrypt(c: int, private_key: tuple):
    return pow(c, private_key[0], private_key[1] * private_key[2])


def digital_signature(m: int, private_key: tuple):
    return pow(m, private_key[0], private_key[1] * private_key[2])


def sign(m, private_key):
    return m, digital_signature(m, private_key)


def signature_verification(m: int, s: int, public_key: tuple):
    return True if m == pow(s, public_key[1], public_key[0]) else False


def main():
    a_public_key, a_private_key = key_gen(
        gen_prime(length=256),
        gen_prime(length=256)
    )

    b_public_key, b_private_key = key_gen(
        gen_prime(length=512),
        gen_prime(length=512)
    )

    print("GENERATED KEYS:")
    print(f"a_public_key = {a_public_key}")
    print(f"a_private_key = {a_private_key}")
    print(f"b_public_key = {b_public_key}")
    print(f"b_private_key = {b_private_key}")

    # A side
    k = randint(100000, 10000000000000)
    k1 = encrypt(k, b_public_key)
    s = sign(k, a_private_key)
    s1 = encrypt(s[1], b_public_key)
    message = (k1, s1)
    print(f"GENERATED MESSAGE: {k}")
    print(f"SIGNATURE: {s}")
    print(f"ENCRYPTED MESSAGE: \n{message}")

    # B side
    dec_k = decrypt(message[0], b_private_key)
    dec_s = decrypt(message[1], b_private_key)
    print(f"DECRYPTED MESSAGE: {dec_k}")
    print(f"DECRYPTED SIGNATURE: {dec_s}")

    verification = signature_verification(dec_k, dec_s, a_public_key)
    print(f"VERIFICATION: {verification}")


if __name__ == "__main__":
    main()

