import random
import math

x, y = 0, 1


def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


def gcdExtended(a, b):
    global x, y
    if (a == 0):
        x = 0
        y = 1
        return b
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
    x = y1 - (b // a) * x1
    y = x1

    return gcd


def modInverse(A, M):
    g = gcdExtended(A, M)
    if g != 1:
        print("Inverse doesn't exist")

    else:
        res = (x % M + M) % M
        return res


def miller_rabin(p, k=20):

    if p % 2 == 0 or p % 3 == 0 or p % 5 == 0 or p % 7 == 0:
        return False
    r = 0
    d = p - 1
    while d % 2 == 0:
        r += 1
        d = d // 2
    for i in range(k):
        a = random.randrange(2, p - 1)
        x = pow(a, d, p)
        if x == 1 or x == p - 1:
            continue
        j = 0
        while j < r - 1:
            x = pow(x, 2, p)
            if x == p - 1:
                break
            j += 1
        if x != p - 1:
            return False
    return True


def gen256bit():
    number = '1'
    for _ in range(255):
        number += str(random.randint(0, 1))
    return int(number, 2)


def GenerateKeyPair():
    p_and_q = []
    key_pairs = [[], [], [], []]
    print('discarded candidates for p and q:\n')
    while True:
        i = 1
        t = gen256bit()
        if miller_rabin(t) is True:
            # p_and_q.append(t)
            while True:
                temp = 2 * i * t + 1
                if miller_rabin(temp) is True:
                    p_and_q.append(temp)
                    break
                else:
                    print(temp)
                i += 1
        else:
            print(t)
        if len(p_and_q) == 4:
            break
    p = p_and_q[0]
    q = p_and_q[1]
    p_1 = p_and_q[2]
    q_1 = p_and_q[3]
    if p * q >= p_1 * q_1:
        p, q = p_1, q_1
    n = p * q
    n_1 = p_1 * q_1
    phi = (p - 1) * (q - 1)
    phi_1 = (p_1 - 1) * (q_1 - 1)
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
    while True:
        e_1 = random.randint(2, phi_1 - 1)
        if gcd(e_1, phi_1) == 1:
            break
    d = modInverse(e, phi)
    d_1 = modInverse(e_1, phi_1)
    key_pairs[0].append(n)
    key_pairs[0].append(e)
    key_pairs[1].append(d)
    key_pairs[1].append(p)
    key_pairs[1].append(q)
    key_pairs[2].append(n_1)
    key_pairs[2].append(e_1)
    key_pairs[3].append(d_1)
    key_pairs[3].append(p_1)
    key_pairs[3].append(q_1)
    return key_pairs


def Encrypt(message, n, e):
    cryptogram = pow(message, e, n)
    return cryptogram


def Decrypt(cryptogram, n, d):
    message = pow(cryptogram, d, n)
    return message


def Sign(message, d, n):
    sign = pow(message, d, n)
    return sign


def Verify(message, sign, e, n):
    if message % n == pow(sign, e, n):
        return True
    else:
        return False


def SendKey(n, e, d, n_1, e_1):
    message = []
    k = random.randint(1, n - 1)
    k_1 = pow(k, e_1, n_1)
    sign = pow(k, d, n)
    print('S - ', hex(sign))
    sign_1 = pow(sign, e_1, n_1)
    message.append(k_1)
    message.append(sign_1)
    return message


def ReceiveKey(k_1, sign_1, d_1, n, e, n_1):
    k = pow(k_1, d_1, n_1)
    print('k ', hex(k))
    sign = pow(sign_1, d_1, n_1)
    print('s ', hex(sign))
    k = pow(sign, e, n)
    print('k ', hex(k))


if __name__ == "__main__":
    public1, d1, public2, d2 = GenerateKeyPair()
    print(public1, d1, public2, d2)
    while public1[0] == public2[0] or public2[0] < public1[0]:
        public1, d1, public2, d2 = GenerateKeyPair()
        print(public1, d1, public2, d2)
    M = 51
    print('BYTE = 0x33')
    # e = 38946907631
    # n = 53285498671
    # d = 44376217071
    # d1[0] = 0x806719246686C32A89DDFFAA3C3738410831F2E64C2CBE7B483C692235487C39
    # ciphered = 0x0FEA3C56E2E5E634D990A06E99AF66D282AAFA89C5C1EB52495A7525271A0DCE
    # print('decrypted', hex(Decrypt(ciphered, 0x806719246686C32A89DDFFAA3C3738410831F2E64C2CBE7B483C692235487C39, d1[0])))
    # public1[0] = 0x14135765b3dc519cbed0e410bf6aecb865768570ee17ca87e37d603d9d7720a916ef63ccca66641d085047a112851ae6619ffcf241760f99b52e07f1001e872d3eef
    # public1[1] = 0xc7989dc29b69d2eb9d713d1c04ebc4fa2fe026c75a17683e2a4f6d894ede7e4e11410ae7ede2df319c900ead91229f11f7a41fd00d98d5d989189282dc5406e6c05
    # public2[0] = 0x9aaec883778ff000d7c6708cee64cfffff5faaa14179cbaa37b36c57c0cbb27e93e3d49dfc824837e7b559555fbcc6e36b191e4931e1166218d2b39f1fce28dd8973
    # public2[1] = 0x3ade208365176e0edad1e7beb98623a17ce8d117e4d2cf57548080ecf680437fcc5859d64dbc139038e738d68c1f03bb90ed97b486f60c4013b9b31e96b6ed83a545
    # d1[0] = 0xa7ba32ea880894da5e84ef6c0de3b78888bdab894695413ab329e0117e3318f829f823a78bcc277a2e5abe0d67fe531d540632c236955d8e65cd1cb5d6429324d4d
    # d2[0] = 0x8281a5fb959932907d1743c09e6dc5a71f5523a26fd1274e16c9ef63ef43b98a8c57f64baa171b066ef6b2beeceb8d7e07978c4ddf21e5eaaf4266299a8ca369f435

    print('hex n, e:', '\n', hex(public1[0]), '\n', hex(public1[1]), sep='')
    C = Encrypt(M, public1[0], public1[1])
    C2 = Encrypt(M, public2[0], public2[1])
    print('encrypted:', hex(C))
    print('encrypted 2:', hex(C2))
    # print('hex n, d:', '\n', hex(public1[0]), '\n', hex(d1[0]), sep='')
    print('decrypted', hex(Decrypt(C, public1[0], d1[0])))
    print('decrypted 2', hex(Decrypt(C, public1[0], d1[0])))
    # print('hex d, n:', '\n', hex(d1[0]), '\n', hex(public1[0]), sep='')
    signed = Sign(M, d1[0], public1[0])
    print('sign:', hex(signed))
    # print('hex e, n:', '\n', hex(public1[1]), '\n', hex(public1[0]), sep='')
    print('verification:', Verify(M, signed, public1[1], public1[0]))

    signed2 = Sign(M, d2[0], public2[0])
    print('sign2:', hex(signed2))
    print('verification:', Verify(M, signed2, public2[1], public2[0]))

    # print('hex e, n:', '\n', hex(public1[1]), '\n', hex(public1[0]), sep='')

    k1, s1 = SendKey(public1[0], public1[1], d1[0], public2[0], public2[1])
    print(f'k1 - {hex(k1)}\ns1 - {hex(s1)}')
    ReceiveKey(k1, s1, d2[0], public1[0], public1[1], public2[0])
