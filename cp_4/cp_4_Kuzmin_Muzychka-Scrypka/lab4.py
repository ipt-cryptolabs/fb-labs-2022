import random

minimum = 2 ** 256 - 1
maximum = 2 ** 257
e = 2 ** 16 + 1

def find_number(count):
    print("Finding p, q, p1, q1:")
    number_list = []
    print("Left to find", count - len(number_list), "numbers.")
    while len(number_list) != count:
        check = False
        while check != True:
            number = random.randint(minimum, maximum)
            check = miller_rabin(number, 60)
        if number not in number_list:
            print("Number", number, "is prime, adding it to the list.")
            number_list.append(number)
            print("Left to find", count - len(number_list), "numbers.")
    number_list.sort()
    print("All numbers found.")
    return number_list

def inverted_number(first, second):
    list = [0, 1]
    while first != 0 and second != 0:
        if first > second:
            list.append(first // second)
            first %= second
        else:
            list.append(second // first)
            second %= first
    for i in range(2, len(list)): 
        list[i] = list[i - 2] - list[i] * list[i - 1]
    return list[-2]

def GenerateKeyPair():
    var = find_number(4)
    fi = (var[0] - 1) * (var[1] - 1)
    fi1 = (var[2] - 1) * (var[3] - 1)
    d = inverted_number(e, fi)
    d1 = inverted_number(e, fi1)
    d %= fi
    d1 %= fi1
    return var[0], var[1], (var[0] * var[1]), d, var[2], var[3], (var[2] * var[3]), d1, e

def miller_rabin(number, check_count):
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        print("Number", number, "is not prime, look for another number...")
        return False
    r, s = 0, number - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for i in range(check_count):
        a = random.randrange(2, number - 1)
        x = pow(a, s, number)
        if x == 1 or x == number - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            print("Number", number, "is not prime, look for another number...")
            return False
    return True

def Horners_method(value, power, module):
    res = 1
    bin_power = str(bin(power)[2:])
    for i in range(len(bin_power)):
        res = (res ** 2) % module
        if int(bin_power[i]) != 0:
            res = (res * value) % module
    return res             

def Encrypt(M, n, e):
    C = Horners_method(M, e, n)
    return C

def Decrypt(C, n, d):
    check_M = Horners_method(C, d, n)
    return check_M

def Sign(M, n, d):
    signature = Horners_method(M, d, n)
    return signature

def Verify(signature, e, n, M):
    verify_C = Horners_method(signature, e, n)
    return M == verify_C
            
def SendKey(k, e, n1, d, n):
    print("k: ", k)
    k1 = Horners_method(k, e, n1)
    print("k1:", k1)
    S = Horners_method(k, d, n)
    S1 = Horners_method(S, e, n1)
    return S1, k1

def ReceiveKey(S1, k1, d1, n1, e, n):
    k = Horners_method(k1, d1, n1)
    S = Horners_method(S1, d1, n1)
    if k == Horners_method(S, e, n):
        return True


var_p, var_q, var_n, var_d, var_p1, var_q1, var_n1, var_d1, var_e = GenerateKeyPair()

print(f"""
p = {var_p}
q = {var_q}
n = {var_n}
e = {var_e}
d = {var_d}
p1 = {var_p1}
q1 = {var_q1}
n1 = {var_n1}
e1 = {var_e}
d1 = {var_d1}
""")

M = random.randint(2, var_n)
print("Random Message:        " , M)

C = Encrypt(M, var_n, var_e)
print("Encrypt M:             " , C )

check_M = Decrypt(C, var_n, var_d)
print("Decrypt C:             " , check_M, '\n')

signature = Sign(M, var_n, var_d)
print("Sign create:           " , signature, '\n')

print("Verify sign:           " , Verify(signature, var_e, var_n, M), '\n')

k = random.randint(0, var_n)
S1_key, k1_key = SendKey(k, var_e, var_n1, var_d, var_n)
print(ReceiveKey(S1_key, k1_key, var_d1, var_n1, var_e, var_n), '\n')