
# Diccionario

informacion_personal = {
    'nombre': 'Balerio',
    'edad': '20',
    'ciudad': 'Puyo',
}
print(informacion_personal)

# Modificar la ciudad
informacion_personal['ciudad'] = "Cuenca"
print(informacion_personal)

# Agregar profecion
informacion_personal[('profesion')] = "militar"
print(informacion_personal)

# preguntar si telefono existe o no
if "telefono" in informacion_personal:
    print("telefono existe")
else:
    print("telefono No existe")

# agregar telefono
informacion_personal['telefono'] = "0998745317"
print(informacion_personal)

# eliminacion de edad
informacion_personal.pop('edad')
print(informacion_personal)







