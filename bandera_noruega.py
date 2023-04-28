from tkinter import *
ventana_Principal = Tk()
ventana_Principal.title("Bandera de Noruega")
ventana_Principal.geometry("700x500")

frame_curojo = Frame(ventana_Principal)
frame_curojo.config(bg="red", width=150, height=175)
frame_curojo.place(x=0, y=0)

frame_curojo2 = Frame(ventana_Principal)
frame_curojo2.config(bg="red", width=150, height=175)
frame_curojo2.place(x=0, y=325)

frame_rojo3 = Frame(ventana_Principal)
frame_rojo3.config(bg="red", width=700, height=175)
frame_rojo3.place(x=300, y=0)

frame_rojo4 = Frame(ventana_Principal)
frame_rojo4.config(bg="red", width=700, height=175)
frame_rojo4.place(x=300, y=325)

frame_azul = Frame(ventana_Principal)
frame_azul.config(bg="blue", width=700, height=75)
frame_azul.place(x=0, y=215)

frame_azul2 = Frame(ventana_Principal)
frame_azul2.config(bg="blue", width=75, height=500)
frame_azul2.place(y=0, x=190)


ventana_Principal.mainloop()

