#ifndef VERYLONG_HPP
#define VERYLONG_HPP
#include <string>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <bits/stdc++.h>

namespace vl
{
    using verylong_digit = unsigned;
    const unsigned num_digits = 2048 / (sizeof(unsigned) * 8);
    const unsigned digit_size = sizeof(verylong_digit) * 8;
    
    struct verylong_result;

    class verylong
    {
    private:
        verylong_digit number[num_digits]{};

        verylong_result long_mul_digit(verylong_digit digit);
        static short int cmp(verylong first, verylong second)
        {
            int i = num_digits-1;
            while(i >= 0 && first[i] == second[i])
                i = i-1;
            if(i == -1)
                return 0;
            else if(first[i] > second[i])
                return 1;
            else
                return -1;
        }
        
    public:
        verylong() : number{}
        {}
        verylong(verylong& longnum) : number{}
        {
            for(unsigned i = 0; i < num_digits; i++)
                number[i] = longnum[i];
        }
        verylong(verylong_result longnum);
        // Конструктори для приведення стандартних типів до великого числа
        verylong(unsigned num) : number{}
        {
            number[0] = num;
        }
        
        verylong(int num) : number{}
        {
            number[0] = num;
        }
        
        verylong(long num) : number{}
        {
            number[0] = num;
        }
        
        verylong(float num) : number{}
        {
            number[0] = num;
        }
        static unsigned bit_length(verylong num)
        {
            unsigned len = num_digits*digit_size;
            for(int i = num_digits-1; i >= 0; i--)
            {
                if(num[i] == 0)
                    len -= digit_size;
                else
                {
                    len -= digit_size;
                    while(num[i])
                    {
                        num[i] >>= 1;
                        len++;
                    }
                    break;
                }
            }
            return len;
        }
        verylong shift_digits_to_high(unsigned shift);
        verylong shift_bits_to_high(unsigned shift);
        verylong shift_bits_to_low(unsigned shift);
        verylong pow(unsigned pow);
        std::string to_bin_string() const;
        std::string to_hex_string() const;
        
        verylong operator=(std::string);
        verylong operator=(verylong num);
        verylong operator=(verylong_result num);
        verylong_digit& operator[](unsigned index);
        friend verylong_result operator+(verylong, verylong);
        friend verylong_result operator-(verylong, verylong);
        friend verylong_result operator*(verylong, verylong);
        friend verylong_result operator/(verylong, verylong);
        friend verylong_result operator%(verylong, verylong);
        friend verylong operator<<(verylong, unsigned);
        friend verylong operator>>(verylong, unsigned);
        friend verylong operator&(verylong, verylong);
        friend verylong operator|(verylong, verylong);
        friend bool operator<(verylong, verylong);
        friend bool operator>(verylong, verylong);
        friend bool operator<=(verylong, verylong);
        friend bool operator>=(verylong, verylong);
        friend bool operator==(verylong, verylong);
        friend bool operator!=(verylong, verylong);
    };
    
    struct verylong_result
    {
        verylong res;
        verylong_digit carry;
        verylong_digit borrow;
        verylong rest;
    };
}
#endif
