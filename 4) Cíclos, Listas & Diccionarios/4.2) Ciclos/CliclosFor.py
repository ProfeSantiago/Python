#---------------------------------------------------------
# Ejemplo básico de Cíclos For
#---------------------------------------------------------

unaLista = [161, 22, 33, 64, "Hola"]

print("Contenido de la lista" + str(unaLista))

#Ejemplo de un "For Each"
for elemento in unaLista:
    print(elemento)

#----------------------------------------------
print()

#Imprimimos un rango numerico secuencial
for i in range(10):
    print(i)

#----------------------------------------------
print()

inicio = 2005
final = 2016
intervalo = 2

#Imprimimos un rango numerico secuencial
for i in range(inicio, final, intervalo):
    print(i)