from tkinter import *

#iniciar tkinter

app = Tk()


# size of window
app.geometry('1220x630+0+0')

#avoid max
app.resizable(0,0)

# title of the window
app.title("My restaurant - Facturation system")

# background color
app.config(bg='burlywood')

# Avoid that the screen close

#superior panel
pansup = Frame(app, bd=1, relief=FLAT)
pansup.pack(side=TOP)

#title 
titleeti = Label(pansup, text='Facturation System',fg='azure4',
                 font=('Dosis',58),bg='burlywood',width=27)
titleeti.grid(row=0,column=0)

# Panel izquierdo
panizq = Frame(app,bd=1,relief=FLAT)
panizq.pack(side=LEFT)

# Costs panel
pancost = Frame(panizq,bd=1,relief=FLAT)
pancost.pack(side=BOTTOM)

# Food panel
pancom = LabelFrame(panizq,text='Food',font=('Dosis',19,'bold'),
                    bd=1, relief=FLAT, fg='azure4')
pancom.pack(side=LEFT)

# Drinks panel
pancom = LabelFrame(panizq,text='Drinks',font=('Dosis',19,'bold'),
                    bd=1, relief=FLAT, fg='azure4')
pancom.pack(side=LEFT)

# Desert panel
pancom = LabelFrame(panizq,text='Desert',font=('Dosis',19,'bold'),
                    bd=1, relief=FLAT, fg='azure4')
pancom.pack(side=LEFT)

# right panel
pander =Frame(app,bg=1,relief=FLAT)
pander.pack(side=RIGHT)

# calculator panel
pancal = Frame(pander,bd=1,relief=FLAT, bg='burlywood')
pancal.pack()

# ticket panel
pantic = Frame(pander,bd=1,relief=FLAT, bg='burlywood')
pantic.pack()

# buttons panel
panbot = Frame(pander,bd=1,relief=FLAT, bg='burlywood')s
panbot.pack()

app.mainloop()

