#---------------------------------------------------------
# Ejemplo básico de Listas
#---------------------------------------------------------

listaVacia = []

miLista = [5, 2, 0, 1, 6.5, 0, 7, 28, 95]
print("Lista original: " + str(miLista) + ", Tamaño : " + str(len(miLista)) )

#Imprimimos la posición de un valor guardado en la lista
print ("posición del elemento 1: " + str(miLista.index(1)) )

#Imprimimos cuantas veces aparece un elemento en la lista
print ("Cuantos elementos '0' hay en la lista: " + str(miLista.count(0)) )

#Insertamos un elemento (33) al inicio
miLista.insert(0, 33)
print ("Insertamos 33 al inicio: "+ str(miLista))

#Agreamos un elemento nuevo (888) al final
miLista.append(888)
print("Agregamos un elemento al final de la lista: " + str(miLista))

#Removemos un elemento de la lista
miLista.remove(6.5)
print("Removemos un elemento de la lista: " + str(miLista))

#Removemos un elemento de la lista
del miLista[1]
print("Se Remueve el elemento con índice 1: " + str(miLista) )

#Ordenamos la Lista
miLista.sort()
print("Lista ordenada" + str(miLista) )

#Volteamos la Lista
miLista.reverse()
print("Lista al reves" + str(miLista) )

print("Ultimo elemento de la lista: " + str(miLista.pop()) )

#Cuando vemos rangos numéricos como 1:4 en Python se conoce como Slices
print("Un rango de elementos (1->4) de la Lista (Slice): " + str(miLista[1:4]))


