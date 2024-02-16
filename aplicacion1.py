from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    db_name='mi_BD.db'
    def __init__ (self, window):
        self.win=window
        self.win.title('mi aplicacion')
        #creando un frame contenedor
        frame=LabelFrame(self.win, text='Registro de Productos')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        #input
        Label(frame, text='Nombre:').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1)
        #precio
        Label(frame, text='Precio:').grid(row=2, column=0)
        self.precio=Entry(frame)
        self.precio.grid(row=2, column=1)
        
        ttk.Button(frame, text='Guardar Datos').grid(row=3, columnspan=3, sticky=W+E)
        #Añadir tabla
        self.tree=ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor= CENTER)
        self.tree.heading('#1', text='Precio', anchor=CENTER)
        
        self.get_products()
        
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor=conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
            return result
    def get_products(self):
        #limpiando tabla
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(elements)
        #mostrando datos
            query='SELECT * FROM productos ORDER BY descripcion DESC'
            db_rows=self.run_query(query)
        #llenando tabla
        for row in db_rows:
            self.tree.insert('',0,text=row[1], values=row[2])
    def validation(self):
        return len(self.descripcion)!=0 and len(self.Precio)!=0
    
    def add_producto(self):
        if (self.validation()):
            print()
        
        
        
    
    
if __name__ == '__main__':
    window=Tk()
    Product(window)
    window.mainloop()