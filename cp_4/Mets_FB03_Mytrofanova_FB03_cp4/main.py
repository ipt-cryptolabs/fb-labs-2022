import math
import random


alphabet = 'abcdefghijklmnopqrstuvwxyz'


class User:
    def __init__(self, key_length):
        self.bits = key_length
        self.pair = None
        self.secret_key = None
        self.open_key = None

    def generate_prime_number(self):

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
        num = get_random_number(self.bits)
        while not test_miller_rabin(num):
            num = get_random_number(self.bits)

        return num

    def get_pair(self):
        self.pair = (self.generate_prime_number(), self.generate_prime_number())

    def euclid(self, e, f):
        if e == 0:
            return f, 0, 1
        else:
            g, x, y = self.euclid(f % e, e)
            return g, y - (f // e) * x, x

    def generate_keys(self):
        n = self.pair[0] * self.pair[1]
        f = (self.pair[0] - 1) * (self.pair[1] - 1)
        e = random.randint(2, f - 1)
        while math.gcd(e, f) != 1:
            e = random.randint(2, f - 1)
        d = self.euclid(e, f)[1]
        self.open_key = (e, n)
        self.secret_key = (d, self.pair[0], self.pair[1])


class Sender(User):
    def __init__(self, key_length):
        self.bits = key_length
        self.message = None
        self.encrypted_message = None


class Receiver(User):
    def __init__(self, key_length):
        self.bits = key_length
        self.encrypted_message = None
        self.decrypted_message = None




a = Sender(5)
b = Receiver(5)

a.get_pair()
b.get_pair()

while a.pair[0] * a.pair[1] > b.pair[0] * b.pair[1]:
    a.get_pair()
    b.get_pair()

a.generate_keys()
b.generate_keys()










