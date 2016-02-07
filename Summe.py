# Autor: Alexander Herbrich
# Wann: 30.01.2016
# Thema: Errechnen von Summen nach Gauss

def summe(n):
    s = 0
    while n > 0:
        s = s + n
        n = n - 1
    return s

def g_summe(n):
    s = 0
    while n > 0:
        if (n % 2) == 0:
            s = s + n
        n = n - 1
    return s

def ug_summe(n):
    s = 0
    while n > 0:
        if (n % 2) != 0:
            s = s + n
        n = n - 1
    return s

def x_summe(n):
    sg = 0 ; su = 0
    while n > 0:
        if (n % 2) == 0:
            sg = sg + n
            n = n - 1
        else:
            su = su + n
            n = n -1
    return(sg,su)
