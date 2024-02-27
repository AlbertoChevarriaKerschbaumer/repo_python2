from tkinter import ttk
from tkinter import *

import sqlite3

class Product:
    db_name='mi_BD.db' # Base de Datos
    def __init__ (self, window):
        self.win=window
        
        self.win.title('mi aplicacion')
        #creando un frame contenedor
        frame=LabelFrame(self.win, text='Registro de Productos')
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        #input
        Label(frame, text='nombre:').grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)
        self.nombre.focus()
        #precio
        Label(frame, text='Precio:').grid(row=2, column=0)
        self.precio=Entry(frame)
        self.precio.grid(row=2, column=1)
        
        ttk.Button(frame, text='Guardar Datos', command=self.add_producto).grid(row=3, columnspan=3, sticky=W+E) #Boton Guardar Datos cenrado en 3 columnas
        #Añadir tabla &&Treeview min 24"
        self.tree=ttk.Treeview(height=10, columns=2) # Crear tabla de 10 filas y 2 columnas
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre', anchor= CENTER) #Crear cabecera 1
        self.tree.heading('#1', text='Precio', anchor=CENTER)  #Crear cabecera 2
        self.get_products()
        
        ttk.Button(frame, text='DELETE', command=self.delete_producto).grid(row=5, column=0, sticky=W+E)
        ttk.Button(frame, text='EDIT', command=self.edit_producto).grid(row=5, column=1, sticky=W+E)
         
        #Mostrar mensajes
        self.message=Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W+E)
    def run_query(self, query, parameters=()): #Conexion a BD y ejecucion de consulta (Query)
        with sqlite3.connect(self.db_name) as conn: #Conexion a BD
            cursor=conn.cursor() #almacenar metodo cursor
            result=cursor.execute(query, parameters)#Ejecuta desde cursor metodo execute que permite ejecutar consulta
            conn.commit()#Ejecutar conn(run_query)
            return result
    def get_products(self): #Obtener productos
        #limpiando tabla
        records=self.tree.get_children()#obtener datos de la tabla
        for element in records:
            self.tree.delete(element) #eliminar datos
        #consultando datos
        query='SELECT * FROM Productos ORDER BY nombre DESC'#Crear Consulta
        db_rows=self.run_query(query)#Guardar filas de la consulta 
                    
        #llenando tabla
        for rows in db_rows:
            self.tree.insert('',0,text=rows[1], values=rows[2])
            
    def validation(self):
        return (len(self.nombre.get())!=0 and len(self.precio.get())!=0)
            
    def add_producto(self):
        if (self.validation()):
            query='INSERT INTO Productos values (NULL,?,?)' 
            parameters=(self.nombre.get(), self.precio.get())
            self.run_query(query, parameters)
            self.message['text']='Producto {} agregado correctamente'.format(self.nombre.get())
            self.nombre.delete(0, END)
            self.precio.delete(0, END)
        else:
            self.message['text']='Nombre y precio son requeridos'
        
        #llenado filas de la tabla
        self.get_products()
    def delete_producto(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text']='Selecciona un registro'
            return
        self.message['text']=''
        name=self.tree.item(self.tree.selection())['text']
        parameters=(name)
        #query='DELETE FROM Productos WHERE nombre=?'
        query='DELETE FROM Productos WHERE nombre=?'
        self.run_query(query, (name,)) 
        #self.run_query(query) 
        self.message['text']='Registro {} Eliminado'.format(name)
        self.get_products()
    def edit_producto(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text']='Selecciona un registro'
            return
        name=self.tree.item(self.tree.selection())['text']
        old_precio=self.tree.item(self.tree.selection())['values'][0]
        self.edit_wind=Toplevel() 
        #self.edit_wind.Title('Editar Producto')
        #old name
        Label(self.edit_wind, text='Old name:').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name), state="readonly").grid(row=0, column=2)
        #new name
        Label(self.edit_wind, text='New name:').grid(row=1, column=1)
        new_name=Entry(self.edit_wind)
        new_name.grid(row=1, column=2)
        #old precio
        Label(self.edit_wind, text='Old precio:').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=old_precio), state="readonly").grid(row=2, column=2)
        #new precio
        Label(self.edit_wind, text='New name:').grid(row=3, column=1)
        
        new_precio=Entry(self.edit_wind)
        new_precio.grid(row=3, column=2)
        #Boton actualizar
        Button(self.edit_wind, text='Actualizar', command=lambda: self.edit_records(new_name.get(), name, old_precio, new_precio.get())).grid(row=4, column=2, sticky=W)
        
    def edit_records(self, new_name, name, new_precio, old_precio):
        query='UPDATE Productos SET nombre=?, precio=? WHERE nombre=? and precio=?'
        parameters=(new_name, name, old_precio, new_precio)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text']='Registro{} Actualizado'.format(name)
        self.get_products()
if __name__ == '__main__':
    window=Tk()
    Product(window)
    window.mainloop()