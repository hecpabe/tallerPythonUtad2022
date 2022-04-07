

# diccionarios
diccionario = {"nombre": "Héctor", "edad": 19, "Teléfono": 123456789}

for i in diccionario:
    print(i + ": " + str(diccionario[i]))

agenda = {"contacto1": {"nombre": "jesus", "telefono":12141431}, "contacto2":{"nombre": "ana", "telefono":12534261}}

for i in agenda:
    print(i + ": " + str(agenda[i]))


# Añadimos un nuevo contacto
agenda["contacto3"] = {"nombre": "Héctor", "Teléfono": 123456789}

for i in agenda:
    print(i + ": " + str(agenda[i]))