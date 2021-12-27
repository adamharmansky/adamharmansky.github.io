from tkinter import *
import random
 
root=Tk()

root.geometry("600x600")

l1=Label(root,font=("Arial",260))
 
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
     
b1=Button(root,text="Hod kockou",foreground='red',command=roll)
b1.place(x=300,y=0)
b1.pack()
 
root.mainloop()
