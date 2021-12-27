import tkinter
canvas = tkinter.Canvas(width=1920,height=1080,bg="white")
canvas.pack()

r=10
m=5
f="red"
def zmaz(event):
    canvas.delete("all")

def sh_down(event):
    global r
    if r>1:
        r=r-1
    else:
        r=1
   
def sh_up(event):
    global r
    r=r+1

def gh_up(event):
    global m   
    m=m+1

def gh_down(event):
    global m
    if m>1:
        m=m-1
    else:
        m=1
def magenta(event):
    global f
    f="magenta"
def cyan(event):
    global f
    f="cyan"
def blue(event):
    global f
    f="blue"
def green(event):
    global f
    f="green"
def red(event):
    global f
    f="red"
def yellow(event):
    global f
    f="yellow"
def black(event):
    global f
    f="black"
def orange(event):
    global f
    f="orange"

def kreslenie(self):
    x=self.x
    y=self.y
    canvas.create_oval(x-r,y-r,x+r,y+r,outline=f,fill=f)

def guma(self):
    x=self.x
    y=self.y
    canvas.create_oval(x-m,y-m,x+m,y+m,outline="white",fill="white")

canvas.bind("<B1-Motion>",kreslenie)
canvas.bind("<B3-Motion>",guma)
canvas.bind_all("<Up>",sh_up)
canvas.bind_all("<Down>",sh_down)
canvas.bind_all("<Left>",gh_down)
canvas.bind_all("<Right>",gh_up)
canvas.bind_all("z",zmaz)

canvas.bind_all("b",blue)
canvas.bind_all("g",green)
canvas.bind_all("r",red)
canvas.bind_all("y",yellow)
canvas.bind_all("B",black)
canvas.bind_all("c",cyan)
canvas.bind_all("m",magenta)
canvas.bind_all("o",orange)
canvas.mainloop()
