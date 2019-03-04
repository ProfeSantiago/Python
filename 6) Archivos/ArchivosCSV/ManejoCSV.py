import csv

def abreCSV(Nombre_Archivo):
    with open(Nombre_Archivo) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'\nLos nombres de las columnas son: \n\t{", ".join(row)}\n')
                line_count += 1
                print(f'Los datos del archivo CSV son:\n')
            else:
                print(f'\tEl telefono de {row[0]} es: {row[1]}.')
                line_count += 1

        print(f'\n{line_count} lineas procesadas.')


def creaCSV(Nombre_Archivo):
    with open(Nombre_Archivo, mode='w') as csv_file:
        fieldnames = ['Nombre', 'Telefono']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Nombre': 'John Wick', 'Telefono': '6666-6666'})
        writer.writerow({'Nombre': 'Diana Prince', 'Telefono': '7777-7777'})

def main():
    abreCSV('listaTelefonos.csv')
    #creaCSV('listaTelefonos2.csv')
    abreCSV('listaTelefonos2.csv')
main()