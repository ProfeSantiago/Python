#---------------------------------------------------------
# Ejemplo básico de uso de Modulos existentes
# (Los módulos son librerías que contienen funciones)
#---------------------------------------------------------
import requests
import random
import math
import platform
import datetime
import json

print("Usando Módulos Existentes (built-in modules) en Python ")

sistema = platform.system()
print("Ejemplo del módulo platform: ",sistema)

aleatorio = random.randint(1,1000)
print("Ejemplo de Random del módulo math: ", aleatorio)

raizCuadrada = math.sqrt(8)
print("Ejemplo de Raiz cuadrada del módulo math: ", raizCuadrada)

laFecha = datetime.datetime.now()
print("Ejemplo de fecha Actual: ", laFecha)

#--------------------------------------------------------------------------------------------------------------

#miLlamada = requests.get('http://jsonip.com') #Llamamos a un Web Api
#miLlamada = requests.get('http://ip-api.com/json'') #Llamamos a un Web Api
miLlamada = requests.get('https://restcountries.eu/rest/v1/all')
miObjetoJSON = miLlamada.json() #Convertimos el texto en JSON

print("\nEjemplo del modulo Requests. Imprimimos el JSON del Web Service:")
print(miObjetoJSON)

print("\nExtraemos e Imprimimos un elemento del JSON del Web Service:")
stringJSON = json.dumps(miObjetoJSON)
miElementoJson = json.loads(stringJSON)
#print(miElementoJson["ip"])
#print(miElementoJson["query"])
print(miElementoJson[1]["name"])
#--------------------------------------------------------------------------------------------------------------
# Nota:
#   Para que no hayan errores por el Modulo requests hay que descargarlo con esta instruccion:
#
#   C:\> pip install requests
#
# (Desde la linea de comandos)
#--------------------------------------------------------------------------------------------------------------