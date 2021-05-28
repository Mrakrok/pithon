
from tkinter import *
import math as mt


def Vyp_fce():
    m=int(vstup_m.get())
    n=int(vstup_n.get())
    x=float(vstup_x.get())
    g=n-m+1
    y=0
    for i in range(g):
        y=y+3*((-1)**m)*(mt.sin(x*2))/(1+m**2)
        m=m+1
    vysledek["text"]=str(y)

hlavni=Tk()

ram=LabelFrame(hlavni,text="Výpočet funkční hodnoty",bd=2,relief="ridge",padx=10,pady=10)
ram.grid(padx=5,pady=5)

popis_m=Label(ram,text="Zadej hodnotu m",font="Calibri 10")
popis_m.grid(padx=5)

vstup_m=Entry(ram,font="Calibri 10")
vstup_m.grid(row=1,pady=5)

popis_n=Label(ram,text="Zadej hodnotu n",font="Calibri 10")
popis_n.grid(row=2,padx=5)

vstup_n=Entry(ram,font="Calibri 10")
vstup_n.grid(row=3,pady=5)

popis_x=Label(ram,text="Zadej hodnotu x",font="Calibri 10")
popis_x.grid(row=4,padx=5)

vstup_x=Entry(ram,font="Calibri 10")
vstup_x.grid(row=5,pady=5)

vypocet_fce=Button(ram,text="Proveď \nvýpočet",font="Calibri 10 bold",command=Vyp_fce)
vypocet_fce.grid(row=1,column=1,rowspan=5,sticky=S+N,padx=5,pady=5)

vysledek=Label(ram,text="Výsledek",font="Calibri 12 bold",bg="lightblue")
vysledek.grid(row=6,columnspan=2,sticky=E+W,pady=5)

hlavni.mainloop()