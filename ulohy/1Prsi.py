#########################################################
#########################################################
###                                                   ###
###                                                   ###
###                                ## ##      ###     ###
###                                 ###      ###      ###
###                                                   ###
###      #######     #######       #####     ###      ###
###      #########   #########   #########   ###      ###
###      ###   ###   ###   ###   ###   ###   ###      ###
###      ###   ###   ###   ###   ###         ###      ###
###      #########   #########   #######     ###      ###
###      #######     ########      #######   ###      ###
###      ###         ######            ###   ###      ###
###      ###         ### ###     ###   ###   ###      ###
###      ###         ###  ###    #########   ###      ###
###      ###         ###   ###     #####     ###      ###
###                                                   ###
###                                                   ###
#########################################################
#########################################################
###                                                   ###
###      #             #   #             #            ###
###      #             #   #                          ###
###      ####  #   #   #####  ###  ####  #  ###       ###
###      #   # #   #   #   # #  #  #   # # #   #      ###
###      ####   ####   #   #  #### ####  #  ###       ###
###                #               #                  ###
###            ####                #                  ###
###                                                   ###
#########################################################
#########################################################

#########################################################
#                  Discord: Hapio#1904                  #
#########################################################

#########################################################
#########################################################
#########################################################
#########################################################

   #
  #
#   #                 #
#   #                 #
#   # #   #  ###   ####
#   #  # #  #   # #   #
 ###    #    ###   ####

#import
from tkinter import *
from random import randint,randrange
from math import sqrt

#premenne
a1=1.6 #plynulost zmeny
a2=40 #cast odtienu
x=801 #rozmer platna
a=x/180 #rozmer pre lahsie pocitanie
sneh=1 #pocasie
opened=1 #pause
ii=70 #pocet vlociek
dele=0 #rusiaci command

#platno
ce=Tk()
ce.title('Prší 1.0.0')
c=Canvas(ce,width=x-2,height=x-2,bg='#000000',bd=0)
c.pack()

#########################################################

#  #               # #
# #
##   # ##  ###     # # # ##   ###
# #  ##   #  #     # # ##  # #  #
#  # #     ####    # # #   #  ####
                #  #
                 ##

class Krajina:

    #init
    def __init__(self,r,g,b):
        self.r,self.g,self.b=r,g,b

    #nejake nasobenie pre tvorenie novych podobnych odtienov farieb
    def ten(self,num,con):
        if con==0:
            return round(9*num/10)
        else:
            return round(11*num/10)

    #premena rgb na hex kod
    def ToHex(self,rgb):
        return "#%02X%02X%02X"%rgb
    
    #tvorba podobnych odtienov od zakladnej farby
    def NewCol(self,rgb,con,i):
        for l in range(len(rgb)):
            if con==0:
                rgb[l]=round(rgb[l]-rgb[l]*i/(x*a1))
            elif con==1:
                rgb[l]=randint(k.ten(rgb[l],0),k.ten(rgb[l],1))
            elif con==2 or 3:
                rgb[l]=k.ten(rgb[l],con-2)
        return rgb[0:3]

    #pozadie (gradient)
    def pozadie(self,r,g,b):
        lc=k.ToHex((r,g,b))
        for i in range(x-a2):
            c.create_line(0,x-i-a2-1,x,x-i-a2-1,fill=lc,tag='krajina')
            rx,gx,bx=k.NewCol([r,g,b],0,i)
            lc=k.ToHex((rx,gx,bx))
    
    #okno
    def okno(self,n,rgb):
        c.create_rectangle((155-3*n)*a,(128-35*n)*a,(137+3*n)*a,(110-29*n)*a,width=0,fill=k.ToHex(rgb),tag='krajina')
        for i in range(2):
            for j in range(2):
                c.create_rectangle((139+i*(8-8*n/3)+7*n/3)*a,(112+j*(8-8*n/3)-89*n/3)*a,(145+i*(8-8*n/3)+n/3)*a,(118+j*(8-8*n/3)-95*n/3)*a,fill='#cccc00',width=0,tag='krajina')

    #komplet celé pozadie
    def krajina(self):
        #pozadie
        self.pozadie(198,231,255) #128,201,255
        #kopce
        if sneh==1:
            c.create_oval(54*a,126*a,270*a,243*a,fill='#e6e6e6',width=0,tag='krajina')
            c.create_oval(-120*a,144*a,144*a,252*a,fill='#eeeeee',width=0,tag='krajina')
        else:
            c.create_oval(54*a,126*a,270*a,243*a,fill='#0b9828',width=0,tag='krajina')
            c.create_oval(-120*a,144*a,144*a,252*a,fill='#139F2F',width=0,tag='krajina')
        #farbydomu
        r1,g1,b1=k.NewCol([self.r,self.g,self.b],1,0)
        r2,g2,b2=k.NewCol([r1,g1,b1],3,0)
        r3,g3,b3=k.NewCol([r1,g1,b1],2,0)
        #horne poschodie
        for i in range(4):
            c.create_polygon((116+10*i)*a,(99-8*i)*a,(176-10*i)*a,(99-8*i)*a,146*a,71*a,fill=k.ToHex((r2,g2,b2)),width=0,tag='krajina')
            (r1,g1,b1),(r2,g2,b2)=(r2,g2,b2),(r1,g1,b1)
        #dolne poschodie
        for i in range(5):
            c.create_line(120*a,(135-8*i)*a,172*a,(135-8*i)*a,fill=k.ToHex((r1,g1,b1)),width=8*a,capstyle='round',tag='krajina')
            (r1,g1,b1),(r2,g2,b2)=(r2,g2,b2),(r1,g1,b1)
        #okna,strecha,verzia
        rc1,rc2='#e6e6e6',k.ToHex((r3,g3,b3))
        for i in range(2):
            k.okno(i,(r3,g3,b3))
            if sneh==1:
                for j in range(2):
                    c.create_line(146*a,(69+2*j)*a,(112+i*68)*a,(99+2*j)*a,fill=rc1,width=4*a,capstyle='round',tag='krajina')
                    rc1,rc2=rc2,rc1
                c.create_text(99*x/100,99.5*x/100,text='v1.0.0',fill='#000000',anchor=SE,font=['Bahnschrift',20,'bold'],tag='krajina')
            else:
                c.create_line(146*a,71*a,(112+i*68)*a,101*a,fill=rc2,width=4*a,capstyle='round',tag='krajina')
                c.create_text(99*x/100,99.5*x/100,text='v1.0.0',fill='#ffffff',anchor=SE,font=['Bahnschrift',20,'bold'],tag='krajina')

