
from tkinter import *
from tkinter import filedialog as fld
from tkinter import messagebox as msb
import pylab


#výběr souboru
def VyberSoubor():
    global cesta
    cesta=fld.askopenfilename(title="Vyberte soubor")
    if cesta!="":
        SouborCesta.set(cesta)

#čteni ze souboru a vykreslení grafu
def FceSoubor():
    try:
        soubor=open(cesta,"r")
        nazev=soubor.readline()
        osaX=soubor.readline()
        osaY=soubor.readline()
        x=[]
        y=[]
        while True:
            radek=soubor.readline()
            if radek=="":
                break
            cisla=radek.split()
            x.append(float(cisla[0]))
            y.append(float(cisla[1]))
        soubor.close()
        pylab.plot(x,y)
        pylab.title(nazev)
        pylab.xlabel(osaX)
        pylab.ylabel(osaY)
        pylab.grid(True)
        pylab.show()
    except:
        msb.showerror("Chybný formát souboru","Graf se nepodřilo vytvořit,\zkontrolujte formát souboru")



main=Tk()
main.title("Graf")


#vzhled aplikace
souborRam=LabelFrame(main,text="Graf se souboru",bd=2,relief="ridge")
souborRam.grid(padx=5,pady=5)

SouborCesta=StringVar
SouborCesta.set=("\cesta\k\souboru")
vstupgraf=Entry(souborRam,textvariable=SouborCesta)
vstupgraf.pack(padx=5,pady=5)

otevrit=Button(souborRam,text="Vyber soubor pro graf",width=20,command=VyberSoubor)
otevrit.pack(padx=5,pady=5)

vytvorgraf=Button(main,text="Vytvoř graf",width=15,height=5,command=FceSoubor)
vytvorgraf.grid(row=0,column=1,padx=10)


main.mainloop()
