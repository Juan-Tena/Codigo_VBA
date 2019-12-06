from tkinter import *

root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Creamos los elementos de menú
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()#Añade una barra separadora entre los elementos de menú
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")
archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de")

#Agregamos los elementos de menú en la barra de menu
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=archivoEdicion)	
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)	
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)	



root.mainloop()