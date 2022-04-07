

# Pedimos el número de personas
numeroPersonas = input("Introduzca un número de personas: ")
numeroPersonas = int(numeroPersonas)

# Declaramos un contador de número de personas
contador = 0

# Realizamos el algoritmo n veces
while(contador < numeroPersonas):
    print("Persona " + str(contador + 1) + "...")
    nombre = input("Introduzca un nombre: ")
    edad = input("Introduzca una edad: ")
    print("Nombre: " + nombre)
    print("Edad: " + edad)
    contador = contador + 1