#########################################################

#  #                   #
# #                    #
##   #   #  ###  ####  # # #   #
# #   # #  #  #  #   # ##  #   #
#  #   #    #### ####  # #  ####
                 #             #
                 #         ####

class Kvapky:

    #init
    def __init__(self,name,x,y,a,i):
        self.name,self.x,self.y,self.a,self.i=name,x,y,a,i

    #snehova vlocka
    def vlocka(self,x,y,a,tag):
        c.create_line(x,y,x,y-a,fill='#ffffff',tag=tag,capstyle='round',width=a/6)
        c.create_line(x-a/2,y-a/2,x+a/2,y-a/2,fill='#ffffff',tag=tag,capstyle='round',width=a/6)
        sqrta=a/(2*sqrt(2))
        c.create_line(x-sqrta,y-a/2-sqrta,x+sqrta,y-a/2+sqrta,fill='#ffffff',tag=tag,capstyle='round',width=a/6)
        c.create_line(x+sqrta,y-a/2-sqrta,x-sqrta,y-a/2+sqrta,fill='#ffffff',tag=tag,capstyle='round',width=a/6)

    #animacia kvapiek/vlociek
    def animacia(self,ych):
        if(self.y+ych>=x+2):
            ych=0
            self.x=randrange(0,x+2,4)
        c.delete(self.name)
        if sneh==1:
            Kvapky.vlocka(self,self.x,self.y+ych,2*self.a,self.name)
        else:
            c.create_line(self.x,self.y+ych,self.x,self.y-self.a+ych,fill='#006190',width=self.a/4,tag=self.name,capstyle='round')
        if self.i<=ii and dele==0:
            c.after(10,func=lambda: self.animacia(ych+opened*self.a*5/(2+2*sneh)))
        else:
            c.delete(self.name)

    #zaciatok celej animaice
    def run(self):
        global dele,ii
        dele=0
        x,y,a=self.x,self.y,self.a
        if sneh==1:
            Kvapky.vlocka(self,self.x,self.y,2*self.a,self.name)
        else:
            c.create_line(x,y,x,y-a,fill='#6fd0ff',width=a/5,tag=self.name,capstyle='round')
        self.animacia(5*a/4)

    #zaciatok tvorby kvapiek
    def start():
        for i in range(ii):
            kvapka=Kvapky("kvap"+str(i),randrange(0,x+2,4),randrange(0,x+2,4)-600,randint(5,10),i)
            kvapka.run()

#########################################################

