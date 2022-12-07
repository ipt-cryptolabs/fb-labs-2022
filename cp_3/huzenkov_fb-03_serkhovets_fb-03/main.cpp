#include "encryption.hpp"

using namespace std;

int main()
{
    locale mylocale("ru_RU.UTF-8");
    wcout.imbue(mylocale);

    wstring entr_text = read_text(string("/home/kaseki/crypt/text.txt"));
    wstring cipher_text = read_text("/home/kaseki/crypt/08.txt");
    filter_text(cipher_text);
    double plain_entropy = entropy(letter_frequency(entr_text));
    pair<int, int> found_key = find_key(cipher_text, 31, plain_entropy);
    wcout << "Found key is " << found_key.first << " " << found_key.second << endl;
    decrypt(cipher_text, found_key, 31);
    wfstream plain;
    plain.imbue(mylocale);
    plain.open("/home/kaseki/crypt/decrypted.txt", wios::out);
    plain << cipher_text << endl;
    plain.close();
    wcout << cipher_text << endl;
}
