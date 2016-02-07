# Autor: Alexander Herbrich
# Wann: 01.02.2016
# Thema: Spiel Bingo

from random import *

def bingo():
        a = randrange(1,26)
        b = randrange(1,26)
        if (a == b):
                print (a,b,"Herzlichen Glueckwunsch. Sie haben den Bingo geknackt")
                print (55 * "*")
        else:
                print (a,b,"Schade :( Naechstes mal hast du vielleicht mehr Glueck")
    
        
    
