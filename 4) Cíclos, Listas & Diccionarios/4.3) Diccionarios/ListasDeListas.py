#---------------------------------------------------------
# Ejemplo básico de Listas de Listas
# y Diccionarios de Listas
#---------------------------------------------------------

menus = [
            ['pinto con natilla y tortillas','huevos con salchicha','cafe o jugo','platanos con natilla'],
            ['casado','carne','pollo','pescado'],
            ['spagetti','sopa','ensalada','casado']
        ]

print("\n Menú completo: " + str(menus) )
print("\n Menú desayuno: " + str(menus[0]) )
print("\n Menú almuerzo: " + str(menus[1]) )
print("\n Menú cena: " + str(menus[2]) )

print("\n Segunda opción del Menú de desayuno: " + str(menus[0][1]) )
print("\n Tercera opción del Menú de cena: " + str(menus[2][2]) )
print("\n Primera opción del Menú de almuerzo: " + str(menus[1][0]) )


#---------------------------------------------------------
# Diccionarios de Listas
#---------------------------------------------------------

print("\n ~~~~~~~~~~~~~~~~~~~~~~~~")

menusCompletos = {
            'Desayuno':['pinto con natilla y tortillas','huevos con salchicha','cafe o jugo','platanos con natilla'],
            'Almuerzo':['casado','carne','pollo','pescado'],
            'Cena':['spagetti','sopa','ensalada','casado']
        }
print("\n Menú completo: " + str(menusCompletos) )
print("\n Menú desayuno: " + str(menusCompletos['Desayuno']) )
print("\n Primera opción del Menú de almuerzo: " + str(menusCompletos['Almuerzo'][0]) )