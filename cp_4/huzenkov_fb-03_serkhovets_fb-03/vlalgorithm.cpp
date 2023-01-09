#include "verylong.hpp"
#include "vlalgorithm.hpp"

namespace vl
{
    verylong base = verylong(2).pow(digit_size);

    verylong gcdex(verylong a, verylong b, verylong &x, verylong &y)
    {
        if (b == 0)
        {
            x = verylong(1);
            y = verylong(0);
            return a;
        }
        verylong x1, y1;
        verylong d1 = gcdex(b, a % b, x1, y1);
        x = y1;
        y = x1 - (a / b) * y1;
        return d1;
    }

    verylong invert(verylong num, verylong mod)
    {
        short sign = 1;
        verylong result = 1;
        verylong res_prev = 0;
        verylong x1 = num, x2 = mod;
        if(num > mod)
            num = num % mod;
        while(x2 > 0)
        {
            verylong_result temp = x2 / x1;
            verylong x = temp.res;
            verylong rest = temp.rest;
            if(result * x + res_prev != mod)
            {
                verylong tmp_res = res_prev;
                res_prev = result;
                result = result*x + tmp_res;
                x2 = x1;
                x1 = rest;
                sign *= -1;
            }
            else
                break;
        }
        if(sign < 0)
            result = mod - result;
        return result;
    }

    // найбільший спільний дільник (бінарний алгоритм)
    verylong gcd(verylong a, verylong b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
    // найменше спільне кратне
    verylong lcm(verylong first, verylong second)
    {
        return first * second / gcd(first, second);
    }

    verylong redc_barret(verylong x, verylong n, verylong mu)
    {
        unsigned k = verylong::bit_length(n)/digit_size + 1;
        verylong q = x >> (k-1)*digit_size;
        q = q * mu;
        q = q >> (k+1)*digit_size;
        verylong r = x - q * n;
        while(r >= n)
            r = r - n;
        return r;
    }

    verylong redc_mont(verylong x, verylong n, verylong c = 0, verylong R = 0)
    {
        unsigned k = verylong::bit_length(n) / digit_size + 1;
        if(R == 0)
            R = base.pow(k);
        if(c == 0)
            c = (base - invert(n[0], base) % base);
        for(unsigned i {}; i < k; i++)
        {
            verylong t = (c*verylong(x[i]))%base;
            x = x + t * n * base.pow(i);
        }
        x = x / R;
        if(x >= n)
            x = x - n;
        return x;
    }

    verylong mont(verylong x, verylong n)
    {
        unsigned k = verylong::bit_length(n) / digit_size + 1;
        verylong R = base.pow(k);
        return (x * R) % n;
    }

    verylong addmod_barret(verylong first, verylong second, verylong module)
    {
        unsigned k = verylong::bit_length(module) / digit_size + 1;
        verylong mu = verylong(1).shift_digits_to_high(k*2) / module;
        return redc_barret((redc_barret(first, module, mu) + redc_barret(second, module, mu)), module, mu);
    }

    verylong submod_barret(verylong first, verylong second, verylong module)
    {
        unsigned k = verylong::bit_length(module) / digit_size + 1;
        verylong mu = verylong(1).shift_digits_to_high(k*2) / module;
        return redc_barret((redc_barret(first, module, mu) - redc_barret(second, module, mu)), module, mu);
    }

    verylong mulmod_barret(verylong first, verylong second, verylong module)
    {
        unsigned k = verylong::bit_length(module) / digit_size + 1;
        verylong mu = verylong(1).shift_digits_to_high(k*2) / module;
        return redc_barret((redc_barret(first, module, mu) * redc_barret(second, module, mu)), module, mu);
    }

    verylong powmod_barret(verylong number, verylong power, verylong module)
    {
        verylong result = 1;
        unsigned k = verylong::bit_length(module)/digit_size+1;
        verylong mu;
        mu[k*2] = 1;
        mu = mu / module;
        std::string p = power.to_bin_string();
        for(int i = p.length()-1; i >= 0; i--)
        {
            if(p[i] == '1')
                result = redc_barret(result * number, module, mu);
            number = redc_barret(number * number, module, mu);
        }
        return result;
    }

    verylong pow2mod_barret(verylong number, verylong module)
    {
        return powmod_barret(number, 2, module);
    }

    verylong addmod_mont(verylong first, verylong second, verylong module, verylong c = 0, verylong R = 0)
    {
        if(c == 0)
            c = (base - invert(module[0], base) % base);
        first = mont(first, module);
        second = mont(second, module);
        verylong result = first + second;
        return redc_mont(result, module, c, R);
    }

    verylong submod_mont(verylong first, verylong second, verylong module, verylong c = 0, verylong R = 0)
    {
        if(c == 0)
            c = (base - invert(module[0], base) % base);
        first = mont(first, module);
        second = mont(second, module);
        verylong result = first - second;
        return redc_mont(result, module, c, R);
    }

    verylong mulmod_mont(verylong first, verylong second, verylong module, verylong c = 0, verylong R = 0)
    {
        first = mont(first, module);
        second = mont(second, module);
        verylong result = first * second;
        return redc_mont(redc_mont(result, module, c, R), module, c, R);
    }
    verylong powmod_mont(verylong number, verylong power, verylong module, verylong c = 0, verylong R = 0)
    {
        number = mont(number, module);
        verylong result = mont(1, module);
        std::string power_str = power.to_bin_string();
        for(unsigned i{}; i < power_str.length(); i++)
        {
            result = redc_mont(result * result, module, c, R);
            if(power_str[i] == '1')
                result = redc_mont(result * number, module, c, R);
        }
        return redc_mont(result, module, c, R);
    }

    verylong pow2mod_mont(verylong number, verylong module, verylong c = 0, verylong R = 0)
    {
        return powmod_mont(number, 2, module, c, R);
    }
}
