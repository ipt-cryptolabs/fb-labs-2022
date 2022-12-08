#include "encryption.hpp"

wchar_t alphabet[] = L"абвгдежзийклмнопрстуфхцчшщьыэюя";
map<wchar_t, int> alphacodes = {pair<wchar_t, int>(L'а', 0),
                                      pair<wchar_t, int>(L'б', 1),
                                      pair<wchar_t, int>(L'в', 2),
                                      pair<wchar_t, int>(L'г', 3),
                                      pair<wchar_t, int>(L'д', 4),
                                      pair<wchar_t, int>(L'е', 5),
                                      pair<wchar_t, int>(L'ж', 6),
                                      pair<wchar_t, int>(L'з', 7),
                                      pair<wchar_t, int>(L'и', 8),
                                      pair<wchar_t, int>(L'й', 9),
                                      pair<wchar_t, int>(L'к', 10),
                                      pair<wchar_t, int>(L'л', 11),
                                      pair<wchar_t, int>(L'м', 12),
                                      pair<wchar_t, int>(L'н', 13),
                                      pair<wchar_t, int>(L'о', 14),
                                      pair<wchar_t, int>(L'п', 15),
                                      pair<wchar_t, int>(L'р', 16),
                                      pair<wchar_t, int>(L'с', 17),
                                      pair<wchar_t, int>(L'т', 18),
                                      pair<wchar_t, int>(L'у', 19),
                                      pair<wchar_t, int>(L'ф', 20),
                                      pair<wchar_t, int>(L'х', 21),
                                      pair<wchar_t, int>(L'ц', 22),
                                      pair<wchar_t, int>(L'ч', 23),
                                      pair<wchar_t, int>(L'ш', 24),
                                      pair<wchar_t, int>(L'щ', 25),
                                      pair<wchar_t, int>(L'ь', 26),
                                      pair<wchar_t, int>(L'ы', 27),
                                      pair<wchar_t, int>(L'э', 28),
                                      pair<wchar_t, int>(L'ю', 29),
                                      pair<wchar_t, int>(L'я', 30)};

int bigram_to_int(wstring bigram, int mod)
{
    return (alphacodes[bigram[0]]) * mod + alphacodes[bigram[1]];
}

wstring int_to_bigram(int bigram, int mod)
{
    wstring ret;
    ret += alphabet[bigram / mod];
    ret += alphabet[bigram % mod];
    return ret;
}

void encrypt(wstring& text, pair<int, int> key, int mod)
{
    for (unsigned i{}; i < text.length(); i += 2)
    {
        int x = (alphacodes[text[i]]) * mod + alphacodes[text[i+1]];
        int y = (x * key.first + key.second) % (mod*mod);
        text[i] = alphabet[y / mod];
        text[i+1] = alphabet[y % mod];
    }
}



void decrypt(wstring& text, pair<int, int> key, int mod)
{
    int a_inv = invert(key.first, mod*mod);
    for (unsigned i{}; i < text.length(); i += 2)
    {
        int y = (alphacodes[text[i]]) * mod + alphacodes[text[i+1]];
        int x = (a_inv * (mod*mod + y - key.second)) % (mod*mod);
        text[i] = alphabet[x / mod];
        text[i+1] = alphabet[x % mod];
    }
}

wstring read_text(const std::string& filename)
{
//    std::wifstream input;
//    std::locale mylocale("ru_RU.UTF8");   // get global locale
//    input.imbue(mylocale);
//    input.open(filename, std::wios::in);
//    if(!input)
//        throw "Неможливо відкрити потік";
//    wstring text;
//    while(input)
//    {
//        wstring str;
//        input >> str;
//        text += str + L" ";
//    }
//    input.close();
//    return text;

    std::wifstream input;
    std::locale mylocale("ru_RU.UTF-8");   // get global locale
    input.imbue(mylocale);
    input.open(filename, std::wios::in);
    if(!input)
        std::wcout << L"Huston, we've got a problem!" << std::endl;
    std::wstring text;
    while(input)
    {
        std::wstring str;
        input >> str;
        text += str + L" ";
    }
    input.close();
    return text;
}

