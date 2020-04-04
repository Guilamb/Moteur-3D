from tkinter import *
from math import *
import time,random
          #le but est de creer un prisme droit rotatif
root = Tk()

global x,y,coordsBASES,coordsCOTES,listaffichage,taille,lumiere,sens,vitesse,brightness,clignote


x,y=pi/2,pi
brightness=1
canvas=Canvas(root,width=1366,height=768)
root.resizable(0,0)
canvas.pack()
coordsBASES=[],[] #0 = bas 1 = haut

ngone=8
vitesse=500
hauteur=300
x=2
taille=10
lumiere=0
sens=1
listeCouleurs=[]
clignote=False
stopit=False


def rotation():
  global sens
  sens*=(-1)

def generationDeCouleurs():
  global listeCouleurs
  listeCouleurs=[]
  for loop in range(50):
    nombre=[0]*3 #creer un tableau
    for x in range(3): 
        for i in range (3): 
            nombre[x]=random.randint(0,255)#gener un nombre aléatoire entre 0 et 255

    for x in range(3):
        nombre[x]=int(nombre[x])#convertis les nombres en int
    
    listeCouleurs.append(nombre)

def oscillationcouleur(listinput):

  listmod=[]
  for loop in range(len(listinput)):
    listmod.append([])
    for n in listinput[loop]:

      listmod[loop].append(int(n*(3/4+cos(lumiere)*1/4)))
      
    tk_rgb = "#%02x%02x%02x" % (listmod[loop][0],listmod[loop][1],listmod[loop][2])

    listmod[loop]=tk_rgb
  return listmod

menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)
menu2 = Menu(menubar, tearoff=0)
menu3 = Menu(menubar, tearoff=0)

menu1.add_command(label="Sens de rotation",command = rotation)
menu1.add_command(label="Couleur",command = generationDeCouleurs)
menu2.add_command(label="A propos")
menu3.add_command(label="Exit", command = root.destroy)


menubar.add_cascade(label="suite", menu = menu1)
menubar.add_cascade(label="Aide", menu = menu2)
menubar.add_cascade(label="Quitter", menu = menu3)


root.config(menu=menubar)
#recuperation de la valeur de facon ponctuelle

def recuperer(x):
  global ngone, vitesse, taille
  ngone=typedepoly.get()
  vitesse=speed.get()
  taille=vartaille.get()

def capt():
  print(canvas.winfo_x())
  ImageGrab.grab((root.winfo_x(),root.winfo_y(),root.winfo_x()+800,root.winfo_y()+800)).save('test.jpg')

def clignotement():
  global clignote
  if clignote==False:
    clignote=True
  elif clignote==True:
    clignote=False

def stop():
  global stopit
  if stopit==False:
    stopit=True
  elif stopit==True:
    stopit=False


typedepoly = Scale(root,orient='horizontal', from_=3, to=50, length=300, variable=ngone, label = "nombre d'angles")
typedepoly.set(3)
typedepoly.place(x=800,y=200)

speed = Scale(root,orient='horizontal', from_=2000, to=1, length=300, variable=vitesse, label = "vitesse")
speed.set(1200)
speed.place(x=800,y=260)

vartaille = Scale(root,orient='horizontal', from_=1, to=500, length=300, variable=taille, label = "taille")
vartaille.set(200)
vartaille.place(x=800,y=310)
sensderotation=0

cadre= Canvas(root,width=300,height=300,bg='beige')
cadre.place(x=800,y=400)

Button(root,text="screenshot",command=capt,width=10).place(x=800,y=400)
Button(root,text="sens",command=rotation,width=10).place(x=900,y=400)
Button(root,text="clignotement",command=clignotement,width=10).place(x=1000,y=400)
Button(root,text="couleur",command=generationDeCouleurs,width=10).place(x=800,y=450)
Button(root,text="stop",command=stop,width=10).place(x=900,y=450)
Button(root,text="quitter",command=root.destroy,width=10).place(x=1000,y=450)

check= Checkbutton(root, command=recuperer, variable=sensderotation)


def creation():

        global x,taille,lumiere, ngone, vitesse, taille,y,codeHexa,listeCouleurs,clignote,stopit
        if clignote==False:
          lumiere=0.1
        elif clignote==True:
          lumiere+=0.1
        oscillationcouleur(listeCouleurs)
        ngone=typedepoly.get()
        vitesse=speed.get()
        taille=vartaille.get()
        if stopit==False:
          x+=pi/(vitesse+0.01)*sens
        elif stopit==True:
          x+=pi/(0+0.01)*sens


        coordsBASES=[],[]
        coordsCOTES=[[] for loop in range(ngone)]

         #generation des couleurs

        for loop in range(0,ngone):
            coordsBASES[0].append([cos(x+loop*pi/(ngone/2))*taille+400])
            coordsBASES[0].append([sin(x+loop*pi/(ngone/2))*taille+400])

        #canvas.create_polygon(coordsBASES[0],fill="cyan")

        for loop in range(0,ngone):
          x0,y0=  ( (cos(x+(loop)*2*pi/ngone)*taille+hauteur))      ,    sin(x+(loop)*2*pi/ngone)*taille+hauteur 

          x1,y1=  ((cos(x+(loop)*2*pi/ngone)*taille+400))           ,        sin(x+(loop)*2*pi/ngone)*taille+400

          x2,y2=  ((cos(x+(loop+1)*2*pi/ngone)*taille+400))        ,      sin(x+(loop+1)*2*pi/ngone)*taille+400

          x3,y3=  ((cos(x+(loop+1)*2*pi/ngone)*taille+hauteur))     ,  sin(x+(loop+1)*2*pi/ngone)*taille+hauteur

          coordsCOTES[loop].append([x0,y0])
          coordsCOTES[loop].append([x1,y1])
          coordsCOTES[loop].append([x2,y2])
          coordsCOTES[loop].append([x3,y3])

          aire=(x0*y1+x1*y2+x2*y3+x3*y0-x1*y0-x2*y1-x3*y2-x0*y3)/2 # application directe de la "formule du lacet de Gauss"

          if aire>0:

            canvas.create_polygon(coordsCOTES[loop],fill=oscillationcouleur(listeCouleurs)[loop])


        for loop in range(ngone):
            coordsBASES[1].append([cos(x+loop*pi/(ngone/2))*taille+hauteur])
            coordsBASES[1].append([sin(x+loop*pi/(ngone/2))*taille+hauteur])

        canvas.create_polygon(coordsBASES[1],    fill="purple")
        cerclex=canvas.create_oval(x0,y0,x0+20,y0+20)
        canvas.update()
        canvas.delete("all")



generationDeCouleurs()
while True:
    creation()
    time.sleep(0.0001)
