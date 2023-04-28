from tkinter import *
ventana_Principal = Tk()
ventana_Principal.title("Bandera de Suiza")
ventana_Principal.geometry("500x500")

ventana_Principal.config(bg="red")

frame_blanco =Frame(ventana_Principal)
frame_blanco.config(bg="white", width=100, height=300)
frame_blanco.place(x=200,y=100)

frame_white = Frame(ventana_Principal)
frame_white.config(bg="white",width=300, height=100)
frame_white.place(x=100,y=200)
ventana_Principal.mainloop()