vector<int> solve_equation(int x, int y, int mod)
{
    vector<int> results;
    if(invert(x, mod) == 0)
    {
        for(int i {}; i < mod; i++)
            if(y == (i * x) % mod)
                results.push_back(i);
    }
    else
        results.push_back((y * invert(x, mod)) % mod);
    return results;
}

vector<pair<int, int>> find_possible_keys(const int x1, const int x2,
                                          const int y1, const int y2,
                                          int mod)
{
    int sqmod = mod*mod;
    vector<pair<int, int>> result;
    int x = (sqmod + x1 - x2) % sqmod;
    int y = (sqmod + y1 - y2) % sqmod;
    vector<int> as = solve_equation(x, y, sqmod);
    for(int a : as)
    {
        int b = (sqmod + (y1 - a * x1) % (sqmod)) % sqmod;
        result.push_back(pair<int, int>(a, b));
    }
    return result;
}

wstring most_frequent(const map<wstring, int>& bigrams)
{
    wstring most;
    int frequency = 0;
    for(auto& bigram : bigrams)
    {
        if((bigram.second) > frequency || (most == wstring(L"")))
        {
            frequency = bigram.second;
            most = bigram.first;
        }
    }
    return most;
}

bool is_text(wstring text)
{
    vector<wstring> wrongs = {L"ьь", L"ыь", L"аь", L"оь", L"уь", L"яь", L"юь", L"эь", L"ыы", L"оы", L"уы", L"еы", L"еь", L"эы", L"ыь", L"ьы",
                              L"жы", L"шы", L"щы", L"чы", L"юы", L"яы", L"аы", L"йь", L"йы", L"фй", L"мй", L"жй", L"пй", L"ьй"};

    for(unsigned long i{}; i < text.length(); i++)
    {
        if(find(wrongs.begin(), wrongs.end(), text.substr(i, 2)) != wrongs.end())
        {
            return false;
        }
    }
    if(text.substr(0, 10) == wstring(L"аааааааааа"))
        return false;
    return true;
}

vector<wstring> get5(map<wstring, int> bigrams)
{
    vector<wstring> ret;
    for(int i{}; i < 5; i++)
    {
        ret.push_back(most_frequent(bigrams));
        bigrams.erase(ret.back());
    }
    return ret;
}

vector<pair<pair<int, int>, pair<int, int>>> get_bigrams_pairs(vector<wstring> xarray, vector<wstring> yarray, int mod)
{
    vector<pair<int, int>> xypairs;
    vector<pair<pair<int, int>, pair<int, int>>> pairs;
    for(auto& x : xarray)
        for(auto& y : yarray)
            xypairs.push_back(pair<int, int>(bigram_to_int(x, mod), bigram_to_int(y, mod)));
    for(auto& xypair1 : xypairs)
        for(auto& xypair2 : xypairs)
            pairs.push_back(make_pair(xypair1, xypair2));
    return pairs;
}

pair<int, int> find_key(const wstring& cypher_text, int mod, double plain_entropy)
{
    vector<wstring> cypher_bigrams = get5(bigram_frequency(cypher_text));
    vector<wstring> plain_bigrams;

    plain_bigrams.push_back(L"ст");
    plain_bigrams.push_back(L"но");
    plain_bigrams.push_back(L"то");
    plain_bigrams.push_back(L"на");
    plain_bigrams.push_back(L"ен");

    vector<pair<pair<int, int>, pair<int, int>>> pairs = get_bigrams_pairs(plain_bigrams, cypher_bigrams, mod);
    for(auto& p : pairs)
    {
        int x1 = p.first.first;
        int x2 = p.second.first;
        int y1 = p.first.second;
        int y2 = p.second.second;
        vector<pair<int, int>> possible_keys = find_possible_keys(x1, x2, y1, y2, mod);
        vector<double> entropies;
        for(auto& key : possible_keys)
        {
            wstring plain = cypher_text;
            decrypt(plain, key, mod);
            if(is_text(plain))
            {
                return key;
            }
        }
    }
    return pair<int, int>(0, 0);
}

