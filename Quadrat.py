# Autor: Alexander Herbrich
# Wann: 03.02.2016
# Thema: Programm zum loesen des magischen Quadrats erstellen

def quadrat():
#    A + B + C = S
#    D + M + d = S
#    a + b + c = S
#    A + D + a = S
#    B + M + b = S
#    C + d + c = S
#    A + M + c = S
#    C + M + a = S
    MAX = 21
    ianz = 0
    ianz2 = 0
    A = 0
    C = 0
    B = 0
    S = 0
    M = 0
    D = 0
    d = 0
    a = 0
    b = 0
    c = 0
    for C in range (2 , MAX):
        for B in range (2 , MAX):
            if (C == B) :
                continue
            for  A in range (2 , MAX):
                if (A == B) or (A == C) :
                    continue
            S = A + B + C
            if (S % 3) != 0:
                continue
            M = S // 3
            ianz += 1
            if M not in range (2, 21):
                continue
            a = S - M - A
            if (a < 1) or (a == A) or (a == B) or (a == C) or (a == M):
                continue
            b = S - M - B
            if (b < 1) or (b == A) or (b == B) or (b == C) or (b == M) or (b == a):
                continue
            c = S - M - C
            if (c < 1) or (c == A) or (c == B) or (c == C) or (c == M) or (c == a) or (c == b):
                continue
            D = S - c - A
            if (D < 1) or (D == A) or (D == B) or (D == C) or (D == M) or (D == a) or (D == b) or (D == c):
                continue            
            d = S - D - M
            if (d < 1) or (d == A) or (d == B) or (d == C) or (d == M) or (d == a) or (d == b) or (d == c) or (d == D):
                continue
            if ((d+C+a) != S):
                print ("nicht zulaessig1...","|",A,B,C,"|",D,M,d,"|",c,b,a,"|",S)
                continue
            if ((b+c+a) != S):
                print ("nicht zulaessig2...","|",A,B,C,"|",D,M,d,"|",c,b,a,"|",S)
                continue
            ianz2 += 1
            print ("\n",A,B,C,"\n",D,M,d,"\n",c,b,a,"\n\tSumme: ",S,"\n")
#           print("\tA =%4i  \tB =%4i  \tC =%4i \tD =%4i \tM =%4i \td =%4i \tc =%4i \tb =%4i \ta =%4i \tS =%4i " % (A,B,C,D,M,d,c,b,a,S))
#           print ("\tA=" + str(A) + "\tB=" + str(B) + "\tC=" + str(C) + "\tM=" + str(M) + "\tS=" + str(S))
            
    print ("Anzahl:" + str(ianz) + "\tAnzahl2:" + str(ianz2))
    
                            
