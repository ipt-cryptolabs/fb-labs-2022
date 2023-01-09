#ifndef VLALGORITHM_HPP
#define VLALGORITHM_HPP
#include "verylong.hpp"

namespace vl
{
    verylong gcdex(verylong a, verylong b, verylong &x, verylong &y);

    verylong invert(verylong a, verylong module);

    // найбільший спільний дільник (бінарний алгоритм)
    verylong gcd(verylong a, verylong b);

    // найменше спільне кратне
    verylong lcm(verylong first, verylong second);

    verylong redc_barret(verylong x, verylong n, verylong mu);

    verylong redc_mont(verylong x, verylong n, verylong, verylong);

    verylong mont(verylong x, verylong n);

    verylong addmod_barret(verylong first, verylong second, verylong module);

    verylong submod_barret(verylong first, verylong second, verylong module);

    verylong mulmod_barret(verylong first, verylong second, verylong module);

    verylong powmod_barret(verylong number, verylong power, verylong module);

    verylong pow2mod_barret(verylong number, verylong module);

    verylong addmod_mont(verylong first, verylong second, verylong module, verylong c, verylong R);

    verylong submod_mont(verylong first, verylong second, verylong module, verylong c, verylong R);

    verylong mulmod_mont(verylong first, verylong second, verylong module, verylong c, verylong R);

    verylong powmod_mont(verylong number, verylong power, verylong module, verylong c, verylong R);

    verylong pow2mod_mont(verylong number, verylong module, verylong c, verylong R);
}
#endif
