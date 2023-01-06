#include "rsa.hpp"
#include <iostream>

using namespace vl;
using namespace std;

std::random_device generator;
std::uniform_int_distribution<unsigned> distribution(0x00000000, 0xffffffff);
auto gen_digit()
{
    return distribution(generator);
}

// Генерація випадкового len-розрядного (по базі 2^32) числа
verylong gen_verylong(unsigned len)
{
    verylong gen_num;
    for(unsigned i{}; i < len; i++)
        gen_num[i] = gen_digit();
    return gen_num;
}
// Навіщо воно тут?
bool try_divide(verylong& num)
{
    unsigned primes[] = {2, 3, 5, 7, 11, 13};
    for(int i = 0; i < 6; i++)
    {
        if(verylong(num % primes[i]) == 0)
            return true;
    }
    return false;
}
// Генерація випадкових чисел не більше за певний номер
verylong gen_in_interval(verylong& num)
{
    unsigned size = verylong::bit_length(num) / 32;
    verylong gen_num;
    for(unsigned i = 0; i < size; i++)
    {
        gen_num[i] = gen_digit();
    }
    gen_num = gen_num + 1;
    return gen_num;
}
// Тест Міллера-Рабіна
bool is_prime(verylong& n)
{
    verylong t = n - 1;
    verylong s = 0;
    while ((t[0] & 1) == 0)
    {
        t = t >> 1;
        s = s + 1;
    }

    for (int i = 0; i < 4; i++)
    {
        verylong a = gen_in_interval(n);
        verylong  x = powmod_barret(a, t, n);
        if (x == 1 || x == n - 1)
            continue;
        for (int j = 1; j < s; j++)
        {
            x = powmod_barret(x, 2, n);
            if (x == 1)
                return false;
            if (x == n - 1)
                break;
        }
        if (x != n - 1)
            return false;
    }
    return true;
}
// Генерація випадкових простих чисел
verylong gen_prime(unsigned len)
{
    verylong prime = gen_verylong(len/32);

    if((prime[0] & 1) == 0)
        prime = prime + 1;
    while(!is_prime(prime))
        prime = prime + 2;
    return prime;
}
// Генерація ключів
key_pair gen_keys()
{
    verylong p = gen_prime(256);
    cout << "[debug message]   " << "p = 0x" << p.to_hex_string() << endl;
    verylong q = gen_prime(256);
    cout << "[debug message]   " << "q = 0x" << q.to_hex_string() << endl;
    verylong n = p*q;
    cout << "[debug message]   " << "n = 0x" << n.to_hex_string() << endl;
    verylong phi = verylong(p-1) * verylong(q-1);
    cout << "[debug message]   " << "phi = 0x" << phi.to_hex_string() << endl;
    verylong e = gen_in_interval(phi);
    while(gcd(e, phi) != 1)
        e = e - 1;
    cout << "[debug message]   " << "e = 0x" << e.to_hex_string() << endl;
    while(e < 2 || gcd(e, phi) != 1)
        e = gen_in_interval(phi);
    verylong d = invert(e, phi);
    cout << "[debug message]   " << "d = 0x" << d.to_hex_string() << endl;
    return key_pair {{d, n}, {e, n}};
}
// Шифрування
verylong encrypt(verylong message, public_key key)
{
    return powmod_barret(message, key.e, key.n);
}
// Дешифрування
verylong decrypt(verylong cypher, private_key key)
{
    return powmod_barret(cypher, key.d, key.n);
}
// Підписати повідомлення
vl::verylong sign(vl::verylong message, private_key key)
{
    return powmod_barret(message, key.d, key.n);
}
// Перевірити підпис
vl::verylong verify(vl::verylong signature, public_key key)
{
    return powmod_barret(signature, key.e, key.n);
}

private_key::private_key() : d(), n()
{}

private_key::private_key(private_key& pk) : d(pk.d), n(pk.n)
{}

private_key::private_key(verylong nd, verylong nn) : d(nd), n(nn)
{}

private_key private_key::operator=(private_key pk)
{
    d = pk.d;
    n = pk.n;
    return *this;
}

public_key::public_key() : e(), n()
{}

public_key::public_key(public_key& pk) : e(pk.e), n(pk.n)
{}

public_key::public_key(verylong ne, verylong nn) : e(ne), n(nn)
{}

public_key public_key::operator=(public_key pk)
{
    e = pk.e;
    n = pk.n;
    return *this;
}

key_pair::key_pair() : pvt(), pub()
{}

key_pair::key_pair(key_pair& kp) : pvt(kp.pvt), pub(kp.pub)
{}

key_pair::key_pair(private_key npvt, public_key npub) : pvt(npvt), pub(npub)
{}

key_pair key_pair::operator=(key_pair kp)
{
    pvt = kp.pvt;
    pub = kp.pub;
    return *this;
}
