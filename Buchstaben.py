# Autor: Alexander Herbrich
# Wann: 30.01.2016
# Thema: Buchstabieren von Woertern in verschiedene Weisen

def bs(name):
        i = 0
        while i < len(name):
                print (name[i])
                i = i + 1
        
def r_bs(name):
        i = len(name)
        while i > 0:
                print (name[i-1])
                i = i - 1

def x_bs(name):
        iv = 0 ; ir = len(name)
        while iv < len(name):
                print (name[iv])
                iv = iv + 1
        print(20 * "-")
        while ir > 0:
                print (name [ir-1])
                ir = ir - 1

def y_bs(name):
        iv = len(name) ; ir = len(name)
        for iv in range (len(name)):
                print (name[iv])
                iv = iv + 1
        print(20 * "-")
        for ir in range (len(name)):
                print (name [-ir-1])
                ir = ir - 1
