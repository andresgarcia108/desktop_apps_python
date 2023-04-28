from tkinter import *

ventana_Principal = Tk()
ventana_Principal.title("Bandera de Francia")
ventana_Principal.geometry("600x500")

# Frames

frame_azul = Frame(ventana_Principal)
frame_azul.config(bg="blue", width=200, height=500)
frame_azul.place(x=0, y=0)

frame_rojo = Frame(ventana_Principal)
frame_rojo.config(bg="red", width=200, height=500)
frame_rojo.place(x=400, y=0)

ventana_Principal.config(bg="white")

ventana_Principal.mainloop()
