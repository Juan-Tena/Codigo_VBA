from  tkinter import *

raiz=Tk()


miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, sticky="w", padx=10, pady=10)
cuadroNombre.config(fg="red", justify="left")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=1, column=1, sticky="w", padx=10, pady=10)
cuadroPassword.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, sticky="w", padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, sticky="w", padx=10, pady=10)

TextoComentatario=Text(miFrame, width=16, height=5)
TextoComentatario.grid(row=4, column=1, padx=10, pady=10)
#Introducimos un scrollbar para poder subir y bajar sobre el texto introduciro en Text
scrollVert=Scrollbar(miFrame, command=TextoComentatario.yview)#lo ajustamos al TextoComentario
scrollVert.grid(row=4, column=2, sticky="nsew")
TextoComentatario.config(yscrollcommand=scrollVert.set)#Permite que al escribir, el scroll se desplaze haste la línea activa






nombreLabel=Label(miFrame, text='Nombre :')
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombrePassword=Label(miFrame, text='Password :')
nombrePassword.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text='Apellidos :')
apellidoLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

direccionLabel=Label(miFrame, text='Dirección :')
direccionLabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

comentariosLabel=Label(miFrame, text='Comentarios :')
comentariosLabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

def codigoBoton():
	minombre.set("Juan")
botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()


raiz.mainloop()