# -*- coding: utf-8 -*-
# Importamos la libreria de SQLite
from Tkinter import *
import tkSimpleDialog   #Libreria de almacenamiento de dialogos
import tkMessageBox     #Libreria de mensajes
import sqlite3
import csv

# Creamos la conexion
connection = sqlite3.connect('proyect.db')

# Creamos el cursor
cursor = connection.cursor()

# Creamos el arreglo que contiene toda la informacion
#cursor.execute("""create table producto55(idproducto int,
 #                 nomproducto text,
  #                categoria text,
   #               stock int)""")
# Insertamos todos los registros
#cursor.execute("""insert into producto55
 #                 values 
  #                ('001','prod1', 'limpieza' ,'10')""")
                  
#cursor.execute("""insert into producto55
 #                 values 
  #                ('002','prod2', 'limpieza' ,'0')""")
                  
#cursor.execute("""insert into producto55
 #                 values 
  #                ('003','prod3', 'limpieza' ,'1')""")

# Hacemos efectiva la transaccion
#connection.commit()
#realizamos una consulta
#cursor.execute("""select * from producto55 """)
class Ingreso:
   def __init__(self, parent=0):
      self.principal = Frame(parent)
      self.titulo = Label (text='SISTEMA DE ALMACEN').pack(side=TOP,padx=10,pady=10)
		#self.titulo = Label (text='Sistema de Almacen').pack(side=TOP,padx=10,pady=10)
 
      fcidr = Frame(self.principal)
      self.idprod = Label (fcidr, text='Idproducto: ').pack(side="left")
      
      self.entry = Entry(fcidr)
      self.entry.pack(side="right")
      
      fcidr.pack(fill=X)
      #
      nombre = Frame(self.principal)
      self.nombre = Label (nombre, text='nombre: ').pack(side="left")
      
      self.entry = Entry(nombre)
      self.entry.pack(side="right")
      
      nombre.pack(fill=X)
      
      #
      #
      stock = Frame(self.principal)
      self.stock = Label (stock, text='Categoria: ').pack(side="left")
      
      self.entry = Entry(stock)
      self.entry.pack(side="right")
      
      stock.pack(fill=X)
      
      #
      #
      categoria = Frame(self.principal)
      self.categoria = Label (categoria, text='Stock: ').pack(side="left")
      
      self.entry = Entry(categoria)
      self.entry.pack(side="right")
      
      categoria.pack(fill=X)
      
      #
     # fdecimal = Frame(self.principal)
      
      #self.Decimal = Label (fdecimal, text='Decimal:').pack(side="left")
      #self.texto = StringVar()
      
      #self.Mascara = Label (fdecimal, textvariable=self.texto).pack(side="right")
      #fdecimal.pack(fill=X)
 
      fButtons = Frame(self.principal, border=2, relief="groove")
      bClear = Button(fButtons, text="Guardar", width=8, height=1, command=self.clickGuardar)
      bQuit = Button(fButtons, text="Salir", width=8, height=1, command=self.principal.quit)
      bClear.pack(side="left", padx=15, pady=1)
      bQuit.pack(side="right", padx=15, pady=1)
      fButtons.pack(fill=X)
      self.principal.pack()
 
      self.principal.master.title("sistema de Almacen")
 
   def clickGuardar(self):
	INFILE = open ('datos.cvs', 'w')
# Escriba el texto
	INFILE.escribir(texto)
# Cierra el archivo
	INFILE. close ()
	print "para guardar texto de demostración"
	imprimir
	imprimir
	texto = raw_input ("Escriba un texto:")
	clickGuardar (texto)
	imprimir
		#while INFILE:
		#	lin = INFILE.RADLINE()
		#	for(n in dato):
			#	if lin>=0 len (lin split() [0])== len (n):
			#		dato.[n]= float (lin.split() [1])
			
		

#cursor.execute("select * from producto71") 
#for valor in cursor.fetchall():
#	print valor
#return self.fuc(*args)

cursor.close()
connection.close()
app = Ingreso()
app.principal.mainloop()
