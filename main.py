import random
import time
import pyautogui
from tkinter import *
from tkinter import messagebox
import os
root = Tk()
root.title("FAST FOOD MENU")
root.config(bg='#000000')
#root.resizable(0,0)
root.geometry('850x755')
# image = Image.open("bg1.PNG")
# photo = ImageTk.PhotoImage(image)
# label = Label(root, text="Background image",image=photo)
# label.configure(image=photo,width=1080,height=1080)
# label.pack()
 
#functions
def receiptsfile():
    os.listdir(r"C:\Users\saira\PycharmProjects\DIGITAL MENU AND BILL GENERATOR\recipts")
 
    os.startfile(r"C:\Users\saira\PycharmProjects\DIGITAL MENU AND BILL GENERATOR\recipts")
 
def save():
    global billnumber
    new_name=pyautogui.prompt("Enter the name:",title='Name',default='xyz')
    new_name+='_'+ billnumber +".txt"
    bill_data=textrecript.get(1.0,END)
    ff = open(new_name , 'w')
    ff.write(bill_data)
    ff.close()
    messagebox.showinfo('Information','your bill is succesfully saved')
 
def receipt():
    global totalcost, tax, subtotal
    global billnumber
    textrecript.delete(1.0,END)
    x=random.randint(100,1000)
    billnumber='BILL  '+str(x)
    date=time.strftime('%d/%m/%Y')
    textrecript.insert(END,'RECEIPT REFERENCE\t\t '+ billnumber+'\t  '+date)
    textrecript.insert(END,'\n\n****************************************\n')
    textrecript.insert(END, 'items:\t\t Cost of items\n')
    textrecript.insert(END, '\n\n****************************************\n')
    if e_var1.get()!='0':
        textrecript.insert(END, f'Sticks\t\t\t{int(e_var1.get())*5}\n\n')
    if e_var2.get() != '0':
        textrecript.insert(END, f'fries\t\t\t{int(e_var2.get()) * 8}\n\n')
    if e_var3.get() != '0':
        textrecript.insert(END, f'fingers\t\t\t{int(e_var3.get()) * 6}\n\n')
    if e_var4.get() != '0':
        textrecript.insert(END, f'soup\t\t\t{int(e_var4.get()) * 4}\n\n')
    if e_var5.get() != '0':
        textrecript.insert(END, f'wedges\t\t\t{int(e_var5.get()) * 5}\n\n')
    if e_var6.get() != '0':
        textrecript.insert(END, f'rings\t\t\t{int(e_var6.get()) * 7}\n\n')
    if e_var7.get() != '0':
        textrecript.insert(END, f'cheese burger\t\t\t{int(e_var7.get()) * 7}\n\n')
    if e_var8.get() != '0':
        textrecript.insert(END, f'Stroanoff\t\t\t{int(e_var8.get()) * 6}\n\n')
    if e_var9.get() != '0':
        textrecript.insert(END, f'Chilli\t\t\t{int(e_var9.get()) * 6}\n\n')
    if e_var10.get() != '0':
        textrecript.insert(END, f'Pounder\t\t\t{int(e_var10.get()) * 6}\n\n')
    if e_var11.get() != '0':
        textrecript.insert(END, f'fourcheese\t\t\t{int(e_var11.get()) * 7}\n\n')
    if e_var12.get() != '0':
        textrecript.insert(END, f'swiss\t\t\t{int(e_var12.get()) * 7}\n\n')
    if e_var13.get() != '0':
        textrecript.insert(END, f'bits\t\t\t{int(e_var13.get()) * 4}\n\n')
    if e_var14.get() != '0':
        textrecript.insert(END, f'cream\t\t\t{int(e_var14.get()) * 3}\n\n')
    if e_var15.get() != '0':
        textrecript.insert(END, f'pepper\t\t\t{int(e_var15.get()) * 3}\n\n')
    if e_var16.get() != '0':
        textrecript.insert(END, f'onions\t\t\t{int(e_var16.get()) * 4}\n\n')
    if e_var17.get() != '0':
        textrecript.insert(END, f'sauce\t\t\t{int(e_var17.get()) * 3}\n\n')
    if e_var18.get() != '0':
        textrecript.insert(END, f'Sourcream\t\t\t{int(e_var18.get()) * 3}\n\n')
    textrecript.insert(END, '\n\n****************************************\n')
    if ee_var4.get()!='$ 0':
        textrecript.insert(END, f'Subtotal\t\t\t{subtotal}\n\n')
    if ee_var5.get() != '$ 0':
        textrecript.insert(END, f'Tax\t\t\t{tax}\n\n')
    if ee_var6.get() != '$ 0':
        textrecript.insert(END, f'Subtotal\t\t\t{totalcost}\n\n')
    textrecript.insert(END, '\n\n****************************************\n')
    textrecript.insert(END, '\t\tThank you for visiting\n')
 
 
