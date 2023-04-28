# ------------------
# Desktop App No. 1
# ------------------

#Se importa la librería tkinter con todas su funciones 

from tkinter import * 
from tkinter import messagebox

# --------------------
# Funciones de la app
# --------------------

# Sumar

def sumar():
    pass

# Borrar
def borrar():
    pass
# Salir
def salir():
    messagebox.showinfo("Suma Enteros 1.0", "La app se cerrará")
    ventana_Principal.destroy()



# ---------------------------
# Ventana principal de la app
# ---------------------------

# Se declara una variable que adquiere las características de un objeto tk

ventana_Principal = Tk()

# Título de la ventana

ventana_Principal.title("Suma Enteros 1.0")

#Tamaño de la ventana

ventana_Principal.geometry("500x500")

# Deshabilitar botón de maximizar 

ventana_Principal.resizable(False, False)

# Color de fondo de la ventana

ventana_Principal.config(bg="cyan")
# Variables globales
x = StringVar()
y = StringVar()

# ------------------
# Frame entrada de datos
# ------------------

frame_entr = Frame(ventana_Principal)
frame_entr.config(bg="white", width=480, height=180)
frame_entr.place(x=10, y=10)

# Logo app
logo=PhotoImage(file="img/escudo_colegio.png")
lb_logo=Label(frame_entr, image=logo, bg="white")
lb_logo.place(x=70,y=50)

# ------------------
# Frame operaciones
# ------------------
frame_opr = Frame(ventana_Principal)
frame_opr.config(bg="white", width=480, height=100)
frame_opr.place(x=10, y=200)

# Botón para sumar
bt_sumar = Button(frame_opr, text = "Sumar", command=sumar)
bt_sumar.place(x=45,y=35, width=100, height=30)
# Botón para borrar
bt_borrar=Button(frame_opr, text = "Borrar", command=borrar)
bt_borrar.place(x =190 ,y=35 , width=100, height=30)
# Botón para salir
bt_salir=Button(frame_opr, text= "Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)
# ------------------
# Frame resultados
# ------------------

frame_resu = Frame(ventana_Principal)
frame_resu.config(bg="gray60", width=480, height=180)
frame_resu.place(x=10, y=310)
ventana_Principal.config(bg="CadetBlue2")

# Área de texto para los resultado
t_resultados=Text(frame_resu)
t_resultados.config(bg="black", fg="green yellow", width=480, height=100, font=("Arial",12))
t_resultados.place(x=10, y=10)
# Título de la app

titulo=Label(frame_entr, text="Suma Enteros 1.0")
titulo.config(font=("Arial", 16), bg ="white")
titulo.place(x=240, y =10)

# Etiqueta para valor de x
lb_x = Label(frame_entr, text="X = ")
lb_x.config(bg="white", font=("Times New Roman",18,))
lb_x.place(x=240, y=60)


# Caja de texto para valor de x

entry_X = Entry(frame_entr,textvariable=X)
entry_X.config(bg="white", font=("Times New Roman",18,) ,width=7)
entry_X.focus_set()
entry_X.place(x=290, y=60)



#Caja de texto para valor de y
entry_y = Entry(frame_entr, textvariable=Y)
entry_y.config(bg="white", font=("Times New Roman",18,) ,width=7)
entry_y.place(x=290, y=120)
lb_Y = Label(frame_entr, text="Y = ")
lb_Y.config(bg="white", font=("Times New Roman",18,))
lb_Y.place(x=240, y=120)    
# Run
ventana_Principal.mainloop()




 