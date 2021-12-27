import math
import random
import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=800,height=500)
canvas.pack()

def main():
    global kmen,yes
    kmen=tk.Entry(root)
    canvas.create_window(400,460,window=kmen)
    ih=tk.Button(text="Ihličie",command=ihlicie)
    canvas.create_window(380,485,window=ih)
    lis=tk.Button(text="Lístie",command=listy)
    canvas.create_window(420,485,window=lis)

def zmaz(event):
    canvas.delete("all")
    main()

def listy():
    global l
    l=int(kmen.get())
    x=random.randint(30,770)
    y=random.randint(30,450)
    w=x+l/6
    z=y-4*l/3
    canvas.create_rectangle(x,y,x+l/3,y-l,fill="brown",outline="brown")
    canvas.create_oval(w-l/2,z-l/2,w+l/2,z+l/2,fill="green",outline="green")

def ihlicie():
    global l
    l=int(kmen.get())
    x=random.randint(30,770)
    y=random.randint(30,450)
    v=math.sqrt(((l/4)**2) - ((l/8)**2))
    g=x+l/8
    h=y-l-v
    a=(v+2*l/3)/math.tan(1.04719755)
    canvas.create_rectangle(x,y,x+l/4,y-l,fill="brown",outline="brown")
    canvas.create_polygon(g,h,g+a,h+(v+2*l/3),g-a,h+(v+2*l/3),fill="dark green",outline="dark green")
    
main()
canvas.bind_all("z",zmaz)

canvas.mainloop()
root.mainloop()