def total():
    global totalcost, tax, subtotal
    item1 = int(esticks.get())
    item2 = int(efries.get())
    item3 = int(efingers.get())
    item4 = int(esoup.get())
    item5 = int(ewedges.get())
    item6 = int(erings.get())
    item7 = int(echeeseburger.get())
    item8 = int(estroanoff.get())
    item9 = int(echilli.get())
    item10 = int(epounder.get())
    item11 = int(efourcheese.get())
    item12 = int(eswiss.get())
    item13 = int(ebits.get())
    item14 = int(ecream.get())
    item15 = int(epepper.get())
    item16 = int(eonions.get())
    item17 = int(esauce.get())
    item18 = int(esourcream.get())
 
    priceofsnakes=(item1*5)+(item2*8)+(item3*6)+(item4*9)+(item5*5)+(item6*7)
    priceofburgers=(item7*7)+(item8*6)+(item9*6)+(item10*6)+(item11*7)+(item12*7)
    priceoftoppings=(item13*4)+(item14*3)+(item15*3)+(item16*4)+(item17*3)+(item18*3)
 
    ee_var1.set('$ ' + str(priceofsnakes))
    ee_var2.set('$ ' + str(priceofburgers))
    ee_var3.set('$ ' + str(priceoftoppings))
 
    subtotal=priceofsnakes+priceofburgers+priceoftoppings
    ee_var4.set('$ '+str(subtotal))
 
    tax=subtotal*0.18
    ee_var5.set('$ ' + str(tax))
 
    totalcost=subtotal+tax
    ee_var6.set('$ ' + str(totalcost))
 
def sticks():
    global e_var1
    if var1.get()==1:
        esticks.config(state=NORMAL)
        esticks.delete(0,END)
        esticks.focus()
    else:
        esticks.config(state=DISABLED)
        e_var1.set('0')
 
def fries():
    if var2.get()==1:
        efries.config(state=NORMAL)
        efries.delete(0,END)
        efries.focus()
    else:
        efries.config(state=DISABLED)
        e_var2.set('0')
 
def fingers():
    if var3.get()==1:
        efingers.config(state=NORMAL)
        efingers.delete(0,END)
        efingers.focus()
    else:
        efingers.config(state=DISABLED)
        e_var3.set('0')
 
def soup():
    if var4.get()==1:
        esoup.config(state=NORMAL)
        esoup.delete(0,END)
        esoup.focus()
    else:
        esoup.config(state=DISABLED)
        e_var4.set('0')
 
def wedges():
    if var5.get()==1:
        ewedges.config(state=NORMAL)
        ewedges.delete(0,END)
        ewedges.focus()
    else:
        ewedges.config(state=DISABLED)
        e_var5.set('0')
 
def rings():
    if var6.get()==1:
        erings.config(state=NORMAL)
        erings.delete(0,END)
        erings.focus()
    else:
        erings.config(state=DISABLED)
        e_var6.set('0')
 
def cheeseburger():
    if var7.get()==1:
        echeeseburger.config(state=NORMAL)
        echeeseburger.delete(0,END)
        echeeseburger.focus()
    else:
        echeeseburger.config(state=DISABLED)
        e_var7.set('0')
 
def stroanoff():
    if var8.get()==1:
        estroanoff.config(state=NORMAL)
        estroanoff.delete(0,END)
        estroanoff.focus()
    else:
        estroanoff.config(state=DISABLED)
        e_var8.set('0')
 
def chilli():
    if var9.get()==1:
        echilli.config(state=NORMAL)
        echilli.delete(0,END)
        echilli.focus()
    else:
        echilli.config(state=DISABLED)
        pounder.set('0')
 
def pounder():
    if var10.get()==1:
        epounder.config(state=NORMAL)
        epounder.delete(0,END)
        epounder.focus()
    else:
        epounder.config(state=DISABLED)
        e_var10.set('0')
 
def fourcheese():
    if var11.get()==1:
        efourcheese.config(state=NORMAL)
        efourcheese.delete(0,END)
        efourcheese.focus()
    else:
        efourcheese.config(state=DISABLED)
        e_var11.set('0')
 
def swiss():
    if var12.get()==1:
        eswiss.config(state=NORMAL)
        eswiss.delete(0,END)
        eswiss.focus()
    else:
        eswiss.config(state=DISABLED)
        e_var12.set('0')
 
