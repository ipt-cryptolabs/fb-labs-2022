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
std::map<std::wstring, int> letter_frequency(const std::wstring text);
std::map<std::wstring, int> bigram_frequency(const std::wstring text);
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
    filter_text(text);
    std::wofstream filtered;
    filtered.open("filtered", std::wios::trunc);
    filtered.imbue(mylocale);
    filtered << text;
    filtered.close();
    std::map<std::wstring, int> letters = letter_frequency(text);
    std::map<std::wstring, int> bigrams = bigram_frequency(text);
    double h1 = entropy(letters);
    double h2 = entropy(bigrams);
    std::wcout << "H1: " << h1 << '\n'
              << "H2: " << h2 << std::endl;
    std::wcout << std::endl;

    unsigned suml{};
    unsigned sumb{};
    
    for(auto const& x : letters)
        suml += x.second;
    for(auto const& x : bigrams)
        sumb += x.second;
    
    std::wofstream tablel;
    tablel.open("table_letters.csv", std::wios::trunc);
    tablel.imbue(mylocale);
    tablel << L"Биграмма" << L";" << L"Частота" << L";"
           << L"Вероятность" << L";" << std::endl;
    for(auto const& x : letters)
    {
        tablel << x.first << L";"
               << x.second << L";"
               << float(x.second) / suml << L";"
               << std::endl;
    }
    std::wofstream tableb;
    tableb.open("table_bigrams.csv", std::wios::trunc);
    tableb.imbue(mylocale);
    tableb << L"Биграмма" << L";" << L"Частота" << L";"
           << L"Вероятность" << L";" << std::endl;
    for(auto const& x : bigrams)
    {
        tableb << x.first << L";"
               << x.second << L";"
               << float(x.second) / sumb << L";"
               << std::endl;
    }
    tablel.close();
    tableb.close();
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
