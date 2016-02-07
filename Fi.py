# Autor: Alexander Herbrich
# Wann: 01.02.2016
# Thema: Fobonacci von einer Zahl errechnen

def fi(n):
        if n < 0:
                return "Negative Zahlen sind nicht erlaubt!!!"
        fi = (1 + 5 ** .5) / 2
        s = 0
        #print (fi)
        m1fi = 1 - fi
        p_fi = 1
        p_m1fi = 1
        for i in range (1, n + 1):
                p_fi = p_fi * fi
                #print (p_fi)
                p_m1fi = p_m1fi * m1fi
                #print (p_m1fi)
                ergebnis = (p_fi - p_m1fi) / 5 ** .5
        return ergebnis
