from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

op = ''
pricom = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
pridr = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
prides = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]



def clic_button(num):
    global op
    op = op + num
    vical.delete(0,END)
    vical.insert(END, op)

def delete():
    global op
    op = ''
    vical.delete(0,END)

def result():
    global op
    res =str(eval(op))
    vical.delete(0,END)
    vical.insert(0, res)
    op = ''

def check():
    x = 0
    for d in numdr:
        if vardr[x].get() == 1:
            numdr[x].config(state=NORMAL)
            if numdr[x].get() == '0':
                numdr[x].delete(0,END)
            numdr[x].focus()
        else:
            numdr[x].config(state=DISABLED)
            drtext[x].set('0')
        x+=1

    x = 0
    for c in numdes:
        if vardes[x].get() == 1:
            numdes[x].config(state=NORMAL)
            if numdes[x].get() == '0':
                numdes[x].delete(0,END)
            numdes[x].focus()
        else:
            numdes[x].config(state=DISABLED)
            destext[x].set('0')
        x+=1
    
    x = 0
    for c in numfo:
        if varfo[x].get() == 1:
            numfo[x].config(state=NORMAL)
            if numfo[x].get() == '0':
                numfo[x].delete(0,END)
            numfo[x].focus()
        else:
            numfo[x].config(state=DISABLED)
            fotext[x].set('0')
        x+=1

def total():
    subcom = 0
    i = 0
    for c in fotext:
        subcom = subcom + (float(c.get()) * pricom[i])
        i+=1
    

    subdr = 0
    i = 0
    for d in drtext:
        subdr = subdr + (float(d.get()) * pridr[i])
        i+=1
  

    subdes = 0
    i = 0
    for de in destext:
        subdes = subdes + (float(de.get()) * prides[i])
        i+=1
    sub = subcom + subdr + subdes
    iva = sub * .16
    total = sub + iva
    varcostcom.set(f'${round(subcom,2)}')
    varcostdr.set(f'${round(subdr,2)}')
    varcostdes.set(f'${round(subdes,2)}')
    varsub.set(f'${round(sub,2)}')
    variva.set(f'${round(iva,2)}')
    vartotal.set(f'${round(total,2)}')
    
def ticket():
    texticket.delete(1.0,END)
    numticket = f'N# - {random.randint(1000,9999)}'
    date = datetime.datetime.now()
    date_ticket = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    texticket.insert(END, f'Datos:\t{numticket}\t\t{date_ticket}\n')    
    texticket.insert(END, f'*'* 61 + '\n')
    texticket.insert(END, 'Items\t\tCount.\titems cost\n')
    texticket.insert(END, f'-'*73+'\n')
    x = 0 
    for c in fotext:
        if c.get() != '0':
            texticket.insert(END, f'{listFo[x]}\t\t{c.get()}\t'
                             f'$ {int(c.get()) * pricom[x]}\n')
        x+=1
    x = 0
    for d in drtext:
        if d.get() != '0':
            texticket.insert(END, f'{listDri[x]}\t\t{d.get()}\t'
                             f'$ {int(d.get()) * pridr[x]}\n')
        x+=1
    x = 0
    for de in destext:
        if de.get() != '0':
            texticket.insert(END, f'{listDes[x]}\t\t{de.get()}\t'
                             f'$ {int(de.get()) * prides[x]}\n')
        x+=1
    texticket.insert(END, f'-'*73+'\n')
    texticket.insert(END,f' Food cost: \t\t\t{varcostcom.get()}\n')
    texticket.insert(END,f' Drinks cost: \t\t\t{varcostdr.get()}\n')
    texticket.insert(END,f' Desert cost: \t\t\t{varcostdes.get()}\n')
    texticket.insert(END, f'-'* 73 +'\n')
    texticket.insert(END,f' Sub-total: \t\t\t{varsub.get()}\n')
    texticket.insert(END,f' IVA: \t\t\t{variva.get()}\n')
    texticket.insert(END,f' Total: \t\t\t{vartotal.get()}\n')
    texticket.insert(END, f'-'* 73 +'\n')
    texticket.insert(END,f'Lo esperamos Pronto!')

def save():
    infoticket = texticket.get(1.0,END)
    arch = filedialog.asksaveasfile(mode='w', defaultextension='txt')
    arch.write(infoticket)
    arch.close()
    messagebox.showinfo('Information', 'the ticket has been saved')

