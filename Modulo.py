# Autor: Alexander Herbrich
# Wann: 30.01.2016
# Thema: Kennenlernen des Ermittelns von teilbare Zahlen

def modulo(n , K):
    i = int (n / K)
    i = n - i * K
    if i == 0:
        return (True,i)
    else:
        return (False,i)

