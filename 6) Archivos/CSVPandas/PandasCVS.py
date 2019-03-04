#-------------------------------------------------------
#    Para este ejercicio hay que correr estos comandos desde el Terminal o Consola:
#
#    pip install --upgrade pip
#    pip install pandas
#-------------------------------------------------------

import pandas

def leeCSVPandas(archivoCSV):
    datosLeidos = pandas.read_csv(archivoCSV) #,index_col='Nombre'
    print('\n')
    print(datosLeidos)

def CreaCSVPandas(archivoCSV):
    df = pandas.read_csv(archivoCSV,
                index_col='Telefono',
                parse_dates=['Cumple'],
                header=2,
                names=['Nombre', 'Telefono', 'Cumple'])
    df.to_csv('CSV_Modificado.csv')

def main():
    leeCSVPandas('listaTelefonos.csv')
    CreaCSVPandas('listaTelefonos.csv')
    leeCSVPandas('CSV_Modificado.csv')

main()