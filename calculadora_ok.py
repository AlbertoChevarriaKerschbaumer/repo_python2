from tkinter import * #importar libreria

def pulsar_tecla(tecla):
    actual =expresion.get()
    if actual == "Error" or actual == "No valido":
        actual =""
    elif actual == "0" and tecla in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
        actual = ""
    elif actual[-1] in ("+", "-", "*", "/") and tecla in ("+", "-", "*", "/"):
        actual=actual[:-1]
    actual += tecla
    expresion.set(actual)

def pulsar_limpiar():
    expresion.set("0")
def division():
    expresion.set("0")
def pulsar_igual():
    actual=expresion.get()
    try:
        resultado = eval(actual)
    except ZeroDivisionError:
        resultado = "no valido"
    except:
        resultado = "Error"
    expresion.set(resultado)
def pulsar_atras():
    actual = expresion.get()
    if actual == "Error" or actual == "No valido":
        actual ="0"
    if len(actual)>1:
        actual = actual[:-1]
        expresion.set(actual)
    elif len(actual)<=1:
        expresion.set("0")

    
ventana=Tk() #definir repositorio ventana

expresion=StringVar()
expresion.set("0")

ventana.title("mi calculadora") # asignar titulo
ventana.config(bg="blue") #asignar color de fondo
ventana.geometry("400x400") #asignar dimensiones
ventana.resizable(width="True", height="True") #cambiar tamaño de ventana

marco=Frame(ventana)

Pantalla=Label(marco, textvariable=expresion,width=3, anchor="e", bd=4, relief="sunken",font="Arial 16")
Pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")

limpiar=Button(marco, text="C", width=3, font="Arial 16",command=pulsar_limpiar)
limpiar.grid(row=1, column=0,columnspan=2, padx=2, pady=2, sticky="nsew")
division=Button(marco, text="/", width=3, font="Arial 16",  command=lambda: pulsar_tecla("/"))
division.grid(row=1, column=2,padx=2, pady=2)
multiplicacion=Button(marco, text="*", width=3, font="Arial 16",  command=lambda: pulsar_tecla("*"))
multiplicacion.grid(row=1, column=3, padx=2, pady=2)

siete=Button(marco, text="7", width=3, font="Arial 16",  command=lambda: pulsar_tecla("7"))
siete.grid(row=2, column=0, padx=2, pady=2)
ocho=Button(marco, text="8", width=3, font="Arial 16", command=lambda: pulsar_tecla("8"))
ocho.grid(row=2, column=1, padx=2, pady=2)
nueve=Button(marco, text="9", width=3, font="Arial 16", command=lambda: pulsar_tecla("9"))
nueve.grid(row=2, column=2, padx=2, pady=2)
menos=Button(marco, text="-", width=3, font="Arial 16",  command=lambda: pulsar_tecla("-"))
menos.grid(row=2, column=3, padx=2, pady=2)

cuatro=Button(marco, text="4", width=3, font="Arial 16", command=lambda: pulsar_tecla("4"))
cuatro.grid(row=3, column=0, padx=2, pady=2)
cinco=Button(marco, text="5", width=3, font="Arial 16", command=lambda: pulsar_tecla("5"))
cinco.grid(row=3, column=1, padx=2, pady=2)
seis=Button(marco, text="6", width=3, font="Arial 16", command=lambda: pulsar_tecla("6"))
seis.grid(row=3, column=2, padx=2, pady=2)
mas=Button(marco, text="+", width=3, font="Arial 16",  command=lambda: pulsar_tecla("+"))
mas.grid(row=3, column=3, padx=2, pady=2)

uno=Button(marco, text="1", width=3, font="Arial 16", command=lambda:pulsar_tecla("1"))
uno.grid(row=4, column=0, padx=2, pady=2)
dos=Button(marco, text="2", width=3, font="Arial 16", command=lambda: pulsar_tecla("2"))
dos.grid(row=4, column=1, padx=2, pady=2)
tres=Button(marco, text="3", width=3, font="Arial 16", command=lambda: pulsar_tecla("3"))
tres.grid(row=4, column=2, padx=2, pady=2)
igual=Button(marco, text="=", width=3, font="Arial 16",  command=lambda: pulsar_igual())
igual.grid(row=4, column=3,rowspan=2, padx=2, pady=2, sticky="nsew")

punto=Button(marco, text=".", width=3, font="Arial 16",  command=lambda: pulsar_tecla("."))
punto.grid(row=5, column=0, padx=2, pady=2)
cero=Button(marco, text="0", width=3, font="Arial 16", command=lambda: pulsar_tecla("0"))
cero.grid(row=5, column=1, padx=2, pady=2)
borrar=Button(marco, text="<-", width=3, font="Arial 16", command=lambda: pulsar_atras())
borrar.grid(row=5, column=2, padx=2, pady=2)

marco.pack(padx=3, pady=3)
ventana.mainloop()#crear ventana 

# ventana es un repositorio