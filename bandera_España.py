from tkinter import *
ventana_Principal = Tk()
ventana_Principal.title("Bandera de España")
ventana_Principal.geometry("600x500")

# Frames

frame_rojo = Frame(ventana_Principal)
frame_rojo.config(bg="red", width=600, height=125)
frame_rojo.place(x=0, y=0)

frame_Rojo2 = Frame(ventana_Principal)
frame_Rojo2.config(bg="red", width=600, height=125)
frame_Rojo2.place(x=0, y=375)

frame_Amarillo = Frame(ventana_Principal)
frame_Amarillo.config(bg="yellow",width=600,height=250)
frame_Amarillo.place(x=0, y=125)

cuadradozzz = Frame(ventana_Principal)
cuadradozzz.config(bg="red", width=75, height=75)
cuadradozzz.place(x=125 ,y=225)


ventana_Principal.mainloop()