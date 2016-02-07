# Autor: Alexander Herbrich
# Wann: 03.02.2016
# Thema: Hangman ausgebaut

from random import *
import time
import sys

Hangman_Pics = ["""
    
         
         
         
         
         
============== """ , """
    
         |
         |
         |
         |
         |
============== """ , """
    +====+
         |
         |
         |
         |
============== """ , """
    +====+
    |    |
         |
         |
         |
============== """ , """
    +====+
    |    |
    0    |
         |
         |
         |
============== """ , """
    +====+
    |    |
    0    |
    |    |
         |
         |
============== """ ,"""
    +====+
    |    |
    0    |
    |    |
   /     |
         |
============== """ , """
    +====+
    |    |
    0    |
    |    |
   / \   |
         |
============== """ , """
    +====+
    |    |
    0    |
   \|    |
   / \   |
         |
============== """ , """
    +====+
    |    |
    0    |
   \|/   |
   / \   |
         |
============== """ ]
                        


def hangman_start(wait_time):
    liste = ["altenheim","amulett","anlage","arm","aufkleber","auspuff","auto","ball","bar","baum","bestellliste","betttuch","biokraftstoff","blatt","buch","callcenter","castingshow","chinese","clip","computer","dach","dichtung","disco","dollar","dorfschule","eimer","eisenbahn","engel","ergebnis","fahrrad","feuer","film","foto","forelle","freiheit","gehirn","gehweg","grundgesetz","gymnasium","hafen","haus","heimatland","holz","horn","igel","impfstoff","information","infusion","insel","jachthafen","jacke","jobcenter","jugendclub","kaktus","kamm","kammer","keller","leber","leiste","leiter","liebe","locher","maus","monat","monitor","music","muskel","nabelschnur","nachbar","nagel","nase","natur","nonne","notunterkunft","obst","ochse","offizier","orgel","osterei","paket","papier","passwort","pimmel","politiker","poster","quader","quark","quecksilber","quelle","quastenflosser","rabe","radio","rakete","reifen","rettungswagen","ritter","sand","scanner","sprunggelenk","schloss","strauch","tasche","taschenrechner","tastatur","taste","tiger","tisch","turnschuh","ulme","umschlagplatz","umwelt","unwetter","vanille","vater","verdauung","verkehr","versicherung","vogel","waage","waggon","waschzeug","wasser","wort","wurzel","xylophon","yogalehrer","zahn","zeichen","zeitung","zentrum"]
    m = randrange (len(liste))
    wort = (liste[m])
    a = len(wort)
    maske = (a * "-")

    Teilnehmer = input ("Guten Tag. Heute koennen sie eine Runde Hangman spielen. Was ist ihr Name? \n")
    print ("\nSie heissen also " + Teilnehmer + ". Schoen sie mal zu treffen. \n")
    time.sleep(wait_time*6)
    Antwort = input ("\nZum Fortfahren (JA) und zum Beenden (NEIN)")
    if (Antwort.lower() == "ja"):
        print("\nJetzt geht es los :-) Viel Spass und Erfolg beim Raten. \n")
        time.sleep(wait_time*8)
    if (Antwort.lower() == "nein"):
        print ("\nDas Spiel wird jetzt beendet...")
        time.sleep(wait_time*6)
        sys.exit("Das Spiel wurde verlassen")
    return (wort, maske , Teilnehmer)

def Untersuchung (NAMEN, name1,Zeichen): 	
    if (len (NAMEN) != len (name1)):
        return
    z = Zeichen[0]
    name31 = ""
    ianz =0	
    le = len (NAMEN)
    for i in range (le):
        if (NAMEN[i] == z):
            ianz += 1
            name31 = name31 + z
        else:
            name31 = name31 + name1[i]   
    return (name31, ianz)

def PrintHangMan(Leben, wait_time):
    if (Leben == 9):
        time.sleep(wait_time*3)
        print ("Der Galgen wird erstellt...")
    elif (Leben == 3):
        time.sleep(wait_time*3)
        print ("Achtung nur noch 3 Leben...")
    elif (Leben == 1):
        time.sleep(wait_time*3)
        print ("Letzte Chance...")
    time.sleep(wait_time*3)
    print ("\t\t\t\t\t" + Hangman_Pics[9-Leben])
    time.sleep(wait_time*3)

def ReadLetter(wait_time, Versuche, benutzt, Leben, mask):
    time.sleep(wait_time)
    print ("\n")
    print ("-" * 80)
    print (str(Versuche) + ". Versuch")
    print ("\t" * 7 + "Genutzte Buchstaben:")
    print ("\t" * 7 + str(benutzt))
    print ("\t" * 7 + "Leben:")
    print ("\t" * 7 + str(Leben))
    print("\nIhr Wort:")
    print ("\n" + mask + "\n")
    print ("\n")
    return input ("BITTE EINEN BUCHSTABEN EINGEBEN...")
    

def HANGMAN() :
    Leben= 10
    Buchstabe = " "
    wait_time = 0.1
    L1 = hangman_start(wait_time)
    
    word = L1[0]
    Lword = len (word)
    mask = L1[1]
    user = L1[2]
    Versuche = 1
    Fehlversuche = 0
    success = 0
    benutzt = []

    while Leben > 0:
        Buchstabe = ReadLetter(wait_time, Versuche, benutzt, Leben, mask)
        Versuche += 1
        if (Buchstabe in benutzt):
            print ("\nBitte benutzen sie einen Buchstaben der noch nicht verwendet wurde!!! \n")
            time.sleep(wait_time*6)
            continue
        benutzt.append(Buchstabe)

        U1 = Untersuchung (word, mask, Buchstabe)
        new_mask = U1[0]
        gefunden = U1[1]
        print (gefunden)
        if (gefunden == 0 ):
            Leben -= 1
            Fehlversuche += 1
            print ("FALSCH!!! \n")
            PrintHangMan(Leben,wait_time)
        else:
            success += gefunden
            mask  = new_mask
            print ("RICHTIG!!!\n")
            time.sleep(wait_time*3)
            if (success == Lword):
                print ("\n" + mask + "\n")
                if (Fehlversuche == 0):
                    print ("Gewonnen ohne einen Fehlversuch\n")
                else:
                    print ("Gewonnen nach " + str(Fehlversuche) + " Fehlversuch(en)\n")
                    return
    print ("\nDas  wars ...........  Tod durch den Galgen. Das Wort waere " + str(L1[0]) + " gewesen.")
        
HANGMAN()
