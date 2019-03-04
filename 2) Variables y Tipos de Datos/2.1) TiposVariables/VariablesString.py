#-------------------------------------------------------------
# Los Strings pueden estar encerrados entre comillas simples
# o comillas dobles
#-------------------------------------------------------------

nombre="John"

apellido='Rambo'

#Variables concatenadas con cadenas de texto
nombreCompleto = nombre + ' ' + apellido

#-------------------------------------------------------------
print('Un String con comillas dobles : ' + nombre)

print('Un String con comillas simples: ' + apellido)

print('Strings concatenados en el print: ' + nombre + " " + apellido)

print('Strings concatenados en variable: ' + nombreCompleto)

#-------------------------------------------------------------

textoSize = len(nombreCompleto)

primeraLetra = nombreCompleto[0]

ultimaLetra = nombreCompleto[textoSize-1]

#Cuando vemos rangos numéricos como 1:3 en Python se conoce como Slices

dosLetras = nombreCompleto[1:3]

quinta_en_adelante = nombreCompleto[5:]

algunasLetras = nombreCompleto[2:8]

#-------------------------------------------------------------

print('Tamaño del String: '+ str(textoSize)+', Primera Letra : ' + primeraLetra +", Ultima Letra: " + ultimaLetra)

print('Segunda letra y tercera letra: '+ dosLetras )

print('Letras de la #3 a la #7: '+ algunasLetras )

print('De la quinta letra en adelante: '+ quinta_en_adelante )