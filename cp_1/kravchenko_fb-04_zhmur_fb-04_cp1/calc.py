from math import log2


def calc_R(ent):
    return 1 - ent / log2(32)

print(calc_R((1.9370+2.5362)/2))