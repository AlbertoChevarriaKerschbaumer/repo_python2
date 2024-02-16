from tkinter import * #importar libreria

ventana=Tk() #definir repositorio ventana
ventana.title("mi ventana") # asignar titulo
ventana.config(bg="blue") #asignar color de fondo
ventana.geometry("400x200") #asignar dimensiones
ventana.resizable(width="True", height="True") #cambiar tamaño de ventana

label1 = Label(ventana, text="Ingresa Nombre:") #definir etiqueta
label1.place(x=10, y=2, width=100, height=30)#Ubicar etiqueta en la ventana columna 10 fila 2 ancho 100 altura 30
Entrada=Entry(ventana) #definir entrada
Entrada.place(x=120,y=2, width=100, height=30) #Ubicar entrada en la ventana columna 120 fla 2 ancho 100 altura 30
#Entrada.grid(row=2,column=2)
ventana.mainloop()#crear ventana 

# ventana es un repositorio