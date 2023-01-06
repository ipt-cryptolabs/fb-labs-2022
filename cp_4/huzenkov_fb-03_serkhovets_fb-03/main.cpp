#include <iostream>
#include <string>
#include <algorithm>
#include "rsa.hpp"
#include "cryptsystem.hpp"

using namespace std;
using namespace vl;

string hex_to_ascii(string hex)
{
    string result;
    for(unsigned i {}; i < hex.length(); i += 2)
        result += char(strtol(hex.substr(i, 2).c_str(), NULL, 16));
    return result;
}

int main()
{
    cout << "***** Generating Alice's keys pair *****\n";
    user Alice("Alice");
    cout << "******** Alice's keys generated ********\n\n";
    cout << "****** Generating Bob's keys pair ******\n";
    user Bob("Bob");
    cout << "********* Bob's keys generated *********\n\n";
    cout << "*********** Exchanging pairs ***********\n";
    exchange_keys(Alice, Bob);
    cout << "********* Exchanging completed *********\n\n";
    verylong message;
    verylong signature;
    message = gen_verylong(256/digit_size);
    cout << "[Message]: 0x" << message.to_hex_string() << endl;
    verylong cypher = Alice.send_message("Bob", message);
    cout << "[Alice -> Bob]: 0x" << cypher.to_hex_string() << endl;
    signature = Alice.sign(message);
    cout << "[Alice sign]: 0x" << signature.to_hex_string() << endl;
    cout << "[Bob decrypted]: " << Bob.recv_message(cypher).to_hex_string() << endl;
    cout << "[Message verified]: " << ((Bob.recv_message(cypher) == Bob.verify("Alice", signature)) ? "True" : "False") << endl;;
    message = gen_verylong(256/digit_size);
    cout << "[Message]: 0x" << message.to_hex_string() << endl;
    cypher = Bob.send_message("Alice", message);
    cout << "[Bob -> Alice]: 0x" << cypher.to_hex_string() << endl;
    signature = Bob.sign(message);
    cout << "[Bob sign]: 0x" << signature.to_hex_string() << endl;
    cout << "[Alice decrypted]: " << Alice.recv_message(cypher).to_hex_string() << endl;
    cout << "[Message verified]: " << ((Alice.recv_message(cypher) == Alice.verify("Bob", signature)) ? "True" : "False") << endl;
}
