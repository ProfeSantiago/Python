#---------------------------------------------------------
# Ejemplo básico de comparación de diccionarios
#---------------------------------------------------------

primerDiccionario = {'naveKey':'Enterprise', 'matriculaKey':'NCC 1701-E', 'capitanKey':'Jean Luc Picard'}

segundoDiccionario = {'capitanKey':'Jean Luc Picard', 'naveKey':'Enterprise', 'matriculaKey':'NCC 1701-E'}

tercerDiccionario = {'naveKey':'Defiant', 'matriculaKey':'74656', 'capitanKey':'Benjamin Cisco'}

print("\nLas listas son iguales? " + str(primerDiccionario == segundoDiccionario))

print("\nLas listas son iguales? " + str(segundoDiccionario == tercerDiccionario))

#---------------------------------------------------------
#Nota:
#   Como los diccionarios NO son contenedores ordenados
#   deben ser iguales tanto en el valor y
#   cantidad de elementos, pero NO deben ser iguales
#   en el orden de los mismos.
#---------------------------------------------------------