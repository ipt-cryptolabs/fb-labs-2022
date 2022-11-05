#include <cstring>
#include <iostream>
#include <iomanip>
#include <map>
#include <string>
#include <cmath>
#include <fstream>
#include <locale>

std::wstring read_text(std::string filename);
void filter_text(std::wstring& text);
void filter_text_spaces(std::wstring& text);
std::map<std::wstring, int> letter_frequency(const std::wstring text);
std::map<std::wstring, int> bigram_frequency(const std::wstring text);
std::map<std::wstring, int> bigram_frequency_nocross(const std::wstring text);
double entropy(std::map<std::wstring, int> ensamble);

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        std::cout << "Usage: " << argv[0] << "<file name>" << std::endl;
        return 1;
    }
    wchar_t* arg = new wchar_t[strlen(argv[1])];
    std::locale mylocale("ru_RU.UTF8");
    std::wcout.imbue(mylocale);
    std::string filename = "plaintext";
    std::wstring text = read_text(filename);
    std::wstring without_spaces = text;
    std::wstring with_spaces = text;
    filter_text(without_spaces);
    filter_text_spaces(with_spaces);
    std::wofstream nospaces;
    std::wofstream spaces;
    nospaces.open("without_spaces.txt", std::wios::trunc);
    spaces.open("with_spaces.txt", std::wios::trunc);
    nospaces.imbue(mylocale);
    spaces.imbue(mylocale);
    nospaces << without_spaces;
    spaces << with_spaces;
    nospaces.close();
    spaces.close();
    std::map<std::wstring, int> letters = letter_frequency(without_spaces);
    std::map<std::wstring, int> letters_spaces = letter_frequency(with_spaces);
    std::map<std::wstring, int> bigrams_cross = bigram_frequency(without_spaces);
    std::map<std::wstring, int> bigrams_nocross = bigram_frequency_nocross(without_spaces);
    std::map<std::wstring, int> bigrams_cross_spaces = bigram_frequency(with_spaces);
    std::map<std::wstring, int> bigrams_nocross_spaces = bigram_frequency_nocross(with_spaces);
    double h11 = entropy(letters);
    double h12 = entropy(letters_spaces);
    double h21 = entropy(bigrams_cross);
    double h22 = entropy(bigrams_nocross);
    double h23 = entropy(bigrams_cross_spaces);
    double h24 = entropy(bigrams_nocross_spaces);
    std::wofstream out;
    out.open("programs_out.txt");
    out.imbue(mylocale);
    out << L"Ентропія монограм без пробілів: " << h11 << '\n'
        << L"Надлишковість для тексту без пробілів: " << 1 - h11/log2(32) << '\n'
        << L"Ентропія монограм з пробілами: " << h12 << '\n'
        << L"Надлишковість для тексту з пробілами: " << 1 - h12/log2(32) << '\n'
        << L"Ентропія біграм без пробілів та з перетинами: " << h21 / 2 << '\n'
        << L"Надлишковість для джерела біграм без пробілів та з перетинами: " << 1 - h21/log2(32*32) << '\n'
        << L"Ентропія біграм без пробілів та без перетинів: " << h22 / 2 << '\n'
        << L"Надлишковість для джерела біграм без пробілів та без перетинів: " << 1 - h22/log2(32*32) << '\n'
        << L"Ентропія біграм з пробілами та перетинами: " << h23 / 2 << '\n'
        << L"Надлишковість для джерела біграм з пробілами та перетинами: " << 1 - h23/log2(32*32) << '\n'
        << L"Ентропія біграм з пробілами та без перетинів: " << h24 / 2 << '\n'
        << L"Надлишковість для джерела біграм з пробілами та без перетинів: " << 1 - h24/log2(32*32) << '\n';
    out << std::endl;

    unsigned sum_letters_nospaces{};
    unsigned sum_letters_spaces{};
    unsigned sum_bigrams_nospaces_cross{};
    unsigned sum_bigrams_nospaces_nocross{};
    unsigned sum_bigrams_spaces_cross{};
    unsigned sum_bigrams_spaces_nocross{};
    
    for(auto const& x : letters)
        sum_letters_nospaces += x.second;
    for(auto const& x : letters_spaces)
        sum_letters_spaces += x.second;
    for(auto const& x : bigrams_cross)
        sum_bigrams_nospaces_cross += x.second;
    for(auto const& x : bigrams_nocross)
        sum_bigrams_nospaces_nocross += x.second;
    for(auto const& x : bigrams_cross_spaces)
        sum_bigrams_spaces_cross += x.second;
    for(auto const& x : bigrams_nocross_spaces)
        sum_bigrams_spaces_nocross += x.second;
    
    std::wofstream table11;
    std::wofstream table12;
    std::wofstream table21;
    std::wofstream table22;
    std::wofstream table23;
    std::wofstream table24;
    
    table11.open("table_letters_nospaces.csv", std::wios::trunc);
    table12.open("table_letters_spaces.csv", std::wios::trunc);
    table21.open("table_bigrams_nospaces_cross.csv", std::wios::trunc);
    table22.open("table_bigrams_nospaces_nocross.csv", std::wios::trunc);
    table23.open("table_bigrams_spaces_cross.csv", std::wios::trunc);
    table24.open("table_bigrams_spaces_nocross.csv", std::wios::trunc);
    
    table11.imbue(mylocale);
    table12.imbue(mylocale);
    table21.imbue(mylocale);
    table22.imbue(mylocale);
    table23.imbue(mylocale);
    table24.imbue(mylocale);
    
    table11 << L"Биграмма" << L";" << L"Частота" << L";"
            << L"Вероятность" << L";" << std::endl;
    table12 << L"Биграмма" << L";" << L"Частота" << L";"
            << L"Вероятность" << L";" << std::endl;
    table21 << L"Биграмма" << L";" << L"Частота" << L";"
            << L"Вероятность" << L";" << std::endl;
    table22 << L"Биграмма" << L";" << L"Частота" << L";"
            << L"Вероятность" << L";" << std::endl;
    table23 << L"Биграмма" << L";" << L"Частота" << L";"
            << L"Вероятность" << L";" << std::endl;
    table24 << L"Биграмма" << L";" << L"Частота" << L";"
            << L"Вероятность" << L";" << std::endl;
    
    for(auto const& x : letters)
        table11 << x.first << L";"
                << x.second << L";"
                << float(x.second) / sum_letters_nospaces << L";"
                << std::endl;
    for(auto const& x : letters_spaces)
        table12 << x.first << L";"
                << x.second << L";"
                << float(x.second) / sum_letters_spaces << L";"
                << std::endl;
    for(auto const& x : bigrams_cross)
        table21 << x.first << L";"
                << x.second << L";"
                << float(x.second) / sum_bigrams_nospaces_cross << L";"
                << std::endl;
    for(auto const& x : bigrams_nocross)
        table22 << x.first << L";"
                << x.second << L";"
                << float(x.second) / sum_bigrams_nospaces_nocross << L";"
                << std::endl;
    for(auto const& x : bigrams_cross_spaces)
        table23 << x.first << L";"
                << x.second << L";"
                << float(x.second) / sum_bigrams_spaces_cross << L";"
                << std::endl;
    for(auto const& x : bigrams_nocross_spaces)
        table24 << x.first << L";"
                << x.second << L";"
                << float(x.second) / sum_bigrams_spaces_nocross << L";"
                << std::endl;
    
    table11.close();
    table12.close();
    table21.close();
    table22.close();
    table23.close();
    table24.close();
}

