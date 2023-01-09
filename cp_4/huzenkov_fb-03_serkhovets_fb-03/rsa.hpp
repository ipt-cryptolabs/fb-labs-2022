#ifndef RSA_HPP
#define RSA_HPP
#include "verylong.hpp"
#include "vlalgorithm.hpp"

struct private_key
{
    private_key();
    private_key(private_key&);
    private_key(vl::verylong, vl::verylong);
    vl::verylong d;
    vl::verylong n;
    private_key operator=(private_key);
};

struct public_key
{
    public_key();
    public_key(public_key&);
    public_key(vl::verylong, vl::verylong);
    vl::verylong e;
    vl::verylong n;
    public_key operator=(public_key);
};

struct key_pair
{
    key_pair();
    key_pair(key_pair&);
    key_pair(private_key, public_key);
    private_key pvt;
    public_key pub;
    key_pair operator=(key_pair);
};
vl::verylong gen_verylong(unsigned);
bool try_divide(vl::verylong&);
vl::verylong gen_in_interval(vl::verylong&);
bool is_prime(vl::verylong&);
vl::verylong find_prime(unsigned);
key_pair gen_keys();
vl::verylong encrypt(vl::verylong, public_key);
vl::verylong decrypt(vl::verylong, private_key);
vl::verylong sign(vl::verylong, private_key);
vl::verylong verify(vl::verylong, public_key);
#endif
