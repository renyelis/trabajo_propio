#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Datos basicos del estudiante")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="red")


barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu = Menu(tearoff=0)
menu.add_command(label="menu", )
menu.add_separator()
menu.add_command(label="Borrar", )

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", )

barra_menu.add_cascade(label="menu", menu=menu)
barra_menu.add_cascade(label="Salir", menu=menu_salir)
# Todo

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=400)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/datos.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=140,y=40)

# titulo de la app
titulo = Label(frame_entrada, text="Datos básicos del estudiante")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=90,y=10)


imgn= PhotoImage(file="img/cal.png")
bt_notas=Button(frame_entrada)
bt_notas.config(image=imgn, width= 50,height=50)
bt_notas.place(x=0 ,y=0)


imgc= PhotoImage(file="img/imc.png")
bt_imc=Button(frame_entrada)
bt_imc.config(image=imgc, width= 50,height=50)
bt_imc.place(x=30 ,y=30)



ventana_principal.mainloop()