std::wstring read_text(std::string filename)
{
    std::wifstream input;
    std::locale mylocale("ru_RU.UTF8");   // get global locale
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

void filter_text(std::wstring& text)
{
    std::locale mylocale("ru_RU.UTF8");
    std::locale enlocale("en_US.UTF8");
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

void filter_text_spaces(std::wstring& text)
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

std::map<std::wstring, int> letter_frequency(const std::wstring text)
{
    std::map<std::wstring, int> freq_map;
    for (unsigned i{}; i < text.length(); i++)
    {
        freq_map[text.substr(i, 1)]++;
    }
    return freq_map;
}

std::map<std::wstring, int> bigram_frequency(const std::wstring text)
{
    std::map<std::wstring, int> freq_map;
    short unsigned last_bg_size;
    last_bg_size = (text.length() % 2 != 0) ? 1 : 0;
    for (unsigned i{}; i < text.length() - last_bg_size; i += 2)
    {
        freq_map[text.substr(i, 2)]++;
    }
    if (last_bg_size == 1)
    {
        std::wstring last_bigram = text.substr(text.length() - 1, 1) + std::wstring(L" ");
        freq_map[last_bigram]++;
    }
    return freq_map;
}

std::map<std::wstring, int> bigram_frequency_nocross(const std::wstring text)
{
    std::wstring temp = text;
    std::map<std::wstring, int> freq_map;
    for (unsigned i{}; i < temp.length(); i += 2)
    {
        bool is_crossed = false;
        do
        {
            std::wstring sub = temp.substr(i, 2);
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

double entropy(std::map<std::wstring, int> ensamble)
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
