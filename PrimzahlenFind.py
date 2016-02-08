# Autor: Alexander Herbrich
# Wann: 31.01.2016
# Thema: Listen von Primzahlen

def is_pz (n):
    k = 0 ; m = (n//2 ) + 1
    if ((n == 0) or (n == 1)):
        return False
    if n < 0:
        return False
    for k in range (2, m):
        if (n % k) == 0:
            return False
    return True

def find_pz (n):  
    PrimZ = [] ; m = n + 1
    for i in range (2, m):
        if is_pz (i):
            PrimZ += [i]
    return PrimZ
