#---------------------------------------------------------
# Ejemplo básico de Diccionarios
# Son como listas pero se pueden buscar valores
# usando una llave en lugar de un índice
#---------------------------------------------------------

listaEjemplo = [5, 2, 0, 1, 6.5, 0, 7, 28, 95]

miDiccionario = {'usuarioKey':'Admin', 'passwordKey':123456, 'terminalKey':'01'}
print("\nDiccionario completo: "+ str(miDiccionario))

#---------------------------------------------------------
# Buscamos elementos en el diccionario usando llaves
#---------------------------------------------------------
print("\nElementos del diccionario buscados por medio de llaves: " )
print("Usuario=" + str(miDiccionario['usuarioKey']) + ", Password=" + str(miDiccionario['passwordKey'])+", N. de Terminal=" + str(miDiccionario['terminalKey']) )

#---------------------------------------------------------
# Podemos cambiar los valores de elementos ya existentes
#---------------------------------------------------------
miDiccionario['passwordKey'] = "1701E"
print("\nElementos existentes con nuevos valores: " + str(miDiccionario))

#---------------------------------------------------------
# Podemos agregar nuevos elementos al diccionario
#---------------------------------------------------------
miDiccionario['emailKey'] = "test@python.tst"
print("\nDiccionario con un nuevo elementos:      " + str(miDiccionario))

#---------------------------------------------------------
# Podemos buscar de manera segura (sin errores)
#---------------------------------------------------------
valorBuscado = miDiccionario.get('llave_Inexistente')
print('El valor buscado es: ' + str(valorBuscado))
#Nota:
#   Si devuelve 'None' es porque el valor buscado no existe

#---------------------------------------------------------
# Borramos elementos del diccionario
#---------------------------------------------------------
del miDiccionario['emailKey']
print("\nDiccionario con menos elementos:      " + str(miDiccionario))