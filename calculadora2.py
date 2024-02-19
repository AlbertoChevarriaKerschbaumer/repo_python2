from tkinter import * #importar libreria

def pulsar_numero(numero):
    #resultado.set(int(resultado.get())+numero)
    #resultado.set("0")
    Pantalla.config(text=int(numero))
    
ventana=Tk() #definir repositorio ventana
ventana.title("mi calculadora") # asignar titulo
ventana.config(bg="blue") #asignar color de fondo
ventana.geometry("400x400") #asignar dimensiones
ventana.resizable(width="True", height="True") #cambiar tamaño de ventana

marco=Frame(ventana)

Pantalla=Label(marco, text="0",width=3, anchor="e", bd=4, relief="sunken",font="Arial 16")
Pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")

limpiar=Button(marco, text="C", width=3, font="Arial 16")#, command=pulsar_limpiar)
limpiar.grid(row=1, column=0,columnspan=2, padx=2, pady=2, sticky="nsew")
division=Button(marco, text="/", width=3, font="Arial 16")
division.grid(row=1, column=2,padx=2, pady=2)
multiplicacion=Button(marco, text="*", width=3, font="Arial 16")
multiplicacion.grid(row=1, column=3, padx=2, pady=2)

siete=Button(marco, text="7", width=3, font="Arial 16",  command=lambda: pulsar_numero(7))
siete.grid(row=2, column=0, padx=2, pady=2)
ocho=Button(marco, text="8", width=3, font="Arial 16", command=lambda: pulsar_numero(8))
ocho.grid(row=2, column=1, padx=2, pady=2)
nueve=Button(marco, text="9", width=3, font="Arial 16", command=lambda: pulsar_numero(9))
nueve.grid(row=2, column=2, padx=2, pady=2)
menos=Button(marco, text="-", width=3, font="Arial 16")
menos.grid(row=2, column=3, padx=2, pady=2)

cuatro=Button(marco, text="4", width=3, font="Arial 16", command=lambda: pulsar_numero(4))
cuatro.grid(row=3, column=0, padx=2, pady=2)
cinco=Button(marco, text="5", width=3, font="Arial 16", command=lambda: pulsar_numero(5))
cinco.grid(row=3, column=1, padx=2, pady=2)
seis=Button(marco, text="6", width=3, font="Arial 16", command=lambda: pulsar_numero(6))
seis.grid(row=3, column=2, padx=2, pady=2)
mas=Button(marco, text="+", width=3, font="Arial 16")
mas.grid(row=3, column=3, padx=2, pady=2)

uno=Button(marco, text="1", width=3, font="Arial 16", command=lambda: pulsar_numero(1))
uno.grid(row=4, column=0, padx=2, pady=2)
dos=Button(marco, text="2", width=3, font="Arial 16", command=lambda: pulsar_numero(2))
dos.grid(row=4, column=1, padx=2, pady=2)
tres=Button(marco, text="3", width=3, font="Arial 16", command=lambda: pulsar_numero(3))
tres.grid(row=4, column=2, padx=2, pady=2)
igual=Button(marco, text="=", width=3, font="Arial 16")
igual.grid(row=4, column=3,rowspan=2, padx=2, pady=2, sticky="nsew")

punto=Button(marco, text=".", width=3, font="Arial 16")
punto.grid(row=5, column=0, padx=2, pady=2)
cero=Button(marco, text="0", width=3, font="Arial 16", command=lambda: pulsar_numero(0))
cero.grid(row=5, column=1, padx=2, pady=2)
borrar=Button(marco, text="<-", width=3, font="Arial 16")
borrar.grid(row=5, column=2, padx=2, pady=2)

marco.pack(padx=3, pady=3)
ventana.mainloop()#crear ventana 

# ventana es un repositorio