def reset():
    texticket.delete(0.1,END)
    for t in fotext:
        t.set('0')
    for t in drtext:
        t.set('0')
    for t in destext:
        t.set('0')
    for c in numfo:
        c.config(state=DISABLED)
    for d in numdr:
        d.config(state=DISABLED)
    for de in numdes:
        de.config(state=DISABLED)
    for v in varfo:
        v.set(0)
    for v in vardr:
        v.set(0)
    for v in vardes:
        v.set(0)
    varcostcom.set('')
    varcostdr.set('')
    varcostdes.set('')
    varsub.set('')
    variva.set('')
    vartotal.set('')

#iniciar tkinter
app = Tk()


# size of window
app.geometry('1300x560+0+0')

#avoid max
app.resizable(0,0)

# title of the window
app.title("My restaurant - Billing system")

# background color
app.config(bg='burlywood')


#superior panel
pansup = Frame(app, bd=1, relief=FLAT)
pansup.pack(side=TOP)

#title 
titleeti = Label(pansup, text='Billing System',fg='azure4',
                 font=('Dosis',58),bg='burlywood',width=28)
titleeti.grid(row=0,column=0)

# Panel izquierdo
panizq = Frame(app,bd=1,relief=FLAT)
panizq.pack(side=LEFT)

# Costs panel
pancost = Frame(panizq,bd=1,relief=FLAT,bg='azure4',padx=140)
pancost.pack(side=BOTTOM)

# Food panel
pancom = LabelFrame(panizq,text='Food',font=('Dosis',19,'bold'),
                    bd=1, relief=FLAT, fg='azure4')
pancom.pack(side=LEFT)

# Drinks panel
pandr = LabelFrame(panizq,text='Drinks',font=('Dosis',19,'bold'),
                    bd=1, relief=FLAT, fg='azure4')
pandr.pack(side=LEFT)

# Desert panel
pandes = LabelFrame(panizq,text='Desert',font=('Dosis',19,'bold'),
                    bd=1, relief=FLAT, fg='azure4')
pandes.pack(side=LEFT)

# right panel
pander =Frame(app,bd=1,relief=FLAT)
pander.pack(side=RIGHT)

# calculator panel
pancal = Frame(pander,bd=1,relief=FLAT, bg='burlywood')
pancal.pack()

# ticket panel
pantic = Frame(pander,bd=1,relief=FLAT, bg='burlywood')
pantic.pack()

# buttons panel
panbot = Frame(pander,bd=1,relief=FLAT, bg='burlywood')
panbot.pack()

# Products lists
listFo=['Pollo','Cordero','Bistek','Pizza','Sushi','Lasagna','Pasta','Carnitas']
listDri = ['Agua','Refresco','Jugo','Limonada','Naranjada','Vino','Corona','Heineken']
listDes = ['icecream','fruit','brownies','flan','cheesecake','pastel chocolate','jericaya','chocoflan']

# gen food items
varfo = []
numfo = []
fotext = []
count = 0

for f in listFo:

    #create checkbutton
    varfo.append('')
    varfo[count] = IntVar()
    f = Checkbutton(pancom,
                    text=f.title(),
                    font=('Dosis',19,'bold'),
                    onvalue=1,
                    offvalue=0,
                    variable=varfo[count],
                    command=check)

    f.grid(row=count,
           column=0, 
           sticky=W)

    #create num of entry
    numfo.append('')
    fotext.append('')
    fotext[count] = StringVar()
    fotext[count].set('0')
    numfo[count] = Entry(pancom,
                         font=('Dosis',18,'bold'),
                         bd=1,
                         width=6,
                         state=DISABLED,
                         textvariable=fotext[count])
    numfo[count].grid(row=count,
                       column=1)
    count += 1

# gen drinks items
vardr = []
numdr = []
drtext = []
count = 0

for d in listDri:
    vardr.append('')
    vardr[count] = IntVar()
    d = Checkbutton(pandr,
                    text=d.title(),
                    font=('Dosis',19,'bold'),
                    onvalue=1,
                    offvalue=0,
                    variable=vardr[count],
                    command=check)

    d.grid(row=count,
           column=0, 
           sticky=W)
    
    #create num of entry
    numdr.append('')
    drtext.append('')
    drtext[count] = StringVar()
    drtext[count].set('0')
    numdr[count] = Entry(pandr,
                         font=('Dosis',18,'bold'),
                         bd=1,
                         width=6,
                         state=DISABLED,
                         textvariable=drtext[count])
    numdr[count].grid(row=count,
                       column=1)

    count += 1

# gen deserts items
vardes = []
numdes = []
destext = []
count = 0

for de in listDes:
    vardes.append('')
    vardes[count] = IntVar()
    de = Checkbutton(pandes,
                     text=de.title(),
                     font=('Dosis',19,'bold'),
                    onvalue=1,
                    offvalue=0,
                    variable=vardes[count],
                    command=check)

    de.grid(row=count,column=0, sticky=W)

    #create num of entry
    numdes.append('')
    destext.append('')
    destext[count] = StringVar()
    destext[count].set('0')
    numdes[count] = Entry(pandes,
                         font=('Dosis',18,'bold'),
                         bd=1,
                         width=6,
                         state=DISABLED,
                         textvariable=destext[count])
    numdes[count].grid(row=count,
                       column=1)

    count += 1



