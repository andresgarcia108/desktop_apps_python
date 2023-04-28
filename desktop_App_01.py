# ------------------
# Desktop App No. 1
# ------------------

#Se importa la librería tkinter con todas su funciones 

from tkinter import * 

# --------------------
# Funciones de la app
# --------------------

# ---------------------------
# Ventana principal de la app
# ---------------------------

# Se declara una variable que adquiere las características de un objeto tk

ventana_Principal = Tk()

# Título de la ventana

ventana_Principal.title("Bandera de Colombia")

#Tamaño de la ventana

ventana_Principal.geometry("500x500")

# Deshabilitar botón de maximizar 

ventana_Principal.resizable(False, False)

# Color de fondo de la ventanaventanaventana

ventana_Principal.config(bg="black")

# ------------------
# Frame amarillo
# ------------------

frame_amarillo = Frame(ventana_Principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0, y=0)
# ------------------
# Frame azul
# ------------------
frame_azul = Frame(ventana_Principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0, y=250)
# ------------------
# Frame rojo
# ------------------

frame_rojo = Frame(ventana_Principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=375)

# Run
ventana_Principal.mainloop()


 