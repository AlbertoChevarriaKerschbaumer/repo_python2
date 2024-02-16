from tkinter import * #importar libreria

ventana=Tk() #definir repositorio ventana
ventana.title("mi ventana") # asignar titulo
ventana.config(bg="blue") #asignar color de fondo
ventana.geometry("400x200") #asignar dimensiones
ventana.geometry("400x200+20+20") #asignar dimensiones - OTRA FORMA
ventana.resizable(width="True", height="True") #cambiar tamaño de ventana

ventana.mainloop()#crear ventana 

# ventana es un repositorio