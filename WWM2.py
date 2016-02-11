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
    Teilnehmer = delay_input ("""Willommen beim Hauptstadt-Wissenstest. Sie koennen hier ein paar Fragen beantworten, um ihr Wissen zu ueberpruefen.
Wie heissen sie denn? \n""")
    Teilnahme = delay_input ("\nHallo " + Teilnehmer + "! Wollen sie denn ueberhaupt am Quiz teilnehmen? Zum Fortfahren (JA) und zum Beenden (NEIN)\n")
    if (Teilnahme.lower() == "ja"):
        delay_print("\nJetzt geht es los :-) Viel Spass und Erfolg. \n")
        time.sleep(wait_time*4)
    else:
        delay_print ("\nDas Spiel wird jetzt beendet...\n")
        time.sleep(wait_time*4)
        sys.exit("Das Spiel wurde verlassen\n") 

def WWM_eingabe(wait_time, versuch, leben):
    print ("\n" + str(versuch) + ". Versuch")
    print ("\t" * 7 + "Leben:")
    print ("\t" * 7 + str(leben))

def WWM_fragen():
    with open("fragen.txt") as f:
        liste = [w.strip() for w in f.readlines()]
    m = randrange (0, (len(liste)), 2) 
    frage = (liste[m])
    antwort = (liste[m + 1])
    return (frage, antwort)

def WWM():
    versuch = 0
    wait_time = 0.15
    leben = 3
    benutzt = []
    #WWM_start(wait_time)
    while leben > 0:
        L1 = WWM_fragen()
        question = L1[0]
        anwser = L1[1]
        if (question in benutzt):
            continue
        benutzt.append(question)
        
        versuch += 1
        WWM_eingabe(wait_time, versuch, leben)
        print ("\n")
        Antwort = delay_input(question + "\n")
        if (Antwort.lower() == anwser.lower()):
            #delay_print ("\nYeah! Sie haben die " + str(versuch) + ". Frage richtig beantwortet!\n\n")
            delay_print ("\nJaa!!! Du lagst richtig!\n")
            time.sleep(wait_time * 3)
        else:
            #delay_print ("\nOhh! Leider haben sie die " + str(versuch) + ". Frage falsch beantwortet!\n\n")
            delay_print("\nOhh!!! Du lagst NICHT richtig! Die richtige Loesung waere " + anwser.upper() + " gewesen.\n")
            time.sleep(wait_time * 4)
            leben -= 1
            benutzt.pop()
WWM()