#---------------------------------------------------------
# Ejemplo básico de Funciones
#---------------------------------------------------------
numeroTemporal = 0

def miFuncionSuma(num1, num2):
    return num1+num2

def miFuncionPotencia(num1, num2):
    return num1**num2

#---------------------------------------------------------
# La función main es la parte donde empieza la ejecucion
# del programa, porque aquí se llaman a las otras funciones
#---------------------------------------------------------
def main():
    numeroTemporal = miFuncionSuma(3, 2)
    print("Resultado de la suma de 3+2: " + str(numeroTemporal))

    numeroTemporal = miFuncionPotencia(2, 8)
    print("Resultado de elevar 2 a la octava potencia: " + str(numeroTemporal))

#---------------------------------------------------------
# En Python tenemos que llamar a la función main
# a "mano", es decir: da igual si se llama main o no.
#---------------------------------------------------------
main()