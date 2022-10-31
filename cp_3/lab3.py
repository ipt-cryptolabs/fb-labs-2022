import math

def inverted_element(e,mod): # обернений елемент за модулем 
  a = 1
  aa = 0
  b = 0
  bb = 1
  while (mod > 0):
      n = e // mod
      e, mod = mod, e % mod
      a, aa = aa, a - aa * n
      b, bb = bb, b - bb * n
  return a


def solver(a, b, n):
	# ax = b mod n
    if (a == b == n == 0):
      print("Розв'язків не існує, так як всі елементи дорівнюють нулю")
      return None
    elif (a == 0 and b != 0):
      print("Розв'язків не існує, так як перший елемент дорівнює 0, а другий не дорівнює 0")
      return None
    elif (a != 0 and b == 0):
      return 0
    elif (a == b == 0):
      return np.arange(n)
    else:
        a = a % n
        d = math.gcd(a, n)
        ans = np.zeros(d, dtype=int)
        if (b % d == 0):
            a1 = int(a/d)
            b1 = int(b/d)
            n1 = int(n/d)            
            inv = inverted_element(a1, n1)
            e0 = (b1 * inv) % n1
            for k in range(0,d):
                ans[k] = e0 + k * n1
            return ans
        else:
            print("Розв'язків не існує, так як числа", b, "та", d,"не взаємно прості")
            return None
