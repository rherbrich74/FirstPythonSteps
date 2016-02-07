# Autor: Alexander Herbrich
# Wann: 01.02.2016
# Thema: Fibonacci von Zahlen errechnen

def fibo(n):
        if n < 0:
                return "Negative Zahlen sind nicht erlaubt!!!"
        if (n == 1):
                return 1
        if (n == 0):
                return 0
        return fibo(n - 1) + fibo(n - 2)
