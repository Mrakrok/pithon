from tkinter import *
from tkinter import messagebox as msb
from tkinter import colorchooser as clc
import pylab as pl

#funkce pro zadávání souřadnic
def Uloz():
    try:
    global x_ove
    global y_ove
    x_ove.append(float(bodx.get()))
    y_ove.append(float(body.get()))
    vstupx.delete(0,END)
    vstupy.delete(0,END)
    vstupx.focus_set()
    #zobrazení zadaných souřadnic
    vypis.delete(1.0,END)
    vypis.insert(1.0,"x: ")
    vypis.insert(END,x_ove)
    vypis.insert(END,"\n")
    vypis.insert(END,"y: ")
    vypis.insert(END,y_ove)
 except:
    msb.showerror("Chyba!","Chybějící nebo neplatná vstupní data")
    vstupx.delete(0,END)
    vstupy.delete(0,END)
    vstupx.focus_set()

def Graf():
    x=pl.array(x_ove)
    y=pl.array(y_ove)
    tl=int(tloustka.get())
    pl.plot(x,y,color=b,linewidth=tl)
    if vstupg.get()!="":
    pl.title(vstupg.get())
    if vstupox.get()!="":
    pl.xlabel(vstupox.get())
    if vstupoy.get()!="":
    pl.ylabel(vstupoy.get())
    if m.get():
    pl.grid(True)
    pl.show()

def Barva():
    global b
    x=clc.askcolor(title="Výběr barvy")
    b=x[1]
    zobrbarvy["bg"]=b


hlavni=Tk()
hlavni.title("Grafy")

#proměnné pro souřadnice
bodx=StringVar()
body=StringVar()
x_ove=[]
y_ove=[]
b="black" #nastavení výchozí barvy

#Vzhled aplikace
ram=LabelFrame(hlavni,text="Zadání
souřadnic",bd=2,relief="ridge",padx=5,pady=5)
ram.pack(padx=10,pady=10)

popis1=Label(ram,text="Souřadnice x",font="Calibri 10")
popis1.grid(row=0,column=0,pady=3)

vstupx=Entry(ram,font="Calibri 10",textvariable=bodx)
vstupx.grid(row=0,column=1,pady=3)

popis2=Label(ram,text="Souřadnice y",font="Calibri 10")
popis2.grid(row=1,column=0,pady=3)

vstupy=Entry(ram,font="Calibri 10",textvariable=body)
vstupy.grid(row=1,column=1,pady=3)

uloz=Button(ram,text="Ulož a další",width=15,font="Calibri 12",command=Uloz)
uloz.grid(row=2,column=0,columnspan=2,pady=10)

#Pro zobrazení souřadnic
vypis=Text(height=4,width=50)
vypis.pack()

#Pro vlatnosti grafu
ram2=LabelFrame(hlavni,text="Parametry
grafu",bd=2,relief="ridge",padx=5,pady=5)
ram2.pack(padx=10,pady=10)

popisg=Label(ram2,text="Název grafu",font="Calibri 10")
popisg.grid(pady=3)

vstupg=Entry(ram2,font="Calibri 10")
vstupg.grid(row=0,column=1)

popisox=Label(ram2,text="Název osy x",font="Calibri 10")
popisox.grid(row=1,pady=3)

vstupox=Entry(ram2,font="Calibri 10")
vstupox.grid(row=1,column=1,pady=3)

popisoy=Label(ram2,text="Název osy y",font="Calibri 10")
popisoy.grid(row=2,pady=3)

vstupoy=Entry(ram2,font="Calibri 10")
vstupoy.grid(row=2,column=1,pady=3)

tloustka=StringVar()
tloustka.set("1")

popisc=Label(ram2,text="Tloušťka čáry",font="Calibri 10")
popisc.grid(row=3,column=0,pady=3)

cara=Spinbox(ram2,from_=1,to=10,textvariable=tloustka,font="Calibri 10",width=15)
cara.grid(row=3,column=1)

m=BooleanVar()
mrizka=Checkbutton(ram2,text="Mřížka",font="Calibri 10",variable=m)
mrizka.grid(row=4,column=0,pady=3)

barva=Button(ram2,text="Barva čáry",font="Calibri 10",width=15,command=Barva)
barva.grid(row=5,column=0,pady=3)

zobrbarvy=Label(ram2,width=3,height=1,bg=b,relief="sunken")
zobrbarvy.grid(row=5,column=1,pady=3)

kresligraf=Button(hlavni,text="Vykresli graf",width=15,font="Calibri 12 bold",command=Graf)
kresligraf.pack(pady=10)

hlavni.mainloop()