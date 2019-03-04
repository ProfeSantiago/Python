
ListAbecedario = ['a','b','c','d','e','f','g','h''i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
palabraSeleccionada = input("\nDigite la palabra deseada y presione Enter: ")
nuevaPalabra = ""
nuevaPosicion = 0
posicionLetrActual =  0

for letra in palabraSeleccionada:

    posicionLetrActual = ListAbecedario.index(letra)

    if posicionLetrActual < len(ListAbecedario) - 2:
        nuevaPosicion = posicionLetrActual + 3
        nuevaPalabra = nuevaPalabra + ListAbecedario[nuevaPosicion]
    else:
        nuevaPalabra = nuevaPalabra + ListAbecedario[posicionLetrActual]

print(nuevaPalabra)