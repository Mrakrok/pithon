
from tkinter import *
from tkinter import filedialog as fld
from tkinter import messagebox as msb
import pylab as pl


##### Výběr souboru z disku

def VyberSoubor():
    global cesta
    cesta=fld.askopenfilename(title="Vyberte soubor")
    if cesta!="":
        SouborCesta.set(cesta)

##### Čtení ze souboru a vykreslení grafu
def FceSoubor():
    try:
        cesta = SouborCesta.get()
        soubor=open(cesta,"r")
        nazev=soubor.readline()
        osaX=soubor.readline()
        osaY=soubor.readline()
        x=[]
        y=[]
        while True:
            radek=soubor.readline()
            if radek=='':
                break
            cisla=radek.split()
            x.append(float(cisla[0]) )
            y.append(float(cisla[1]) )
        soubor.close()
        pl.figure("Graf ze souboru")
        pl.plot(x,y)
        pl.title(nazev)
        pl.xlabel(osaX)
        pl.ylabel(osaY)
        pl.grid(True)
        pl.show()
    except:
        msb.showerror("Chybný formát souboru','Graf se nepodařilo vytvořit, \nzkontrolujte fomát souboru.")

hlavni=Tk()
hlavni.title("Technické výpočty a grafy")

##### Vzhled aplikace

souborRam=LabelFrame(hlavni,text="Graf ze souboru",bd=2,relief="ridge")
souborRam.grid(padx=5,pady=5)

SouborCesta=StringVar()
SouborCesta.set("\cesta\k\souboru")

vstupgraf=Entry(souborRam,textvariable=SouborCesta)
vstupgraf.pack(padx=5,pady=10)

otevrit=Button(souborRam,text="Vyber soubor pro graf", width=20,command=VyberSoubor)
otevrit.pack(padx=10,pady=10)

vytvorgraf=Button(hlavni,text="Vytvoř graf", width=15, height=5,command=FceSoubor)
vytvorgraf.grid(row=0,column=1,padx=10)

hlavni.mainloop()