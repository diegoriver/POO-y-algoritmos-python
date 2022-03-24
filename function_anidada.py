# def funcion_mayor():
# 	print("Esta es una función mayor y su mensaje de salida.")

# 	def librerias():
# 		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

# 	def frameworks():
# 		print("Algunos frameworks de Python son: Django, Dash y Flask.")

# 	frameworks()
# 	librerias()

# funcion_mayor()

### decorador funtion

# def funcion_decoradora(funcion):
# 	def wrapper():
# 		print("Este es el último mensaje...")
# 		funcion()
# 		print("Este es el primer mensaje ;)")
# 	return wrapper


# @funcion_decoradora
# def zumbido():
# 	print("Buzzzzzz")


##########

class Millas:
	def __init__(self, distancia=0):
		self.distancia = distancia

	def convertir_a_kilometros(self):
		return (self.distancia * 1.609344)


# Creamos un nuevo objeto
avion = Millas()

# Indicamos la distancia
avion.distancia = 200

print(avion.distancia)
print(avion.convertir_a_kilometros())
