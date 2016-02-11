from random import *
from math import *
import time
import sys

def delay_print(s, delay=0.06):
    for c in str(s):
        sys.stdout.write('%s' % c )
        sys.stdout.flush()
        time.sleep(delay)

def delay_input(s):
    delay_print(s)
    return input()

def WWM_start(wait_time):
    Teilnehmer = delay_input ("""Willommen beim Allgemeinwissenstest. Sie koennen hier ein paar Quizfragen beantworten, um ihr Wissen zu ueberpruefen.
Wie heissen sie denn? \n""")
    Teilnahme = delay_input ("\nHallo " + Teilnehmer + "! Wollen sie denn ueberhaupt am Quiz teilnehmen? Zum Fortfahren (JA) und zum Beenden (NEIN)\n")
    if (Teilnahme.lower() == "ja"):
        delay_print("\nJetzt geht es los :-) Viel Spass und Erfolg. \n")
        time.sleep(wait_time*4)
    else:
        delay_print ("\nDas Spiel wird jetzt beendet...\n")
        time.sleep(wait_time*4)
        sys.exit("Das Spiel wurde verlassen\n") 
        
    #if (Teilnahme.lower() == "nein"):
        #delay_print ("\nDas Spiel wird jetzt beendet...\n")
        #time.sleep(wait_time*4)
        #sys.exit("Das Spiel wurde verlassen\n") 

def WWM_eingabe(wait_time, versuch, leben):
    print ("\n" + str(versuch) + ". Versuch")
    print ("\t" * 7 + "Leben:")
    print ("\t" * 7 + str(leben))

def WWM():
    versuch = 0
    wait_time = 0.15
    leben = 3
    #WWM_start(wait_time)
    while leben > 0:
        versuch += 1
        WWM_eingabe(wait_time, versuch, leben)
        Antwort = delay_input ("\nWas ist das Wahrzeichen von Paris? \n")
        if ((Antwort.lower() == "der eiffelturm") or (Antwort.lower() == "eiffelturm")):
            delay_print ("\nYeah! Sie haben die " + str(versuch) + ". Frage richtig beantwortet!\n")
        else:
            delay_print ("\nOhh! Leider haben sie die " + str(versuch) + ". Frage falsch beantwortet!\n")
            leben -= 1
WWM()