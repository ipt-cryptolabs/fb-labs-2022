#ifndef ENCRYPTION_HPP
#define ENCRYPTION_HPP

#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <locale>
#include <algorithm>

using std::map;
using std::wstring;
using std::pair;
using std::vector;
using std::min;
using std::find;

extern wchar_t alphabet[];
extern map<wchar_t, int> alphacodes;

int bigram_to_int(wstring, int);
void encrypt(wstring& text, pair<int, int> key, int alphabet_size);
void decrypt(wstring& text, pair<int, int> key, int alphabet_size);
vector<int> solve_equation(int, int, int);
wstring most_frequent(const map<wstring, int>&);
vector<pair<int, int>> find_possible_keys(const int, const int,
                                          const int, const int,
                                          int);
pair<int, int> find_key(const wstring&, int, double);
wstring read_text(const std::string&);
void filter_text(wstring&);
void filter_text_spaces(wstring&);
map<wstring, int> letter_frequency(const wstring&);
map<wstring, int> bigram_frequency(const wstring&);
map<wstring, int> bigram_frequency_nocross(const wstring text);
double entropy(map<wstring, int> ensamble);
int gcdex(int, int, int&, int&);
int invert(int, int);

#endif
