# Autor: Alexander Herbrich
# Wann: 30.01.2016
# Thema: Verschieben von Buchstaben

def wort (name,K):
    Wort1 = ''
    for i in range (len(name)):
        n = i + K
        if n >= len(name):
            n -= len(name)
        Wort1 += name[n]
    return (Wort1)

