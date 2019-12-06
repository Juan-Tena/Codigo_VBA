from tkinter import *
from tkinter import filedialog

root=Tk()

def abrefichero():
	fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:\\", filetypes=(("Ficheros de EXCEL", "*.xlsx"),
		("Ficheros de texto","*.txt"),("Todos los ficheros","*.*")))
	print(fichero)#nos da la ruta del fichero

Button(root, text="Abrir fichero", command=abrefichero).pack()




root.mainloop()