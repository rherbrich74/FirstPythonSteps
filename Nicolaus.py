# Autor: Alexander Herbrich
# Wann: 09.02.16
# Thema: Turtle "Haus vom Nicolaus"

from turtle import *

def nicolaus ():
    a = 1
    i = 3
    x = 0
    pencolor("white")
    lt(180)
    fd(220)
    rt(90)
    fd(60)
    rt(90)
    pencolor("red")
    lt(90)
    fd(140)
    lt(30)
    fd(140)
    lt(120)
    fd(140)
    lt(120)
    fd(140)
    lt(225)
    fd(198)
    lt(135)
    fd(140)
    lt(135)
    fd(198)
    lt(135)
    fd(140)
    lt(90)
    fd(140)
    while (a == 1):
        x += 1
        if (i - x == 0):
            pencolor("white")
            rt(90)
            fd(20)
            rt(90)
            fd(560)
            lt(90)
            fd(280)
            lt(90)
            pencolor("red")
            lt(90)
            fd(140)
            lt(30)
            fd(140)
            lt(120)
            fd(140)
            lt(120)
            fd(140)
            lt(225)
            fd(198)
            lt(135)
            fd(140)
            lt(135)
            fd(198)
            lt(135)
            fd(140)
            lt(90)
            fd(140)
            x -= 3
        else:
            pencolor("green")
            lt(90)
            fd(140)
            rt(30)
            fd(140)
            rt(120)
            fd(140)
            rt(120)
            fd(140)
            rt(225)
            fd(198)
            rt(135)
            fd(140)
            rt(135)
            fd(198)
            rt(135)
            fd(140)
            lt(90)
            pencolor("red")
            lt(90)
            fd(140)
            rt(30)
            fd(140)
            rt(120)
            fd(140)
            rt(120)
            fd(140)
            rt(225)
            fd(198)
            rt(135)
            fd(140)
            rt(135)
            fd(198)
            rt(135)
            fd(140)
            lt(90)
nicolaus()
    
