#include "verylong.hpp"
using namespace vl;

namespace vl
{
    verylong::verylong(verylong_result longnum)
    {
        for(unsigned i = 0; i < num_digits; i++)
            number[i] = longnum.res[i];
    }
    verylong_result verylong::long_mul_digit(verylong_digit digit)
    {
        verylong_digit carry = 0;
        verylong result;
        for(unsigned i = 0; i < num_digits/2; i++)
        {
            unsigned long long temp = static_cast<unsigned long long>(number[i]) * digit + carry;
            result[i] = temp & ((1ull << digit_size)-1);
            carry = temp >> digit_size;
        }
        result[num_digits/2] = carry;
        return verylong_result {result, carry, 0, 0};
    }
    
    verylong verylong::pow(unsigned pow)
        {
            verylong result = 1;
            verylong num = *this;
            while(pow)
            {
                if((pow & 1) == 1)
                    result = result * num;
                num = num * num;
                pow >>= 1;
            }
            return result;
        }

    verylong verylong::shift_digits_to_high(unsigned shift)
    {
        for(unsigned j = 0; j < shift; j++)
        {
            for(unsigned i = num_digits-1; i > 0; i--)
            {
                number[i] = number[i-1];
            }
            number[0] = 0;
        }
        return *this;
    }
    
    verylong verylong::shift_bits_to_high(unsigned shift)
    {
        verylong num = *this;
        for(unsigned j = 0; j < shift; j++)
        {
            for(unsigned i = num_digits-1; i > 0; i--)
            {
                unsigned hdigit = num[i-1] >> (digit_size-1);
                num[i] <<= 1;
                num[i] += hdigit;
            }
            num[0] <<= 1;
        }
        return num;
    }
    
    verylong verylong::shift_bits_to_low(unsigned shift)
    {
        verylong num = *this;
        for(unsigned j = 0; j < shift; j++)
        {
            for(unsigned i = 0; i < num_digits-1; i++)
            {
                unsigned ldigit = num[i+1] << (digit_size-1);
                num[i] >>= 1;
                num[i] += ldigit;
            }
        }
        return num;
    }
    
    verylong_digit& verylong::operator[](unsigned index)
    {
       
        return number[index];
    }
    
    std::string verylong::to_bin_string() const
    {
        verylong_digit temp;
        std::stringstream stream;
        for(unsigned i = 0; i < num_digits; i++)
        {
            temp = number[i];
            for(unsigned j = 0; j < digit_size; j++)
            {
                stream << (temp & 1);
                temp >>= 1;
            }
        }
        
        std::string result( stream.str() );
        while(result[result.length()-1] == '0' && result.length() != 1)
            result.pop_back();
        std::reverse(result.begin(), result.end());
        
        return result;
    }
    std::string verylong::to_hex_string() const
    {
        verylong_digit temp;
        std::stringstream stream;
        for(unsigned i = 0; i < num_digits; i++)
        {
            temp = number[i];
            for(unsigned j = 0; j < digit_size; j += 4)
            {
                stream << std::hex << temp%16;
                temp /= 16;
            }
        }
        
        std::string result( stream.str() );
        while(result[result.length()-1] == '0' && result.length() != 1)
            result.pop_back();
        std::reverse(result.begin(), result.end());
        
        return result;
    }
    
    verylong verylong::operator=(std::string num)
    {
        *this = verylong(0);
        while(num.length() > 0)
        {
            *this = this->shift_bits_to_high(4);
            *this = *this + verylong(strtol(num.substr(0,1).c_str(), NULL, 16));
            num.erase(0,1);
        }
        return *this;
    }
    
    verylong verylong::operator=(verylong num)
    {
        for(unsigned i = 0; i < num_digits; i++)
            number[i] = num[i];
        return *this;
    }
    
    verylong verylong::operator=(verylong_result num)
    {
        for(unsigned i = 0; i < num_digits; i++)
            number[i] = num.res[i];
        return *this;
    }
    
    verylong_result operator+(verylong first, verylong second)
    {
        verylong_digit carry = 0;
        verylong result;
        for (unsigned i = 0; i < num_digits; i++)
        {
            unsigned long long temp = static_cast<const unsigned long long>(first[i]) + second[i] + carry;
            result[i] = temp & ((1ll << digit_size)-1);
            carry = temp >> digit_size;
        }
        return verylong_result {result, carry, 0, 0};
    }
    
    verylong_result operator-(verylong first, verylong second)
    {
        verylong_digit borrow = 0;
        verylong result;
        for(unsigned i = 0; i < num_digits; i++)
        {
            long long temp = static_cast<long long>(first[i]) - second[i] - borrow;
            if(temp >= 0)
            {
                result[i] = temp;
                borrow = 0;
            }
            else
            {
                result[i] = (1ull << digit_size) + temp;
                borrow = 1;
            }
        }
        return verylong_result {result, 0, borrow, 0};
    }
    verylong_result operator*(verylong first, verylong second)
    {
        verylong result;
        for(unsigned i = 0; i < num_digits/2; i++)
        {
            verylong_result temp = first.long_mul_digit(second[i]);
            temp.res.shift_digits_to_high(i);
            result = (result + temp.res);
        }
        return verylong_result {result, 0, 0, 0};
    }
    verylong_result operator/(verylong first, verylong second)
    {
        unsigned k = verylong::bit_length(second);
        verylong rest = first;
        verylong result = 0;
        while(verylong::cmp(rest, second) != -1)
        {
            unsigned t = verylong::bit_length(rest);
            verylong C = second.shift_bits_to_high(t-k);
            if(verylong::cmp(rest, C) == -1)
            {
                t = t - 1; // тоді повертаємось на біт назад
                C = second.shift_bits_to_high(t-k);
            }
            rest = rest - C;
            result = result + verylong(2).pow(t - k);
        }
        return verylong_result {result, 0, 0, rest};
    }
    verylong_result operator%(verylong number, verylong module)
    {
        verylong_result mod = number/module;
        return verylong_result {mod.rest, 0, 0, 0};
    }
    verylong operator<<(verylong num, unsigned shift)
    {
        return num.shift_bits_to_high(shift);
    }
    verylong operator>>(verylong num, unsigned shift)
    {
        return num.shift_bits_to_low(shift);
    }
    verylong operator&(verylong first, verylong second)
    {
        verylong ret;
        for(unsigned i = 0; i < num_digits-1; i++)
        {
            ret[i] = first[i] & second[i];
        }
        return ret;
    }
    verylong operator|(verylong first, verylong second)
    {
        verylong ret;
        for(unsigned i = 0; i < num_digits-1; i++)
        {
            ret[i] = first[i] | second[i];
        }
        return ret;
    }
    bool operator<(verylong first, verylong second)
    {
        return (verylong::cmp(first, second) == -1);
    }
    bool operator>(verylong first, verylong second)
    {
        return (verylong::cmp(first, second) == 1);
    }
    bool operator<=(verylong first, verylong second)
    {
        short res = verylong::cmp(first, second);
        return (res == -1 || res == 0);
    }
    bool operator>=(verylong first, verylong second)
    {
        short res = verylong::cmp(first, second);
        return (res == 1 || res == 0);
    }
    bool operator==(verylong first, verylong second)
    {
        return (verylong::cmp(first, second) == 0);
    }
    bool operator!=(verylong first, verylong second)
    {
        return (verylong::cmp(first, second) != 0);
    }
}
