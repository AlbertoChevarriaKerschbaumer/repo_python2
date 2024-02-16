from tkinter import * #importar libreria

ventana=Tk() #definir repositorio ventana
ventana.title("mi ventana") # asignar titulo
ventana.config(bg="blue") #asignar color de fondo
ventana.geometry("400x200") #asignar dimensiones
ventana.geometry("400x200+20+20") #asignar dimensiones - OTRA FORMA
ventana.resizable(width="True", height="True") #cambiar tamaño de ventana

label1 = Label(ventana, text="Ingresa Nombre")
#label1.pack() #Ubicar etiqueta en la ventana
label1.place(x=2, y=2,width=200, height=30) #Ubicar etiqueta en la ventana fila 2 columna 2
#label1.place(x=20, y=50, width=100, height=30)#Ubicar etiqueta en la ventana fila 2 columna 50 ancho 100 altura 30
label1.config(anchor="n") #Ubicar el texto de la etiqueta hacia el norte
label1.config(anchor="ne") #Ubicar el texto de la etiqueta hacia el nor este
label1.config(anchor="s") #Ubicar el texto de la etiqueta hacia el sur
label1.config(anchor="se") #Ubicar el texto de la etiqueta hacia el sur este
label1.config(anchor="w") #Ubicar el texto de la etiqueta hacia el oeste
#label1.config(anchor="center") #Ubicar el texto de la etiqueta hacia el centro
ventana.mainloop()#crear ventana 

# ventana es un repositorio