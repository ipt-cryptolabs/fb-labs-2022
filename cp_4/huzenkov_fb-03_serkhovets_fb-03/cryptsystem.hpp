#ifndef CRYPTSYSTEM_HPP
#define CRYPTSYSTEM_HPP

#include <string>
#include <map>
#include "rsa.hpp"

using namespace std;
using namespace vl;

class user
{
protected:
    string name;
    key_pair keys;
    map<string, public_key> key_storage;
public:
    user(string n);
    user(string n, key_pair k);
    verylong send_message(string recipient, verylong message);
    verylong recv_message(verylong message);
    verylong sign(verylong message);
    verylong verify(string user, verylong signature);
    string get_name();
    public_key get_pubkey();
    void set_pubkey(string n, public_key pub);
    friend void exchange_keys(user&, user&);
};

void exchange_keys(user&, user&);

#endif // CRYPTSYSTEM_HPP