#variables
varcostcom = StringVar()
varcostdes = StringVar()
varcostdr = StringVar()
varsub = StringVar()
variva = StringVar()
vartotal = StringVar()

# etiquets of costs and num of entry
etcoscom = Label(pancost,
                 text='Food cost',
                 font=('Dosis',12,'bold'),
                 bg='azure4',
                 fg='white')
etcoscom.grid(row=0,column=0)
textcoscom = Entry(pancost,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=varcostcom)
textcoscom.grid(row=0,column=1,padx=41)

etcosdr = Label(pancost,
                 text='Drink cost',
                 font=('Dosis',12,'bold'),
                 bg='azure4',
                 fg='white')
etcosdr.grid(row=1,column=0)
textcosdr = Entry(pancost,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=varcostdr)
textcosdr.grid(row=1,column=1,padx=41)

etcosdes = Label(pancost,
                 text='Desert cost',
                 font=('Dosis',12,'bold'),
                 bg='azure4',
                 fg='white')
etcosdes.grid(row=2,column=0)
textcosdes = Entry(pancost,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=varcostdes)
textcosdes.grid(row=2,column=1,padx=41)

etsub = Label(pancost,
                 text='Subtotal',
                 font=('Dosis',12,'bold'),
                 bg='azure4',
                 fg='white')
etsub.grid(row=0,column=2)
textsub = Entry(pancost,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=varsub)
textsub.grid(row=0,column=3,padx=41)

etiva = Label(pancost,
                 text='IVA',
                 font=('Dosis',12,'bold'),
                 bg='azure4',
                 fg='white')
etiva.grid(row=1,column=2)
textiva = Entry(pancost,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=variva)
textiva.grid(row=1,column=3,padx=41)

ettot = Label(pancost,
                 text='Total',
                 font=('Dosis',12,'bold'),
                 bg='azure4',
                 fg='white')
ettot.grid(row=2,column=2)
textot = Entry(pancost,
                   font=('Dosis',12,'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=vartotal)
textot.grid(row=2,column=3,padx=41)

# buttons
buttons = ['total','ticket','save','reset']
butcreate = []
columns = 0

for b in buttons:
    b = Button(panbot,
               text=b.title(),
               font=('Dosis',14,'bold'),
               fg='white',
               bg='azure4',
               bd=1,
               width=9)
    butcreate.append(b)
    b.grid(row=0,
           column=columns)
    columns+=1

butcreate[0].config(command=total)
butcreate[1].config(command=ticket)
butcreate[2].config(command=save)
butcreate[3].config(command=reset)





# ticket
texticket = Text(pantic,
                 font=('Dosis',12,'bold'),
                 bd=1,
                 width=54,
                 height=12)
texticket.grid(row=0,
               column=0)

# Calculator
vical = Entry(pancal,
              font=('Dosis',16,'bold'),
              width=42,
              bd=1)
vical.grid(row=0,
           column=0,
           columnspan=4)

butcal =['7','8','9','+',
         '4','5','6','-',
         '1','2','3','x',
         'CE','Del','0','/']
butsave = []

r = 1
c = 0
for b in butcal:
    b = Button(pancal,
               text=b.title(),
               font=('Dosis',16,'bold'),
               fg='white',
               bg='azure4',
               bd=1,
               width=9)
    butsave.append(b)
    b.grid(row=r,column=c)

    if c == 3:
        r +=1
    c +=1
    if c == 4:
        c = 0
butsave[0].config(command=lambda: clic_button('7'))
butsave[1].config(command=lambda: clic_button('8'))
butsave[2].config(command=lambda: clic_button('9'))
butsave[3].config(command=lambda: clic_button('+'))
butsave[4].config(command=lambda: clic_button('4'))
butsave[5].config(command=lambda: clic_button('5'))
butsave[6].config(command=lambda: clic_button('6'))
butsave[7].config(command=lambda: clic_button('-'))
butsave[8].config(command=lambda: clic_button('1'))
butsave[9].config(command=lambda: clic_button('2'))
butsave[10].config(command=lambda: clic_button('3'))
butsave[11].config(command=lambda: clic_button('*'))
butsave[12].config(command=result)
butsave[13].config(command=delete)
butsave[14].config(command=lambda: clic_button('0'))
butsave[15].config(command=lambda: clic_button('/'))





# Avoid that the loop close
app.mainloop()

