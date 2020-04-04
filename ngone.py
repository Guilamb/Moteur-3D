from tkinter import *
from math import *

global x

root = Tk()

canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())

ngone = int()
x=0
speed = int( )

coords = []

canvas.pack()

typedepoly = Scale(root,orient='horizontal', from_=3, to=22, length=300, variable=ngone, label = "nombre d'angles")
typedepoly.place(x=800,y=200)

#vitesse = Scale(root, showvalue = 0, orient='vertical', from_=, to=20, length=300, variable= speed, label = "vitesse radiale")
#vitesse.place(x=800,y=160)

def creation():
        ngone=typedepoly.get()
        
        coords=[]
        global x
        x += pi/1000
        for loop in range(ngone):
                try:
                        coords.append([cos(x+loop*pi/(ngone/2))*350+400])
                        coords.append([sin(x+loop*pi/(ngone/2))*350+400])
                except:
                        pass
        #print(coords)
        canvas.create_polygon(coords)
        
        canvas.update()
        canvas.delete("all")
        
while True:
        #vit=vitesse.get()
        creation()
root.mainloop()
        
