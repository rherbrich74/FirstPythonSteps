# Autor: Alexander Herbrich
# Wann: 03.02.2016
# Thema: Hangman ausgebaut

from random import *
import time

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
                        


def hangman_start():
    
    liste = ["altenheim","amulett","anlage","arm","aufkleber","auspuff","auto","ball","bar","baum","bestellliste","betttuch","biokraftstoff","blatt","buch","callcenter","castingshow","chinese","clip","computer","dach","dichtung","disco","dollar","dorfschule","eimer","eisenbahn","engel","ergebnis","fahrrad","feuer","film","foto","forelle","freiheit","gehirn","gehweg","grundgesetz","gymnasium","hafen","haus","heimatland","holz","horn","igel","impfstoff","information","infusion","insel","jachthafen","jacke","jobcenter","jugendclub","kaktus","kamm","kammer","keller","leber","leiste","leiter","liebe","locher","maus","monat","monitor","music","muskel","nabelschnur","nachbar","nagel","nase","natur","nonne","notunterkunft","obst","ochse","offizier","orgel","osterei","paket","papier","passwort","pimmel","politiker","poster","quader","quark","quecksilber","quelle","quastenflosser","rabe","radio","rakete","reifen","rettungswagen","ritter","sand","scanner","sprunggelenk","schloss","strauch","tasche","taschenrechner","tastatur","taste","tiger","tisch","turnschuh","ulme","umschlagplatz","umwelt","unwetter","vanille","vater","verdauung","verkehr","versicherung","vogel","waage","waggon","waschzeug","wasser","wort","wurzel","xylophon","yogalehrer","zahn","zeichen","zeitung","zentrum"]
    m = randrange (20)
    wort = (liste[m])
    a = len(wort)
    maske = (a * "-")
    
    Teilnehmer = raw_input ("Guten Tag. Heute koennen sie eine Runde Hangman spielen. Duerfte ich ihren Namen erfahren? \n")
    print ("\nSie heissen also " + Teilnehmer + ". Schoen sie mal zu treffen. \n")
    time.sleep(1.75)
    Antwort = raw_input ("\nZum Fortfahren (JA) und zum Beenden (NEIN)")
    if ((Antwort == "JA") or (Antwort == "(JA)") or (Antwort == "Ja") or (Antwort == "(Ja)") or (Antwort == "ja") or (Antwort == "(ja)")):
        print("\nJetzt geht es los :-) Viel Spass und Erfolg beim Raten. \n")
        time.sleep(2)
    else:
        return
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
		else :
 			name31 = name31 + name1[i]   
	return (name31, ianz)

def HANGMAN() :
	Leben= 10
	Buchstabe = " "
	L1 = hangman_start ()
	word = L1[0]
	Lword = len (word)
	mask = L1[1]
	user = L1[2]
	Versuche = 1
	Fehlversuche = 0
	success = 0
	benutzt = []
	while Leben > 0:
                time.sleep(0.25)
                print ("\n\n\n")
                print ( 143 * "-" )
                print ("\n\n\n")
		print (str(Versuche) + ". Versuch")
		Versuche += 1
		if (Leben == 9):
                    print (Hangman_Pics[0])
                if (Leben == 8):
                    print (Hangman_Pics[1])
                if (Leben == 7):
                    print (Hangman_Pics[2])
                if (Leben == 6):
                    print (Hangman_Pics[3])
                if (Leben == 5):
                    print (Hangman_Pics[4])
                if (Leben == 4):
                    print (Hangman_Pics[5])
                if (Leben == 3):
                    print (Hangman_Pics[6])
                if (Leben == 2):
                    print (Hangman_Pics[7])
                if (Leben == 1):
                    print (Hangman_Pics[8])
                if (Leben == 0):
                    print (Hangman_Pics[9])
		print ("\t\t\t\t\t\t\tGenutzte Buchstaben:")
		print ("\t\t\t\t\t\t\t" + str(benutzt))
		print ("\t\t\t\t\t\t\tLeben:")
		print ("\t\t\t\t\t\t\t" + str(Leben) )
		print("Ihr Wort:")
		print ("\n" + mask + "\n")
		print ("EINGABE BITTE...")
		Buchstabe = raw_input ()
		print ("\n")
		if (Buchstabe in benutzt):
                    print ("\nBitte benutzen sie einen Buchstaben der noch nicht verwendet wurde!!! \n")
                    time.sleep(1.5)
                    continue
		benutzt.append(Buchstabe)
		
		U1 = Untersuchung (word, mask, Buchstabe)
		new_mask = U1[0]
		gefunden = U1[1]
		if (gefunden == 0 ):
                    Leben -= 1
                    Fehlversuche += 1
                    print ("FALSCH!!! \n")
                    if (Leben == 9):
                        time.sleep(1)
                        print ("Der Galgen wird erstellt...")
                        time.sleep(1)
                        print (Hangman_Pics[0])
                        time.sleep(1)
                    if (Leben == 8):
                        time.sleep(0.75)
                        print (Hangman_Pics[1])
                        time.sleep(1)
                    if (Leben == 7):
                        time.sleep(0.75)
                        print (Hangman_Pics[2])
                        time.sleep(1)
                    if (Leben == 6):
                        time.sleep(0.75)
                        print (Hangman_Pics[3])
                        time.sleep(1)
                    if (Leben == 5):
                        time.sleep(0.75)
                        print (Hangman_Pics[4])
                        time.sleep(1)
                    if (Leben == 4):
                        time.sleep(0.75)
                        print (Hangman_Pics[5])
                        time.sleep(1)
                    if (Leben == 3):
                        time.sleep(0.75)
                        print ("Achtung nur noch 3 Leben...")
                        time.sleep(1)
                        print (Hangman_Pics[6])
                        time.sleep(1)
                    if (Leben == 2):
                        time.sleep(0.75)
                        print (Hangman_Pics[7])
                        time.sleep(1)
                    if (Leben == 1):
                        time.sleep(0.75)
                        print ("Letzte Chance...")
                        time.sleep(1)
                        print (Hangman_Pics[8])
                        time.sleep(1)
                    if (Leben == 0):
                        time.sleep(0.75)
                        print (Hangman_Pics[9])
                        time.sleep(1)
                else:
                    success += gefunden
                    mask  = new_mask
                    print ("RICHTIG!!!\n\n")
                    time.sleep(0.75)
                    if (success == Lword):
                        if (Fehlversuche == 0):
                            print (" Gewonnen ohne einen Fehlversuch\n")
                        else:
                            print (" Gewonnen nach " + str(Fehlversuche) + " Fehlversuch(en)\n")
                            return
        
	print ("\nDas  wars ...........  Tod durch den Galgen. Das Wort waere " + str(L1[0]) + " gewesen.")

