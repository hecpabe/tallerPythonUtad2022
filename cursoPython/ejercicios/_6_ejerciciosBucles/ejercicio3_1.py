

# Pedimos el número de personas
numeroPersonas = input("Introduzca un número de personas: ")
numeroPersonas = int(numeroPersonas)

# Realizamos el algoritmo n veces
for i in range(numeroPersonas):
    print("Persona " + str(i + 1) + "...")
    nombre = input("Introduzca un nombre: ")
    edad = input("Introduzca una edad: ")
    print("Nombre: " + nombre)
    print("Edad: " + edad)
