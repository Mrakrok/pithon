

from tkinter import *

def Nacteni_kurzu():
    kurzy=(("EUR",24.30,26.10),("GBP",28.70,30.25),("USD",18.06,19.07))

    return kurzy

def zmena_meny(*args):
    castka.configure(text="Částka ["+str(kurzy[int(kurz_RB.get())-1][0])+"]")
    vypocet()
    return

def vypocet():
    if c_entry.get()=="":
        return
    try:
        float(c_entry.get())
    except:
        text.configure(text="Chyba vstupu \n(Zadaná částka musí být číslo)")
        return
    if nakup_prodej_RB.get()==1:
        text.configure(text="Vyplatit "+str(float(c_entry.get())*float(kurzy[int(kurz_RB.get())-1][1]))+" Kč")
    else:
        text.configure(text="Inkasovat "+str(float(c_entry.get())*float(kurzy[int(kurz_RB.get())-1][2]))+" Kč"
                       )
    return


###################################################################
#################### "First steps" ################################
###################################################################
hl=Tk()
hl.title("* -- EXCHANGE -- *")
kurzy=Nacteni_kurzu()
hlavni=LabelFrame(hl,padx=50,pady=10)
hlavni.pack(side=TOP)

###################################################################
############################ KURZY ################################
###################################################################
kurz_RB=IntVar()
kF=LabelFrame(hlavni,text="Kurzy naší směnárny")
kF.grid(row=0,column=0)

l_nakup=Label(kF,text="Nákup")
l_nakup.grid(row=0,column=1)

EUR_N=Label(kF,text=kurzy[0][1])
EUR_N.grid(row=1,column=1)
GBP_N=Label(kF,text=kurzy[1][1])
GBP_N.grid(row=2,column=1)
USD_N=Label(kF,text=kurzy[2][1])
USD_N.grid(row=3,column=1)

l_prodej=Label(kF,text="Prodej")
l_prodej.grid(row=0,column=2)

EUR_P=Label(kF,text=kurzy[0][2])
EUR_P.grid(row=1,column=2)
GBP_P=Label(kF,text=kurzy[1][2])
GBP_P.grid(row=2,column=2)
USD_P=Label(kF,text=kurzy[2][2])
USD_P.grid(row=3,column=2)

l_mena=Label(kF,text="Měna")
l_mena.grid(row=0,column=0)

Radiobutton(kF,text=kurzy[0][0],variable=kurz_RB,value=1).grid(row=1,column=0)
Radiobutton(kF,text=kurzy[1][0],variable=kurz_RB,value=2).grid(row=2,column=0)
Radiobutton(kF,text=kurzy[2][0],variable=kurz_RB,value=3).grid(row=3,column=0)

kurz_RB.trace("w",zmena_meny)
              
###################################################################
#################### Nákup Prodej #################################
###################################################################
nakup_prodej_RB=IntVar()
npF=LabelFrame(hlavni,text="")
npF.grid(row=1,column=0)

Radiobutton(npF,text="Nákup",variable=nakup_prodej_RB,value=1).grid(row=0,column=0)
Radiobutton(npF,text="Prodej",variable=nakup_prodej_RB,value=2).grid(row=0,column=1)

nakup_prodej_RB.trace("w",zmena_meny)

###################################################################
################### CASTKA, SPOCITAT ... ##########################
###################################################################
L_Frame=LabelFrame(hlavni,text="")
L_Frame.grid(row=2,column=0)

castka=Label(L_Frame,text="Částka[-]")
castka.grid(row=0,column=0)

c_entry=Entry(L_Frame,width=9)
c_entry.grid(row=0,column=1)

text=Label(L_Frame,text="Stiskni vypočítat!")
text.grid(row=1,columnspan=2)

tl=Button(L_Frame,text="Vypočítat",command=vypocet)
tl.grid(row=2,columnspan=2)

###################################################################
###################################################################

hlavni.mainloop()
    