#   #        # #                    #  #
## ##         #                    ###
# # #  ###  ##### # ##   ###   ##   #  #
#   # #   #   #   ##  # #   # ####  #  #
#   #  ###  ##### #   #  ###   ##   #  #

#nebol čas urobiť to prehľadnejšie a jednoduchšie, čo už xd

#moznosti(menu)
def Options():
    c.delete('Controlb')
    global opened
    opened=0
    Options.d=Canvas(relief=GROOVE,bd=x/200)
    c.create_window(x/2,x/2,width=9*x/10,height=6*x/10,window=Options.d,tag='Dcan')
    Options.back=Button(Options.d,text='X',font=['Bahnschrift',round(x/25),'bold'],fg='#ffffff',bg='#cc0000',height=1,command=Back,cursor='hand2',anchor=CENTER)
    Options.d.create_window(89*x/100,x/100,anchor=NE,window=Options.back,height=3*x/50,width=3*x/50)
    Options.nazov1=Label(Options.d,compound=TOP,text="Možnosti",font=['Bahnschrift',round(x/25),'bold'],height=1)
    Options.nazov1.pack(pady=x/100)
    Options.e=Canvas()
    Options.d.create_window(4.5*x/10,3*x/10,window=Options.e,tag='buttons')
    Button(Options.e,text="Nastavenia",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Settings).pack(fill=BOTH,padx=20*x/100,pady=x/100)
    Button(Options.e,text="Ovládanie",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Controls).pack(fill=BOTH,padx=20*x/100)
    Button(Options.e,text="Verzie",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Versions).pack(fill=BOTH,padx=20*x/100,pady=x/100)
    
#nastavenia
def Settings():
    Options.d.delete("buttons")
    Options.nazov1.config(text="Nasatavenia")
    Realback()
    Settings.e=Canvas()
    Options.d.create_window(4.5*x/10,3*x/10,window=Settings.e,tag='buttons')
    Button(Settings.e,text="Zmeniť počasie",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Zmena).pack(fill=BOTH,padx=20*x/100,pady=x/100)
    Button(Settings.e,text="Resetovať nastavenia",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Reset).pack(fill=BOTH,padx=20*x/100)

#ovladanie
def Controls():
    Options.d.delete("buttons")
    Options.nazov1.config(text="Ovládanie")
    Realback()
    Controls.e=Canvas()
    Options.d.create_window(4.5*x/10,3*x/10,window=Controls.e,tag='buttons')
    Label(Controls.e,justify=LEFT,anchor=W,text='Otvorenie/Zatvorenie možností\nZníženie intenzity počasia\nZvýšenie intenzity počasia',font=['Bahnschrift',round(x/50)],width=25).pack(side=LEFT)
    Label(Controls.e,justify=LEFT,anchor=E,text='Escape\nŠípka nahor\nŠípka nadol',font=['Bahnschrift',round(x/50)],width=25).pack(side=LEFT)

#verzie
def Versions():
    Options.d.delete("buttons")
    Options.nazov1.config(text="Verzie")
    Realback()
    Versions.e=Canvas()
    Options.d.create_window(4.5*x/10,3*x/10,window=Versions.e,tag='buttons')
    Button(Versions.e,text="Changelog",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Changelog).pack(fill=BOTH,padx=20*x/100,pady=x/100)
    Button(Versions.e,text="Plánované novinky",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Plany).pack(fill=BOTH,padx=20*x/100)

#zmena pocasia
def Zmena():
    Options.d.delete("buttons")
    Options.nazov1.config(text="Zmeniť počasie")
    Realback.realback.config(command=Settings)
    Zmena.e=Canvas()
    Options.d.create_window(4.5*x/10,3.5*x/10,window=Zmena.e,tag='buttons')
    Label(Zmena.e,compound=TOP,text='Vyberte si počasie a potvrďte výber tlačidlom OK:',font=['Bahnschrift',round(x/40),'bold'],height=1).pack(pady=3*x/100)
    Zmena.v=StringVar()
    dazd=Radiobutton(Zmena.e,text="Dážď",value="0",variable=Zmena.v,height=1,indicator=0,cursor='hand2',font=['Bahnschrift',round(x/40),'bold'])
    dazd.pack(fill=BOTH,padx=20*x/100,pady=x/200)
    snezenie=Radiobutton(Zmena.e,text="Sneženie",value="1",variable=Zmena.v,height=1,indicator=0,cursor='hand2',font=['Bahnschrift',round(x/40),'bold'])
    snezenie.pack(fill=BOTH,padx=20*x/100,pady=x/200)
    if sneh==1:
        snezenie.select()
    else:
        dazd.select()
    Button(Zmena.e,text="OK",cursor='hand2',font=['Bahnschrift',round(x/40),'bold'],height=1,command=OK).pack(fill=BOTH,padx=20*x/100,pady=7*x/100)

