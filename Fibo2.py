# Autor: Alexander Herbrich
# Wann: 01.02.2016
# Thema: Fobonacci von einer Zahl errechnen

def fibo2(n):
    if n < 0:
        return "Negative Zahlen sind nicht erlaubt!!!"
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    a = 0
    b = 1
    for i in range (2, n + 1):
        s = a + b
        a = b
        b = s
    return b
    
