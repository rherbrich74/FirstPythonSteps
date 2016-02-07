# Autor: Alexander Herbrich
# Wann: 01.02.2016
# Thema: Fakultaet von einer Zahl errechnen

def fak2(n):
        if n < 0:
                return "Negative Zahlen sind nicht erlaubt!!!"
        if (n == 1) or (n == 0):
                return 1
        return fak2(n - 1) * n