#potvrdenie zmeny pocasia
def OK():
    global sneh
    if Zmena.v.get()=="1":
        sneh=1
        c.delete("krajina")
        k.krajina()
    else:
        sneh=0
        c.delete("krajina")
        k.krajina()
    Back()

#reset nastaveni
def Reset():
    global sneh,ii,dele
    sneh=1
    c.delete("krajina")
    dele=1
    dele=0
    while ii<70:
        kvapka=Kvapky("kvap"+str(ii),randrange(0,x+2,4),randrange(0,x+2,4)-600,randint(5,10),ii)
        kvapka.run()
        ii+=1
    ii=70
    k.krajina()
    Back()

#changelog
def Changelog():
    Options.d.delete("buttons")
    Options.nazov1.config(text="Changelog")
    Realback.realback.config(command=Versions)
    Changelog.e=Canvas()
    Options.d.create_window(4.5*x/10,3*x/10,window=Changelog.e,tag='buttons')
    Label(Changelog.e,compound=TOP,text='1.0.0:',font=['Bahnschrift',round(x/40),'bold'],height=1).pack(pady=5*x/100)
    Label(Changelog.e,justify=LEFT,text='-Prvá plná verzia\n-Zmeny počasia\n-Zmeny intenzity\n-Pekné pozadie',font=['Bahnschrift',round(x/50)]).pack(padx=20*x/100)

#planovane novinky v novych verziach
def Plany():
    Options.d.delete("buttons")
    Options.nazov1.config(text="Plánované novinky")
    Realback.realback.config(command=Versions)
    Plany.e=Canvas()
    Options.d.create_window(4.5*x/10,3*x/10,window=Plany.e,tag='buttons')
    Label(Plany.e,justify=LEFT,text='-Vietor\n-Pohyby vločiek\n-Lepšia grafika\n-Rôzne pozadia\n-Dostupnejšie nastavenia\n-Farby',font=['Bahnschrift',round(x/50)]).pack(padx=20*x/100)

#tlacidlo "X" (rusi cele menu)
def Back():
    c.create_window(x/100,99*x/100,anchor=SW,window=options,tag='Controlb')
    c.delete('Dcan')
    global opened
    opened=1

#tlacidlo "späť" (vracia sa na povodnu stranku menu)
def Realback():
    Realback.realback=Button(Options.d,text='Späť',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Options,cursor='hand2',anchor=CENTER)
    Options.d.create_window(x/100,x/100,anchor=NW,window=Realback.realback,height=48)

#otvorenie moznosti pomocou gombika
options=Button(text='Možnosti',font=['Bahnschrift',round(x/40),'bold'],height=1,command=Options,cursor='hand2')
c.create_window(x/100,99*x/100,anchor=SW,window=options,tag='Controlb')

#########################################################

#  # #    #
# #  #   #
##   #  ###  #   #  ####  ##  #   #
# #  # #  #   # #  # #   #### #   #
#  # #  ####   #    ####  ##   ####
                                  #
                              ####

#zvysenie intenzity pocasia
def increase(event):
    global ii
    if ii<120:
        Kvapky("kvap"+str(ii),randrange(0,x+2,4),randrange(0,x+2,4)-600,randint(5,10),ii).run()
        ii+=1

#znizenie intenzity pocasia
def decrease(event):
    global ii
    if ii>20:
        ii-=1

#otvaranie/zatvaranie moznosti
def Menuu(event):
    global opened
    if opened==0:
        Options()
        opened=1
    else:
        Back()
        opened=0

#nabindovanie klaves
ce.bind('<Up>',lambda event:increase(event))
ce.bind('<Down>',lambda event:decrease(event))
ce.bind('<Escape>',lambda event:Menuu(event))

#########################################################

 ####                   #              #
#                      ###
 ###  ####  #   #  ##   #   #### # ##  #  ####
    # #   # #   # ####  #  # #   ##  # # # #
####  ####   ####  ##   #   #### #   # #  ####
      #
      #

#definicia farby dreva (velmi podstatne btw)
k=Krajina(121,54,15) #121,54,15
#krajina
k.krajina()
#zatvorenie moznosti pre istotu
Back()
#spustenie animacie
Kvapky.start()
#otvorenie canvasu
ce.mainloop()

#########################################################
#ende
