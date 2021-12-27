import tkinter
import math
import random

canvas=tkinter.Canvas(width=1000,height=900,bg="black")
canvas.pack()

canvas.create_oval(450,420,510,480,fill="yellow")

uhp=0

class Planet:
    def __init__(self,name,radius,speed,orbit1,orbit2,color):
        self.name=name
        self.radius=radius
        self.speed=speed
        self.orbit1=orbit1
        self.orbit2=orbit2
        self.color=color
    def move(self,angle=0):
        canvas.delete(self.name)
        a,b,r,color=self.orbit1,self.orbit2,self.radius,self.color
        canvas.create_oval(500+a*math.cos(angle)+r,450+b*math.sin(angle)+r,
                           500+a*math.cos(angle)-r,450+b*math.sin(angle)-r,tag=self.name,fill=color)
        canvas.after(25,func=lambda: self.move(angle-self.speed))
    def orbita(self):
        a,b=self.orbit1,self.orbit2
        canvas.create_oval(500-a,450-b,500+a,450+b,outline="white")
        self.move()

class Asteroid:
    def __init__(self,meno,radius,v,orbit3,orbit4):
        self.meno=meno
        self.radius=radius
        self.v=v
        self.orbit3=orbit3
        self.orbit4=orbit4
    def aster(self,uhol):
        canvas.delete(self.meno)
        c,d,s=self.orbit3,self.orbit4,self.radius
        canvas.create_rectangle(500+c*math.cos(uhol)+s,
                                450+d*math.sin(uhol)+s,
                                500+c*math.cos(uhol)-s,
                                450+d*math.sin(uhol)-s,
                                fill="grey",tag=self.meno, outline="grey")
        canvas.after(25,func=lambda: self.aster(uhol-self.v))

def prstenec():
    global uhp 
    canvas.delete("prst")
    canvas.create_line(500+295*math.cos(uhp)+40,
                       450+285*math.sin(uhp),
                       500+295*math.cos(uhp)-40,
                       450+285*math.sin(uhp),tag="prst",width=5,fill="grey")
    uhp=uhp-0.037
    canvas.after(25,prstenec)
    



merkur=Planet("merkur",7,0.23,70,60,"maroon")
merkur.orbita()

venus=Planet("venuša",13,0.13,100,90,"orange")
venus.orbita()

zem=Planet("zem",14,0.1,130,120,"dark blue")
zem.orbita()

mars=Planet("mars",9,0.092,160,150,"red")
mars.orbita()

jupiter=Planet("jupiter",20,0.05,235,225,"red")
jupiter.orbita()

saturn=Planet("saturn",20,0.037,295,285,"yellow")
saturn.orbita()
prstenec()

uran=Planet("uran",17,0.024,345,335,"cyan")
uran.orbita()

neptun=Planet("neptun",18,0.011,395,385,"blue")
neptun.orbita()

pluto=Planet("pluto",6,0.02,465,365,"white")
pluto.orbita()



for i in range(400):
    n="a"+str(i)
    asteroid=Asteroid(n,5,0.03,190+random.randint(-20,20),180+random.randint(-20,20))
    asteroid.aster(2*math.pi*i/300)

canvas.mainloop()


