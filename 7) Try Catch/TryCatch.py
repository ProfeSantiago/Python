#---------------------------------------------------------
# Ejemplo básico del Try-Catch
#---------------------------------------------------------
print("Demostraciones de Try-Catch")
print("Intentando abrir un archivo...\n")

try:
    Var_chivo = open('noExiste.txt', 'r')
    print(Var_chivo.read())
except:
    print('Ocurrio un error: El Archivo no existe!!')

#============================================================

print("\n--------------------------------------")
print("Intentando abrir un archivo #2...\n")

try:
    Var_chivo = open('noExiste.txt', 'r')
    print(Var_chivo.read())

except FileNotFoundError as errorcillo:
    print('Se detecto el siguiente error: \n', errorcillo)

print("\n--------------------------------------")
print("Leyendo valores de pantalla...")

#============================================================

try:
    variable_entrada = input("Digite un numero (Mentira ponga una letra para que se caiga):\n")
    variable_entrada = float(variable_entrada)
    print('El numero digitado es:',variable_entrada)

except ValueError as errorcillo:
    print('Se detecto el siguiente error: \n',errorcillo)


#============================================================
# Nota:
#       Tambien existen otros tipos de exepciones como:
#       -IndexError
#       -KeyError
#       -NameError
#============================================================