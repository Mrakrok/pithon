# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:33:14 2014

@author: Ocelot
"""


from tkinter import *
from random import *





def Priklad():
    global Vystup
    a=randint(0,100)
    b=randint(0,100)
    while a+b>100:
        a=randint(0,100)
        b=randint(0,100)
    Napis1.configure(text=u"Příklad: " + str(a) + " + " + str(b)   )
    Vystup=(a)+(b)
     
            
y=0
n=0
p=0
      
def Overit():
    global Vystup
    global y
    global p
    global n
    if Vstup.get()==str(Vystup):    
        Napis3.configure(text=u"SPRÁVNĚ!")
        y+=1
        p+=1
        n=n
        Napis5.configure(text=u"Odpovězeno správně:  " + str(y))
        Napis4.configure(text=u"Počet příkladů: " + str(p))
        
    elif Vstup.get()!=str(Vystup):
        Napis3.configure(text=u"ŠPATNĚ!")
        y=y
        n+=1
        p+=1
        Napis6.configure(text=u"Odpovězeno špatně:  " + str(n))
        Napis4.configure(text=u"Počet příkladů: " + str(p))
    
    
    if Metoda.get()==0:
        a=randint(0,100)
        b=randint(0,100)
        while a+b>100:
            a=randint(0,100)
            b=randint(0,100)
        Napis1.configure(text=u"Příklad: " + str(a) + " + " + str(b)   )
        Vystup=(a)+(b)

            
    elif Metoda.get()==1:
        c=randint(1,100)
        d=randint(0,100)
        while c<d:
            c=randint(1,100)
            d=randint(0,10)
        Napis1.configure(text=u"Příklad: " + str(c) + " - " + str(d)   )
        Vystup=(c)-(d)

        
    elif Metoda.get()==2:
        e=randint(1,10)
        f=randint(1,10)
        Napis1.configure(text=u"Příklad: " + str(e) + " * " + str(f)   )
        Vystup=(e)*(f)

            
    elif Metoda.get()==3:
        g=randint(1,100)
        h=randint(1,10)
        while g%h==0 and g/h<=10:
            g=randint(1,100)
            h=randint(1,10)
        Napis1.configure(text=u"Příklad: " + str(g) + " / " + str(h)   )
        Vystup=g%h
    






#######

Okno = Tk()
Okno.title("Počítání")


Ramecek0 = Frame(Okno)
Ramecek0.pack(pady=1,padx=1)

Napis0 = Label(Ramecek0,text="POČÍTÁNÍ", font=("Arial",20))
Napis0.pack(side="top", padx=20,pady=3)

### OPERACE

Metoda = IntVar() 

Ramecek1 = LabelFrame(Okno,text=u"Početní operace:")
Ramecek1.pack(pady=1,padx=1) 

ScitaniB=Radiobutton(Ramecek1,text=u"Sčítání", value=0, variable=Metoda)
ScitaniB.pack(side=LEFT)

OdcitaniB=Radiobutton(Ramecek1,text=u"Odčítání", value=1, variable=Metoda)
OdcitaniB.pack(side=LEFT)

NasobeniB=Radiobutton(Ramecek1,text=u"Násobení", value=2, variable=Metoda)
NasobeniB.pack(side=LEFT)

DeleniB=Radiobutton(Ramecek1,text=u"Dělení", value=3, variable=Metoda)
DeleniB.pack(side=LEFT)



### PŘÍKLAD

Ramecek2 = Frame(Okno)
Ramecek2.pack(pady=1,padx=1)

Napis1 = Label(Ramecek2,text="Příklad: - - - - -", font=("Arial", 20))
Napis1.pack(side="top", padx=20,pady=6)

VstupVar=StringVar()

Ramecek3 = Frame(Okno)
Ramecek3.pack(pady=1,padx=1)

Napis2 = Label(Ramecek3,text=u"Zadejte výsledek: ")
Napis2.pack(side="left", padx=10,pady=5)

Vstup = Entry(Ramecek3, textvariable=VstupVar)
Vstup.pack(side="right", padx=10, pady=5)

Tlacitko1 = Button(Okno, text=u"Potvrdit", command=Overit)
Tlacitko1.pack(padx=10,pady=5)

### VÝPIS PLATBY

Napis3 = Label(Okno, text=u"", font=("Arial", 15))
Napis3.pack()

Napis4 = Label(Okno, text=u"Počet příkladů: " + str(p))
Napis4.pack()

Napis5 = Label(Okno, text=u"Odpovězeno správně:  " + str(y))
Napis5.pack()

Napis6 = Label(Okno, text=u"Odpovězeno špatně: " + str(n))
Napis6.pack()

TlacitkoX = Button(Okno, text=u"Ukončení",command=Okno.destroy)
TlacitkoX.pack(padx=10,pady=5)

Priklad()

Okno.mainloop()
