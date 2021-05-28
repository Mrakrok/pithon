from tkinter import *  
from tkinter.messagebox import * 

hlavni = Tk()
vstup = Entry(hlavni)
vstup.grid(row=0, column= 2)
def směna():
    global value
    try:
        amount = int(vstup.get())
    except:
        showerror("Answer", "zadavejte cisla")
    if amount <= 0:
        showerror("Answer", "zadejte částku větší jak 0")
    else:  
        if value == 1:
            amount = amount*20
        if value == 2:
            amount = amount*0.2
        if value == 3:
            amount = amount*0.3
        final = Label(hlavni, text=amount)
        final.grid(row = 3, column = 2)

def dogeco():
    global value
    value = 1
def bitco():
    global value
    value = 2
def krav():
    global value
    value = 3
butt = Button(hlavni, text = "převod", command=směna)
butt.grid(row = 1, column = 2)

doge = Radiobutton(hlavni, text="dogecoin", value = 0, command = dogeco)
doge.grid(row = 2, column = 1)

bitcoin = Radiobutton(hlavni, text="bitcoin", value = 1, command = bitco)
bitcoin.grid(row = 2, column = 2)

krava = Radiobutton(hlavni, text="krávy", value = 2, command = krav)
krava.grid(row =2, column= 3)


hlavni.mainloop()