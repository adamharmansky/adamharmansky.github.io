from tkinter import *
import math
import time

degree_mercury = 183.2
degree_venus = 183.2
degree_earth = 183.2
degree_mars = 183.2

window = Tk()
canvas = Canvas(window, width=1920, height=1080,bg="black")
canvas.pack()
center_x=960
center_y=540

orbit_mercury = canvas.create_oval(center_x-155, center_y-130, center_x+145, center_y+170, outline="grey")
mercury = canvas.create_oval(955, 405, 965, 415, fill="grey")
label_mercury = Label(window, text="Merkúr",
                      font=('Arial', 15, 'bold'),
                      fg='grey',
                      bg='black',)
label_mercury.place(x=915, y=670)

orbit_venus = canvas.create_oval(center_x-225, center_y-225, center_x+225, center_y+225, outline="orange")
venus = canvas.create_oval(950, 295, 990, 335, fill="orange", width=2)
label_venus = Label(window, text="Venuša",
                      font=('Arial', 15, 'bold'),
                      fg='orange',
                      bg='black',)
label_venus.place(x=920, y=715)

orbit_earth = canvas.create_oval(center_x-300, center_y-300, center_x+300, center_y+300, outline="blue")
earth = canvas.create_oval(955, 220, 995, 260, fill="blue")
label_earth = Label(window, text="Zem",
                      font=('Arial', 15, 'bold'),
                      fg='blue',
                      bg='black',)
label_earth.place(x=920, y=785)

orbit_mars = canvas.create_oval(center_x-435, center_y-420, center_x+375, center_y+390, outline="red")
mars = canvas.create_oval(940, 110, 960, 130, fill="red")
label_mars = Label(window, text="Mars",
                      font=('Arial', 15, 'bold'),
                      fg='red',
                      bg='black',)
label_mars.place(x=920, y=865)

sun = canvas.create_oval(920, 500, 1000, 580, fill="yellow", width=5)

while True:
    degree_mercury -= 3.83/2
    mercuryToRadian = math.radians(degree_mercury)
    mercuryX = 10/2 * math.cos(mercuryToRadian)
    mercuryY = 10/2 * math.sin(mercuryToRadian)
    canvas.move(mercury, mercuryX, mercuryY)

    degree_venus -= 3.81/4
    venusToRadian = math.radians(degree_venus)
    venusX = 15/4 * math.cos(venusToRadian)
    venusY = 15/4 * math.sin(venusToRadian)
    canvas.move(venus, venusX, venusY)

    degree_earth -= 3.25/6
    earthToRadian = math.radians(degree_earth)
    earthX = 17/6 * math.cos(earthToRadian)
    earthY = 17/6 * math.sin(earthToRadian)
    canvas.move(earth, earthX, earthY)

    degree_mars -= 2.98/8
    marsToRadian = math.radians(degree_mars)
    marsX = 21/8 * math.cos(marsToRadian)
    marsY = 21/8 * math.sin(marsToRadian)
    canvas.move(mars, marsX, marsY)
    window.update()
    time.sleep(0.01)

window.mainloop()
