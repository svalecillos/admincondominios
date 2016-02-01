
"""
Esta funcion imprime en la consola el argumento recibido
es util para 
arg (requerido): Argumento el cual sera impreso en pantalla de consola con print
nombre (opcional): Para mostrar el nombre del Argumento por consola
"""

def ver(arg,nombre=None):
	if arg:
			if nombre :
				print("___________________________________________________________________________")
				print("Debug de: " + nombre)
			print("___________________________________________________________________________\n\n\n")
			print (arg)
			print("\n___________________________________________________________________________\n")