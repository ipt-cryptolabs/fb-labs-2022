#include "cryptsystem.hpp"

user::user(string n) : name(n), keys(gen_keys())
{}
user::user(string n, key_pair k) : name(n), keys(k)
{}
verylong user::send_message(string recipient, verylong message)
{
    return encrypt(message, key_storage[recipient]);
}
verylong user::recv_message(verylong message)
{
    return decrypt(message, keys.pvt);
}
verylong user::sign(verylong message)
{
    return ::sign(message, keys.pvt);
}
verylong user::verify(string user, verylong signature)
{
    return ::verify(signature, key_storage[user]);
}
string user::get_name()
{
    return name;
}
public_key user::get_pubkey()
{
    return keys.pub;
}
void user::set_pubkey(string n, public_key pub)
{

    key_storage[n] = pub;
}
void exchange_keys(user& u1, user& u2)
{
    u1.set_pubkey(u2.get_name(), u2.get_pubkey());
    u2.set_pubkey(u1.get_name(), u1.get_pubkey());
}
