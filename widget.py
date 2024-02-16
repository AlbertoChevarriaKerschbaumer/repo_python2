from tkinter import ttk
from tkinter import *
ventana=Tk()
ventana.title("4 OPERACIONES")
ventana.geometry("400x200")

def fn_suma():
    n1=text1.get()
    n2=text2.get()
    result=float(n1)+float(n2)
    text3.delete(0,'end')
    text3.insert(0,result)
    
def fn_resta():
    n1=text1.get()
    n2=text2.get()
    result=float(n1)-float(n2)
    text3.delete(0,'end')
    text3.insert(0,result)
    
def fn_producto():
    n1=text1.get()
    n2=text2.get()
    result=float(n1)*float(n2)
    text3.delete(0,'end')
    text3.insert(0,result)
    
def fn_division():
    n1=text1.get()
    n2=text2.get()
    if (int(n2) > 0):
        result=float(n1)/float(n2)
        text3.delete(0,'end')
        text3.insert(0,result)
    else:
        text3.delete(0,'end')
        text3.insert(0,'no se divide entre 0')
    
label1=Label(ventana, text="1er numero", bg="yellow")
label1.place(x=10, y=10, width=100, height=30)
text1=Entry(ventana, fg="blue", bg="yellow")
text1.place(x=120, y=10, width=100, height=30)
text1.insert(0,0)

btn=Button(ventana, text="suma", fg="red", bg="yellow", cursor="mouse", command=fn_suma)
btn.place(x=230, y=10, width=60, height=30)
btn=Button(ventana, text="producto", fg="red", bg="yellow", cursor="mouse", command=fn_producto)
btn.place(x=300, y=10, width=60, height=30)

label2=Label(ventana, text="2do numero", bg="yellow")
label2.place(x=10, y=50, width=100, height=30)
text2=Entry(ventana, bg="yellow")
text2.place(x=120, y=50, width=100, height=30)
text2.insert(0,0)

btn=Button(ventana, text="resta", fg="red", bg="yellow", cursor="mouse", command=fn_resta)
btn.place(x=230, y=50, width=60, height=30)
btn=Button(ventana, text="division", fg="red", bg="yellow", cursor="mouse", command=fn_division)
btn.place(x=300, y=50, width=60, height=30)

label3=Label(ventana, text="resultado", bg="yellow")
label3.place(x=10, y=90, width=100, height=30)
text3=Entry(ventana,fg="white", bg="red")
text3.place(x=120, y=90, width=120, height=30)

ventana.mainloop()