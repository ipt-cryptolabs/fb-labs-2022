from lab4 import *

(n, e), (d, p, q) = GenerateKeyPair(256)
(n1, e1), (d1, p1, q1) = GenerateKeyPair(256)
if n > n1:
    n, n1 = n1, n
    p, q, p1, q1 = p1, q1, p, q
    e, d, e1, d1 = e1, d1, e, d
print(f"""
n = {hex(n)}
e = {hex(e)}
d = {hex(d)}
p = {hex(p)}
q = {hex(q)}
n1 = {hex(n1)}
e1 = {hex(e1)}
d1 = {hex(d1)}
p1 = {hex(p1)}
q1 = {hex(q1)}
""")
messageA = 0x42434445
messageB = 0x56575859
cryptA = Encrypt(messageA, e, n)
signA = Sign(messageA, d, n)
cryptB = Encrypt(messageB, e1, n1)
signB = Sign(messageB, d1, n1)
print(f"""
message A = {hex(messageA)}
message B = {hex(messageB)}
encrypted A = {hex(cryptA)}
encrypted B = {hex(cryptB)}
decrypted A = {hex(Decrypt(cryptA, d, n))}
decrypted B = {hex(Decrypt(cryptB, d1, n1))}
sign A = {tuple((str(hex(i))) for i in signA)}
sign B = {tuple((str(hex(i))) for i in signB)}
is message A verified? - {Verify(signA[0], signA[1], e, n)}
is message B verified? - {Verify(signB[0], signB[1], e1, n1)}
""")
k = 0x11
k1, S1 = SendKey(k, d, n, e1, n1)
rcvkey = ReceiveKey(k1, S1, d1, n1, e, n)
print(f"""
is the key not deformed? - {rcvkey}
""")