def bits():
    if var13.get()==1:
        ebits.config(state=NORMAL)
        ebits.delete(0,END)
        ebits.focus()
    else:
        ebits.config(state=DISABLED)
        e_var13.set('0')
 
def cream():
    if var14.get()==1:
        ecream.config(state=NORMAL)
        ecream.delete(0,END)
        ecream.focus()
    else:
        ecream.config(state=DISABLED)
        e_var14.set('0')
 
def pepper():
    if var15.get()==1:
        epepper.config(state=NORMAL)
        epepper.delete(0,END)
        epepper.focus()
    else:
        epepper.config(state=DISABLED)
        e_var15.set('0')
 
def onions():
    if var16.get()==1:
        eonions.config(state=NORMAL)
        eonions.delete(0,END)
        eonions.focus()
    else:
        eonions.config(state=DISABLED)
        e_var16.set('0')
 
def sauce():
    if var17.get()==1:
        esauce.config(state=NORMAL)
        esauce.delete(0,END)
        esauce.focus()
    else:
        esauce.config(state=DISABLED)
        e_var17.set('0')
 
def sourcream():
    if var18.get()==1:
        esourcream.config(state=NORMAL)
        esourcream.delete(0,END)
        esourcream.focus()
    else:
        esourcream.config(state=DISABLED)
        e_var18.set('0')
 
 
 
#main frames.
main_frame=Frame(root,bd=5,relief=RIDGE)
main_frame.grid(row=1,column=0)
menu_frame=Frame(main_frame,bd=5,relief=RIDGE)
menu_frame.grid(row=1,column=0)
 
billing_frame=Frame(main_frame,bd=5,relief=RIDGE)
billing_frame.grid(row=1,column=1)
 
heading_frame=Frame(root,bd=5,relief=RIDGE)
heading_frame.grid(row=0,column=0)
 
#heading
 
heading_label=Label(heading_frame,text='WELCOME',font=('arial',30,'bold'),fg='red',width=27).pack()
#inframes
snakes_frame=LabelFrame(menu_frame,text='APPETIZERS AND SNACKS',fg='red',bd=4,relief=RIDGE,padx=18)
snakes_frame.pack(side=TOP)
burger_frame=LabelFrame(menu_frame,text='GOURMET BURGERS',fg='red',bd=4,relief=RIDGE)
burger_frame.pack(side=TOP)
toppings_frame=LabelFrame(menu_frame,text='BURGER TOPPNGS',fg='red',bd=4,relief=RIDGE,padx=22)
toppings_frame.pack(side=TOP)
 
text_frame=Frame(billing_frame,bd=4,relief=RIDGE)
text_frame.pack(side=TOP)
cost_frame=Frame(billing_frame,bd=4,relief=RIDGE)
cost_frame.pack(side=TOP)
button_frame=Frame(billing_frame,bd=4,relief=RIDGE)
button_frame.pack(side=TOP)
 
 
#variables
var1 = IntVar()
var2 = IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
 
e_var1=StringVar()
e_var2=StringVar()
e_var3=StringVar()
e_var4=StringVar()
e_var5=StringVar()
e_var6=StringVar()
e_var7=StringVar()
e_var8=StringVar()
e_var9=StringVar()
e_var10=StringVar()
e_var11=StringVar()
e_var12=StringVar()
e_var13=StringVar()
e_var14=StringVar()
e_var15=StringVar()
e_var16=StringVar()
e_var17=StringVar()
e_var18=StringVar()
 
e_var1.set('0')
e_var2.set('0')
e_var3.set('0')
e_var4.set('0')
e_var5.set('0')
e_var6.set('0')
e_var7.set('0')
e_var8.set('0')
e_var9.set('0')
e_var10.set('0')
e_var11.set('0')
e_var12.set('0')
e_var13.set('0')
e_var14.set('0'),
e_var15.set('0')
e_var16.set('0')
e_var17.set('0')
e_var18.set('0')
 
 
#text variables for the total cost
 
ee_var1=StringVar()
ee_var2=StringVar()
ee_var3=StringVar()
ee_var4=StringVar()
ee_var5=StringVar()
ee_var6=StringVar()
 
#ing in snacks
 
