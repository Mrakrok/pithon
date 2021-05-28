from tkinter import *
from tkinter import filedialog as fld
from tkinter import messagebox as msb 

def Otevrit():
    text.delete(1.0,END)
    cesta=fld.askopenfilename(title="Otevřít soubor")
    try:
        soubor=open(cesta,"r")
        for radek in soubor:
            text.insert(END,radek)
        soubor.close()
    except:pass

def Ulozit():
    cesta=fld.asksaveasfilename(title="Ulozit soubor",defaultextension="txt")
    try:
        soubor=open(cesta,"w")
        retezec=text.get(1.0,END)
        soubor.write(retezec)
        soubor.close()
    except:pass

def Konec():
    x=msb.askyesno("Konec aplikace","Opravdu chcete skončit")
    if x:hlavni.destroy()

def Velka():
    a=text.get(1.0,END)
    a=a.upper()
    text.delete(1,0,END)
    text.insert(1.0,a)

def OknoNahrad():
    global vstup1
    global vstup2
    global oknoN
    oknoN=Toplevel()
    oknoN.title("Nahrazení")
    t1=Label(oknoN,text="Nahradit znak")
    t1.pack(pady=3)
    vstup1=Entry(oknoN)
    vstup1.pack(pady=3)
    t2=Label(oknoN,text="Tímto nahradit")
    t2.pack(pady=3)
    vstup2=Entry(oknoN)
    vstup2.pack(pady=3)
    akce1=Button(oknoN,text="Proved",width=10,command=Nahradit)
    akce1.pack(pady=3)

def Nahradit():
    retezec=text.get(1.0,END)
    retezec1=retezec.replace(vstup1.get(),vstup2.get())
    text.delete(1.0,END)
    text.insert(1.0,retezec1)
    oknoN.destroy()

def Statistika():
    seznam=[]
    oknoS=Toplevel()
    oknoS.title("Statistika")
    texts=Text(oknoS,font="Arial 8",width=20,height=30)
    texts.pack(pady=3,padx=3)
    radky=text.get(1.0,END)
    radky=radky.lower()
    for i in radky:
        seznam.append(i)
    for i in abeceda:
        if i in seznam:
            texts.insert(END,i+":")
            texts.insert(END,str(seznam.count(i)))
            text.insert(END,"\n")
        else:
            texts.insert(END,i+":0")
            texts.insert(END,"\n") 

hlavni=Tk()
hlavni.title("Soubory")


abeceda=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","g","r","s","t","u","v","w","x","y","z"]


#vzhled aplikace
text=Text(hlavni,font="Arial 10")
text.pack()

hornimenu=Menu(hlavni)
menusoubor=Menu(hornimenu,tearoff=0)
menusoubor.add_command(label="Otevřít",command=Otevrit)
menusoubor.add_command(label="Uložit",command=Ulozit)
menusoubor.add_separator()
menusoubor.add_command(label="Konec",command=Konec)
hornimenu.add_cascade(label="Soubor",menu=menusoubor)

menuoperace=Menu(hornimenu,tearoff=0)
menuoperace.add_command(label="Velká písmena",command=Velka)
menuoperace.add_command(label="Nahradit znak",command=OknoNahrad)
menuoperace.add_command(label="Statistika znaků",command=Statistika)
hornimenu.add_cascade(label="Operace",menu=menuoperace)

hlavni.config(menu=hornimenu)

hlavni.mainloop()

