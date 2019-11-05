import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de",nombre ,".")

	def __str__(self): #convierte en cadena de texto la información de un objeto
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+")
		#desplazamos el cursor al inicio
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(ListaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero está vacio")
		finally:
			listaDePersonas.close()
			del (listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)
	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno","wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFicheroExterno(self):
		print("La información del fichero externo es la siguiente:")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()

persona=Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

persona=Persona("Juan", "Masculino", 52)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()

#p=Persona("Sandra", "Femenino", 29)
#miLista.agregarPersonas(p)

#p=Persona("Antonio", "Masculino", 39)
#miLista.agregarPersonas(p)

#p=Persona("Ana", "Femenino", 19)
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()