sticks=Checkbutton(snakes_frame,text='Mozzarella Sticks',onvalue=1,offvalue=0,variable=var1,command=sticks)
sticks.grid(row=0,column=0,sticky=W)
fries=Checkbutton(snakes_frame,text='French Fries',onvalue=1,offvalue=0,variable=var2,command=fries)
fries.grid(row=1,column=0,sticky=W)
fingers=Checkbutton(snakes_frame,text='Chicken Fingers',onvalue=1,offvalue=0,variable=var3,command=fingers)
fingers.grid(row=2,column=0,sticky=W)
soup=Checkbutton(snakes_frame,text='Brocoli Cheddar Soup',onvalue=1,offvalue=0,variable=var4,command=soup )
soup.grid(row=3,column=0,sticky=W)
wedges=Checkbutton(snakes_frame,text='Potato Wedges',onvalue=1,offvalue=0,variable=var5,command=wedges)
wedges.grid(row=4,column=0,sticky=W)
rings=Checkbutton(snakes_frame,text='Churly onion rings',onvalue=1,offvalue=0,variable=var6,command=rings)
rings.grid(row=5,column=0,sticky=W)
 
 
lsticks=Label(snakes_frame,text='$5').grid(row=0,column=1)
lfries=Label(snakes_frame,text='$8').grid(row=1,column=1)
lfingers=Label(snakes_frame,text='$6').grid(row=2,column=1)
lsoup=Label(snakes_frame,text='$9').grid(row=3,column=1)
lwedges=Label(snakes_frame,text='$5').grid(row=4,column=1)
lrings=Label(snakes_frame,text='$7').grid(row=5,column=1)
 
esticks=Entry(snakes_frame,state=DISABLED,textvariable=e_var1)
esticks.grid(row=0,column=2)
 
efries=Entry(snakes_frame,state=DISABLED,textvariable=e_var2)
efries.grid(row=1,column=2)
efingers=Entry(snakes_frame,state=DISABLED,textvariable=e_var3)
efingers.grid(row=2,column=2)
esoup=Entry(snakes_frame,state=DISABLED,textvariable=e_var4)
esoup.grid(row=3,column=2)
ewedges=Entry(snakes_frame,state=DISABLED,textvariable=e_var5)
ewedges.grid(row=4,column=2)
erings=Entry(snakes_frame,state=DISABLED,textvariable=e_var6)
erings.grid(row=5,column=2)
 
 
#ing in burgers
 
cheeseburger=Checkbutton(burger_frame,text='Cheese Burger',onvalue=1,offvalue=0,variable=var7,command=cheeseburger)
cheeseburger.grid(row=0,column=0,sticky=W)
stroanoff=Checkbutton(burger_frame,text='Stroanoff',onvalue=1,offvalue=0,variable=var8,command=stroanoff)
stroanoff.grid(row=1,column=0,sticky=W)
chilli=Checkbutton(burger_frame,text='Vegetable Chilli',onvalue=1,offvalue=0,variable=var9,command=chilli)
chilli.grid(row=2,column=0,sticky=W)
pounder=Checkbutton(burger_frame,text='Four Cheese',onvalue=1,offvalue=0,variable=var10,command=pounder)
pounder.grid(row=3,column=0,sticky=W)
fourcheese=Checkbutton(burger_frame,text='Quater Pounder with cheese',onvalue=1,offvalue=0,variable=var11,command=fourcheese)
fourcheese.grid(row=4,column=0,sticky=W)
swiss=Checkbutton(burger_frame,text='Mashroom Swiss',onvalue=1,offvalue=0,variable=var12,command=swiss)
swiss.grid(row=5,column=0,sticky=W)
 
lcheeseburger=Label(burger_frame,text='$7').grid(row=0,column=1)
lstroanoff=Label(burger_frame,text='$6').grid(row=1,column=1)
lchilli=Label(burger_frame,text='$6').grid(row=2,column=1)
lpounder=Label(burger_frame,text='$6').grid(row=3,column=1)
lfourcheese=Label(burger_frame,text='$7').grid(row=4,column=1)
lswiss=Label(burger_frame,text='$7').grid(row=5,column=1)
 
echeeseburger=Entry(burger_frame,state=DISABLED,textvariable=e_var7)
echeeseburger.grid(row=0,column=2)
estroanoff=Entry(burger_frame,state=DISABLED,textvariable=e_var8)
estroanoff.grid(row=1,column=2)
echilli=Entry(burger_frame,state=DISABLED,textvariable=e_var9)
echilli.grid(row=2,column=2)
epounder=Entry(burger_frame,state=DISABLED,textvariable=e_var10)
epounder.grid(row=3,column=2)
efourcheese=Entry(burger_frame,state=DISABLED,textvariable=e_var11)
efourcheese.grid(row=4,column=2)
eswiss=Entry(burger_frame,state=DISABLED,textvariable=e_var12)
eswiss.grid(row=5,column=2)
#ing in toppings
 