void filter_text(wstring& text)
{
    std::locale mylocale("ru_RU.UTF8");
    for (unsigned i{}; i < text.length(); i++)
    {
        if (!std::isalpha(text[i], mylocale))
        {
            text.erase(i, 1);
            if(i != 0) i--;
        }
        else if(std::isalpha(text[i], mylocale))
        {
            text[i] = std::tolower(text[i], mylocale);
            if(text[i] >= L'a' && text[i] <= L'z')
            {
                text.erase(i, 1);
                if(i != 0) i--;
            }
        }
    }
}

void filter_text_spaces(wstring& text)
{
    std::locale mylocale("ru_RU.UTF8");
    std::locale enlocale("en_US.UTF8");
    for (unsigned i{}; i < text.length(); i++)
    {
        if (!std::isalpha(text[i], mylocale) && text[i] != L' ')
        {
            text.erase(i, 1);
            if(i != 0) i--;
        }
        else if (text[i] == '\n')
            text[i] = ' ';
        else if(std::isalpha(text[i], mylocale))
        {
            text[i] = std::tolower(text[i], mylocale);
            if(text[i] >= L'a' && text[i] <= L'z')
            {
                text.erase(i, 1);
                if(i != 0) i--;
            }
        }
        if(text[i] == ' ')
        {
            if(i != 0 && text[i-1] == ' ')
            {
                text.erase(i-1, 1);
                if(i != 0) i--;
            }
        }
    }
}

map<wstring, int> letter_frequency(const wstring& text)
{
    map<wstring, int> freq_map;
    for (unsigned i{}; i < text.length(); i++)
    {
        freq_map[text.substr(i, 1)]++;
    }
    return freq_map;
}

map<wstring, int> bigram_frequency(const wstring& text)
{
    map<wstring, int> freq_map;
    short unsigned last_bg_size;
    last_bg_size = (text.length() % 2 != 0) ? 1 : 0;
    for (unsigned i{}; i < text.length() - last_bg_size; i += 2)
    {
        freq_map[text.substr(i, 2)]++;
    }
    if (last_bg_size == 1)
    {
        wstring last_bigram = text.substr(text.length() - 1, 1) + wstring(L" ");
        freq_map[last_bigram]++;
    }
    return freq_map;
}

map<wstring, int> bigram_frequency_nocross(const wstring text)
{
    wstring temp = text;
    map<wstring, int> freq_map;
    for (unsigned i{}; i < temp.length(); i += 2)
    {
        bool is_crossed = false;
        do
        {
            wstring sub = temp.substr(i, 2);
            if(sub[0] == sub[1])
            {
                is_crossed = true;
                temp.erase(i+1, 1);
            }
            else
            {
                freq_map[temp.substr(i, 2)]++;
                is_crossed = false;
            }
        }while(is_crossed);
    }
    return freq_map;
}

double entropy(map<wstring, int> ensamble)
{
    unsigned sum = 0;
    for (auto const& x : ensamble)
        sum += x.second;
    double h = 0;
    for (auto const& x : ensamble)
    {
        h += double(x.second) / double(sum) * log2(double(x.second) / double(sum));
    }
    return -h;
}

int gcdex(int a, int b, int& x, int& y)
{
    if (b == 0)
    {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d1 = gcdex(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return d1;
}

int invert(int a, int module)
{
    int x, y, d;
    d = gcdex(a, module, x, y);
    if (d != 1)
        return 0;
    return (x < 0) ? module + x : x;
}
