#---------------------------------
# Desktop app No. 2- Temperatura
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

def abrir_notas():
    global abrir_notas
    abrir_notas=Toplevel()


    abrir_notas.title("Notas")

    # tamaño de la ventana
    abrir_notas.geometry("400x500")

    # deshabilitar boton de maximizar
    abrir_notas.resizable(False, False)

    # color de fondo de la ventana
    abrir_notas.config(bg="red")

    frame_entrada = Frame(abrir_notas)
    frame_entrada.config(bg="white", width=380, height=480)
    frame_entrada.place(x=10, y=10)

    # titulo de la app
    titulo = Label(frame_entrada, text="Ingrese los datos")
    titulo.config(bg = "white",fg="blue", font=("Comic Sans MS", 20))
    titulo.place(x=100,y=10)

        # etiqueta para el dato
    lb_c = Label(frame_entrada, text = " Cognitivo= ")
    lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_c.place(x=50, y=100)
    # caja de texto 
    entry_c = Entry(frame_entrada, )
    entry_c.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_c.focus_set()
    entry_c.place(x=200,y=100, height=30, width=100)

    # etiqueta para el dato
    lb_proc = Label(frame_entrada, text = " Procedimental = ")
    lb_proc.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_proc.place(x=10, y=150)
    # caja de texto 
    entry_proc = Entry(frame_entrada, )
    entry_proc.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_proc.focus_set()
    entry_proc.place(x=200,y=150, height=30, width=100)

        # etiqueta para el dato
    lb_act = Label(frame_entrada, text = " Actitudinal= ")
    lb_act.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_act.place(x=10, y=200)
    # caja de texto 
    entry_act = Entry(frame_entrada )
    entry_act.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_act.focus_set()
    entry_act.place(x=200,y=200, height=30, width=100)

    # etiqueta para el dato
    lb_auto = Label(frame_entrada, text = " Autoevaluacion = ")
    lb_auto.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_auto.place(x=10, y=250)
    # caja de texto 
    entry_auto = Entry(frame_entrada, )
    entry_auto.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_auto.focus_set()
    entry_auto.place(x=200,y=250, height=30, width=100)

    # etiqueta para el dato
    lb_bim = Label(frame_entrada, text = " Bimestral = ")
    lb_bim.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_bim.place(x=10, y=300)
    # caja de texto 
    entry_bim = Entry(frame_entrada, )
    entry_bim.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_bim.focus_set()
    entry_bim.place(x=200,y=300, height=30, width=100)

    # boton para calcular
    bt = Button(frame_entrada, text="cALCULAR")
    bt.place(x=120, y=350)

    def calcular():
        cong = int(entry_c.get())
        proc = int(entry_proc.get())
        act = int(entry_act.get())
        auto = int(entry_auto.get())
        bim = int(entry_bim.get())
        defit=(0.3*cong)+(0.3*proc)+(0.1*act)+(0.1*auto)+(0.2*bim)















    
def abrir_imc():
    global abrir_imc
    abrir_imc=Toplevel()

    abrir_imc.title("IMC")

    # tamaño de la ventana
    abrir_imc.geometry("400x400")

    # deshabilitar boton de maximizar
    abrir_imc.resizable(False, False)

    # color de fondo de la ventana
    abrir_imc.config(bg="red")

    frame_entrada = Frame(abrir_imc)
    frame_entrada.config(bg="white", width=380, height=380)
    frame_entrada.place(x=10, y=10)

    # titulo de la app
    titulo = Label(frame_entrada, text="Ingrese los datos")
    titulo.config(bg = "white",fg="blue", font=("Comic Sans MS", 20))
    titulo.place(x=100,y=10)
    
    # etiqueta para el dato
    lb_c = Label(frame_entrada, text = " Peso= ")
    lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_c.place(x=50, y=150)

    # caja de texto 
    entry_ = Entry(frame_entrada, )
    entry_.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_.focus_set()
    entry_.place(x=200,y=150, height=30, width=100)

    # etiqueta para el dato
    lb_c = Label(frame_entrada, text = " Altura= ")
    lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_c.place(x=50, y=200)

    # caja de texto 
    entry_ = Entry(frame_entrada, )
    entry_.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_.focus_set()
    entry_.place(x=200,y=200, height=30, width=100)







#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Renyelis Luyando")

# tamaño de la ventana
ventana_principal.geometry("500x700")

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
frame_entrada.config(bg="white", width=480, height=650)
frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/datos.png")
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=140,y=20)

# titulo de la app
titulo = Label(frame_entrada, text="Datos básicos del estudiante")
titulo.config(bg = "white",fg="blue", font=("Comic Sans MS", 20))
titulo.place(x=90,y=10)

# etiqueta para el dato
lb_c = Label(frame_entrada, text = " Nombre = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=50, y=200)

# caja de texto 
entry_ = Entry(frame_entrada, )
entry_.config(bg="white", fg="blue", font=("Times New Roman", 20), width=6)
entry_.focus_set()
entry_.place(x=200,y=200, height=30, width=100)

# etiqueta para el dato
lb_c = Label(frame_entrada, text = " Grado = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=50, y=250)

# caja de texto 
entry_ = Entry(frame_entrada, )
entry_.config(bg="white", fg="blue", font=("Times New Roman", 20), width=6)
entry_.focus_set()
entry_.place(x=200,y=250, height=30, width=100)

# etiqueta para el dato
lb_c = Label(frame_entrada, text = " Edad = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=50, y=300)

# caja de texto 
entry_ = Entry(frame_entrada, )
entry_.config(bg="white", fg="blue", font=("Times New Roman", 20), width=6)
entry_.focus_set()
entry_.place(x=200,y=300, height=30, width=100)


imgn= PhotoImage(file="img/cal.png")
bt_notas=Button(frame_entrada, command=abrir_notas)
bt_notas.config(image=imgn, width= 130,height=130)
bt_notas.place(x=100 ,y=350)


imgc= PhotoImage(file="img/imc.png")
bt_imc=Button(frame_entrada, command=abrir_imc)
bt_imc.config(image=imgc, width= 130,height=130)
bt_imc.place(x=250,y=350)

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=400, height=80)
frame_resultados.place(x=45, y=500)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10,y=10,width=460,height=160)





ventana_principal.mainloop()