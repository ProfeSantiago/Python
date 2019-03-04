#---------------------------------------------------------
# Ejemplo básico de manejo de archivos
#---------------------------------------------------------

Var_chivo = open('miArchivito.txt', 'w')
#------------------------------------------------
#Si el segundoparámetro es 'w' entonces escribe
#y si el archivo no existe Python lo crea
#------------------------------------------------

Var_chivo.write('Primera linea del archivo\n')
Var_chivo.write('Segunda linea del archivo')
Var_chivo.close()

Var_chivo = open('miArchivito.txt', 'a')
#------------------------------------------------
#Si el segundo parámetro es 'a' entonces se
# agrega al final del archivo
#------------------------------------------------

Var_chivo.write('. Texto agregado al final del archivo')
Var_chivo.close()


Var_chivo = open('miArchivito.txt', 'r')
#------------------------------------------------
#Si el segundo parámetro es 'r' entonces
# abre y lee el archivo
#------------------------------------------------
laLinea = Var_chivo.readline() #Leemos del archivo
laLinea = laLinea.strip() #Eliminamos espacios en blanco adelante y atras
print('Esta es la linea #1 leida del archivo:\n'+ laLinea)

laLinea = Var_chivo.readline() #Leemos del archivo
laLinea = laLinea.strip() #Eliminamos espacios en blanco adelante y atras
print('Esta es la linea #2 leida del archivo:\n'+laLinea)
