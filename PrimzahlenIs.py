# Autor: Alexander Herbrich
# Wann: 31.01.2016
# Thema: Ueberpruefung einer Primzahl

def is_pz (n):
    k = 0 ; m = (n//2 ) + 1
    if ((n == 0) or (n == 1)):
        print(n,"und negative Zahlen sind nicht erlaubt")
        return False
    if n < 0:
        print ("Negative Zahlen sind nicht erlaubt")
        return False
    for k in range (2, m):
        if (n % k) == 0:
            print(n,'ist keine Primzahl')
            return False
    print(n,'ist einePrimzahl')
    return True
     
     
     
     



    
    
    
    
    
    
    
