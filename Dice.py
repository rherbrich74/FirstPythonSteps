# Autor: Alexander Herbrich
# Wann: 30.01.2016
# Thema: Wuerfel, Nutzung von Random

from random import randrange

def dice():
    a = randrange(1,7)
    if a == 1:
        print ("1")
    if a == 2:
        print ("2")
    if a == 3:
        print ("3")
    if a == 4:
        print ("4")
    if a == 5:
        print ("5")
    if a == 6:
        print (" 6 - BINGO!!!")
        print (15 * "*")
dice()
    
