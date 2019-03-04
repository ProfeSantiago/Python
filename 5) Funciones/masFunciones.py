#---------------------------------------------------------
# Ejemplo básico de Funciones
#---------------------------------------------------------
opcionesUsuario = []
menu = ['1) Lado obscuro de la Luna','2) Narnia','2) 20 leguas de viaje submarino','4) Ruinas del planeta kripton']

def imprimeTitulo():
    print("\nAgencia de viajes Titanic, Lo llevamos donde nadie lo lleva")
    print("Nuestro Menú;")

def imprimeMenu():
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[3])

def obtieneSeleccionUsuario():
    opcionseleccionada = input("\nDigite el número de la opción deseada (presione X para salir): ")

    while (opcionseleccionada.upper() != 'X'):
        opcionesUsuario.append(menu[int(opcionseleccionada)-1])
        opcionseleccionada = input("\nDesea alguna otra opción? (presione X para salir): ")

def imprimeResultados():
    print("\nLa opciones seleccionadas son:")
    print(opcionesUsuario)

def main():
    imprimeTitulo()
    imprimeMenu()
    obtieneSeleccionUsuario()
    imprimeResultados()

main()