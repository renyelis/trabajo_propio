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


    def calcular_notas():
        messagebox.showinfo("Nota Difinitiva", "Operacion realizada")

        # variables notas
        entry_proc_def = float(entry_proc.get())
        entry_c_def = float(entry_c.get())
        entry_auto_def = float(entry_auto.get())
        entry_act_def = float(entry_act.get())
        entry_bim_def = float(entry_bim.get())

        entry_not_final = (0.3*entry_proc_def) + (0.3*entry_c_def) + (0.1*entry_auto_def) + (0.1*entry_act_def) + (0.2*entry_bim_def)

        if entry_not_final < 30:
                messagebox.showinfo("Resultado", "su nota definitiva es:  "+str(entry_not_final))
        else:
                messagebox.showinfo("Resultado", "su nota definitiva es:  "+str(entry_not_final))
# boton para convertir
    bt_convertir = Button(abrir_notas, text="Resultado", command=calcular_notas)
    bt_convertir.place(x=130, y=400, width=100, height=80)










    
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
    entry_peso= Entry(frame_entrada, )
    entry_peso.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_peso.focus_set()
    entry_peso.place(x=200,y=150, height=30, width=100)

    # etiqueta para el dato
    lb_c = Label(frame_entrada, text = " Estatura= ")
    lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
    lb_c.place(x=50, y=200)

    # caja de texto 
    entry_estatura = Entry(frame_entrada, )
    entry_estatura.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
    entry_estatura.focus_set()
    entry_estatura.place(x=200,y=200, height=30, width=100)


    def convertir_imc():
        estatura = float(entry_estatura.get())
        peso = float(entry_peso.get())
        imc = peso/estatura**2

        if imc < 16:
            messagebox.showinfo("resultado","esta muy flaco")
        elif imc < 17:
            messagebox.showinfo("resultados","esta en delgadez moderada")
        elif imc <18.5:
            messagebox.showinfo("resultados","esta en delgadez ligera") 
        elif imc < 25:
            messagebox.showinfo("resultdos","esta saludable")       
        elif imc < 30:
            messagebox.showinfo("resultados","esta en sobrepeso,cuidese mas")
        elif imc < 35:
            messagebox.showinfo("resultados","esta en obecidad I grado") 
        elif imc < 34:
            messagebox.showinfo("resultados","esta en obecidad II grado")  
        else:
            messagebox.showinfo("resultados","esta en obecidad II grado")  

    # boton para calcular
    bt_convertir= Button(abrir_imc, text="Masa corporal", command=convertir_imc)
    bt_convertir.place(x=130, y=280, width= 100, height= 80)



#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Renyelis del Carmen Luyando Capitillo")

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
frame_entrada.config(bg="white", width=480, height=600)
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
entry_.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
entry_.focus_set()
entry_.place(x=200,y=200, height=30, width=150)

# etiqueta para el dato
lb_c = Label(frame_entrada, text = " Grado = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=50, y=250)

# caja de texto 
entry_ = Entry(frame_entrada, )
entry_.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
entry_.focus_set()
entry_.place(x=200,y=250, height=30, width=150)

# etiqueta para el dato
lb_c = Label(frame_entrada, text = " Edad = ")
lb_c.config(bg="white", fg="blue", font=("Comic Sans MS", 20))
lb_c.place(x=50, y=300)

# caja de texto 
entry_ = Entry(frame_entrada, )
entry_.config(bg="white", fg="blue", font=("Times New Roman", 10), width=6)
entry_.focus_set()
entry_.place(x=200,y=300, height=30, width=150)


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

ventana_principal.mainloop()