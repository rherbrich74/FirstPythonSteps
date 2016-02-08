# Autor: Alexander Herbrich
# Wann: 01.02.2016
# Thema: Fakultaet von einer Zahl errechnen

def fak(n):
    k = 1
    for i in range(1,n + 1):
        k = i * k
    return k
