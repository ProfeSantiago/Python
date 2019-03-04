#---------------------------------------------------------
# Ejemplo básico de Cíclos While
#---------------------------------------------------------

unValor = 1

while unValor <= 5:
    print(unValor)
    unValor = unValor + 1
#----------------------------------------------

while (True):
    variable_entrada = input("Desea continuar (S / N): ")
    if variable_entrada.upper() == 'N':
        break
#----------------------------------------------