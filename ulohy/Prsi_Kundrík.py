import tkinter
import random


canvas=tkinter.Canvas(width=1000,height=900,bg="grey")
canvas.pack()
canvas.create_rectangle(0,700,1000,900,fill="green",outline="green")
c="blue"
k=15
e=0
def acid(event):
    global c
    c="light green"
def normal(event):
    global c
    c="blue"
def plus(event):
    global k
    k=k+1
def minus(event):
    global k
    k=k-1
    if k<=1:
        k=3
class Rain:
    def __init__(self,name,length,thick,speed,xposition):
        self.name=name
        self.length=length
        self.thick=thick
        self.speed=speed
        self.xposition=xposition
    def move(self,y,f):
        canvas.delete(self.name)
        s=k+self.speed
        x,l,t=self.xposition,self.length,self.thick
        if y+s>=950:
            y=f
        if e==0:
            canvas.create_line(x,y,x,y+l,fill=c,width=t,tag=self.name)
            canvas.after(25,func=lambda: self.move(y+s,f))
        if e==1:
            s=1+self.speed
            canvas.create_line(x,y,x,y+2*l,fill="white",width=t,tag=self.name)
            canvas.create_line(x-l,y+l,x+l,y+l,fill="white",width=t,tag=self.name)
            canvas.after(25,func=lambda: self.move(y+s,f))

def snow(event):
    global e
    e=1
    canvas.create_rectangle(0,700,1000,900,fill="white",outline="white")
def rain(event):
    global e
    e=0
    canvas.create_rectangle(0,700,1000,900,fill="green",outline="green")
canvas.bind_all("<Left>",acid)
canvas.bind_all("<Right>",normal)
canvas.bind_all("<Up>",plus)
canvas.bind_all("<Down>",minus)
canvas.bind_all("s",snow)
canvas.bind_all("r",rain)

for i in range(300):
    n="k"+str(i)
    kvapka=Rain(n,random.randint(5,10),random.randrange(1,5)
                ,random.randint(0,10),random.randint(10,990))
    kvapka.move(random.randint(0,900),0)


canvas.mainloop()



