# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:47:54 2019

@author: odg46
"""
        
import random
      

def Menu() :
    print("1.optellen")
    print("2.aftrekken")
    print("3.keer")
    print("4.delen")
    print("5.sluiten")
    Keuze = int(input("Maak uw keuze:"))
    if Keuze == 1:
            print("1.optellen")
            optellen()
            Menu()
            
    elif Keuze == 2:
            print("2.aftrekken")
            aftrekken()
            Menu()
            
    elif Keuze == 3:
            print("3.keer") 
            keer()
            Menu()
            
    elif Keuze == 4:
            print("4.delen")
            delen()
            Menu()
            
    elif Keuze == 5:
            exit 
                  

def optellen() :
    plusscore = 0
    plusscore = int(plusscore)
    for i in range(5):
       a = (random.randint(1,101))
       b = (random.randint(1,101))
       a = int(a)
       b = int(b)
       print(a,"+",b,"=")
       Plussom = int(input("uitkomst:"))
       if Plussom == a+b:
            print ("goed")
            print("score:",plusscore,"+ 100 punten")
            plusscore = plusscore + 100 
       else:
            print ("Fout! Het goede antwoord is",a+b)
            print("score:",plusscore)
        
def aftrekken():
    minscore = 0
    minscore = int(minscore)
    for i in range(5):
        a = (random.randint(1,101))
        b = (random.randint(1,101))
        a = int(a)
        b = int(b)
        if a >= b:
            print(a,"-",b,"=")
            Plussom = int(input("uitkomst:"))
            if Plussom == a-b:
                print ("goed")
                print("score:",minscore,"+ 100 punten")
                minscore = minscore + 100 
            else:
                print ("Fout! Het goede antwoord is",a-b)
                print("score:",minscore)
        if a <= b:
            print(b,"-",a,"=")
            Plussom = int(input("uitkomst:"))
            if Plussom == b-a:
                print ("goed")
                print("score:",minscore,"+ 100 punten")
                minscore = minscore + 100 
            else:
                print ("Fout! Het goede antwoord is",a-b)
                print("score:",minscore)

def keer():
    keerscore = 0
    keerscore = int(keerscore)
    for i in range(5):
        a = (random.randint(1,12))
        b = (random.randint(1,12))
        a = int(a)
        b = int(b)
        print(a,"x",b,"=")
        Plussom = int(input("uitkomst:"))
        if Plussom == a*b:
            print ("goed")
            print("score:",keerscore,"+ 100 punten")
            keerscore = keerscore + 100 
        else:
            print ("Fout! Het goede antwoord is",a*b)
            print("score:",keerscore)
        
 
def delen():
    deelscore = 0
    deelscore = int(deelscore)
    for i in range(5):
        a = (random.randint(1,12))
        b = (random.randint(1,12))
        c=a*b
        a = int(a)
        b = int(b)
        c = int(c)
        print(c,":",b,"=")
        Plussom = int(input("uitkomst:"))
        if Plussom == c/b:
            print ("goed")
            print("score:",deelscore,"+ 100 punten")
            deelscore = deelscore + 100 
        else:
            print ("Fout! Het goede antwoord is",c/b)
            print("score:",deelscore)
        
                  
    
# main routine
Menu()