bits=Checkbutton(toppings_frame,text='Chicken bits',onvalue=1,offvalue=0,variable=var13,command=bits)
bits.grid(row=0,column=0,sticky=W)
cream=Checkbutton(toppings_frame,text='Cream Cheese',onvalue=1,offvalue=0,variable=var14,command=cream)
cream.grid(row=1,column=0,sticky=W)
pepper=Checkbutton(toppings_frame,text='Roasted Red pepper',onvalue=1,offvalue=0,variable=var15,command=pepper)
pepper.grid(row=2,column=0,sticky=W)
onions=Checkbutton(toppings_frame,text='Caramilized Onions',onvalue=1,offvalue=0,variable=var16,command=onions)
onions.grid(row=3,column=0,sticky=W)
sauce=Checkbutton(toppings_frame,text='Cranny berry sauce',onvalue=1,offvalue=0,variable=var17,command=sauce)
sauce.grid(row=4,column=0,sticky=W)
sourcream=Checkbutton(toppings_frame,text='Sour Cream',onvalue=1,offvalue=0,variable=var18,command=sourcream)
sourcream.grid(row=5,column=0,sticky=W)
 
lbits=Label(toppings_frame,text='$4').grid(row=0,column=1)
lcream=Label(toppings_frame,text='$3').grid(row=1,column=1)
lpepper=Label(toppings_frame,text='$3').grid(row=2,column=1)
lonions=Label(toppings_frame,text='$4').grid(row=3,column=1)
lsause=Label(toppings_frame,text='$3').grid(row=4,column=1)
lsourcream=Label(toppings_frame,text='$3').grid(row=5,column=1)
 
ebits=Entry(toppings_frame,state=DISABLED,textvariable=e_var13)
ebits.grid(row=0,column=2)
ecream=Entry(toppings_frame,state=DISABLED,textvariable=e_var14)
ecream.grid(row=1,column=2)
epepper=Entry(toppings_frame,state=DISABLED,textvariable=e_var15)
epepper.grid(row=2,column=2)
eonions=Entry(toppings_frame,state=DISABLED,textvariable=e_var16)
eonions.grid(row=3,column=2)
esauce=Entry(toppings_frame,state=DISABLED,textvariable=e_var17)
esauce.grid(row=4,column=2)
esourcream=Entry(toppings_frame,state=DISABLED,textvariable=e_var18)
esourcream.grid(row=5,column=2)
 
 
#cost lables and entry fields
lcostofsnakes=Label(cost_frame,text='COST OF SNACKS',fg='red',padx=55).grid(row=0,column=0)
lcostofburgers=Label(cost_frame,text='COST OF BURGERS',fg='red',padx=55).grid(row=1,column=0)
lcostoftoppings=Label(cost_frame,text='COST OF TOPPINGS',fg='red').grid(row=2,column=0)
lcostofsutotal=Label(cost_frame,text='SUB TOTAL',fg='red').grid(row=3,column=0)
lcostoftax=Label(cost_frame,text='TAX AMOUNT',fg='red').grid(row=4,column=0)
lcostoftotal=Label(cost_frame,text='TOTAL AMOUNT',fg='red').grid(row=5,column=0)
 
 
tcostofsnakes=Entry(cost_frame,state='readonly',textvariable=ee_var1).grid(row=0,column=1)
tcostofburgers=Entry(cost_frame,state='readonly',textvariable=ee_var2).grid(row=1,column=1)
tcostoftoppings=Entry(cost_frame,state='readonly',textvariable=ee_var3).grid(row=2,column=1)
tcostofsubtotal=Entry(cost_frame,state='readonly',textvariable=ee_var4).grid(row=3,column=1)
tcostoftax=Entry(cost_frame,state='readonly',textvariable=ee_var5).grid(row=4,column=1)
tcostoftotal=Entry(cost_frame,state='readonly',textvariable=ee_var6).grid(row=5,column=1)
 
#buttons
btotal=Button(button_frame,text='TOTAL',width=16,padx=25,command=total).grid(row=0,column=0)
brecipt=Button(button_frame,text='BILL',width=16,padx=25,command=receipt).grid(row=1,column=0)
breset=Button(button_frame,text='RESET',width=16,padx=25).grid(row=0,column=1)
bsave=Button(button_frame,text='SAVE',width=16,padx=25,command=save).grid(row=1,column=1)
brecipt=Button(button_frame,text='RECIPTS',width=16,padx=25,command=receiptsfile).grid(row=2,column=0)
babout=Button()
#text area
textrecript=Text(text_frame,bd=3,width=40,height=20)
textrecript.grid(row=0,column=0)
 
root.mainloop()
