from tkinter import *
from tkinter import messagebox

root=Tk()

#Ventana emergentes
def infoAdicional():
	messagebox.showinfo("Procesador de Juan","Procesador de textos. Versión 2019")

def infoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicacion():
	#Muestra los botones de Si/No
	#valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
	#if valor=="yes":
	#	root.destroy()

	#Muestra los botones de Aceptar/Cancelar
	valor=messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")
	if valor==True:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento bloqueado")
	if valor==False:
		root.destroy()

#Creamos la barra de menú
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Creamos los elementos de menú
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()#Añade una barra separadora entre los elementos de menú
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)
archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia",command=infoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)

#Agregamos los elementos de menú en la barra de menu
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=archivoEdicion)	
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)	
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)	



root.mainloop()