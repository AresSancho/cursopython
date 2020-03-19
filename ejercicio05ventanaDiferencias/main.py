'''
ejemplo de un juego basado en una aplicacion
de ventanas con python tkinter.
Para mostrar un ejemplo sobre eventos
y diferentes componentes visuales.
'''
from tkinter import *
import time 
#tkinter esta disponible por defecto en python
#otro recurso muy usado es pyQt5
x = 0
y = 0
tini = time.time()
def click_raton(evento):
    global x, y
    #se pone global para poder usar las variables 
    #x e y definidas fuera de la funcion
    x = evento.x
    y = evento.y
    print("x: " + str(x))
    print("y: " + str(y))
    if x >= 0 and x <= 500 and y >= 0 and y <= 500:
        print("FELICIDADES ADIVINASTE LA PRIMERA DIFERENCIA")
        tfin = time.time()
        tardado = tfin - tini
        print("has tardado en adivinar la primera diferencia: " + str(tardado) +" segundos")
    elif x >= 600 and x <= 664 and y >= 48 and y <= 109:
        print("FELICIDADES ADIVINASTE LA SEGUNDA")
    elif x >= 500 and x <= 555 and y >= 100 and y <= 150:
        print("FELICIDADES ADIVINASTE LA TERCERA")    
    else:
        print("NO HAS ADIVINADO UNA DIFERENCIA")    
    
#end click_raton
ventana = Tk()
canvas = Canvas(ventana, width = 800, height = 600)
canvas.pack(expand = YES, fill = BOTH )
# imagen = PhotoImage(file="imagen2.png")
# canvas.create_image(0,0,image = imagen, anchor = NW)

ventana.geometry("930x360")
ventana.title("PINCHA PARA ADIVINAR LAS DIFERENCIAS A LA DERECHA")
ventana.bind("<Button 1>",click_raton)

ventana.mainloop()