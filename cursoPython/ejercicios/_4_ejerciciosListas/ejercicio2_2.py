

# Pedimos los datos al usuario y los guardamos en las variables nombre y edad
nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")

# Guardamos los datos en una lista
datosPersona = []
datosPersona.append(nombre)
datosPersona.append(edad)

# Mostramos los datos
print("Nombre: " + datosPersona[0])
print("Edad: " + datosPersona[1])

# mostrarlo con un for
for i in datosPersona:
    print(i)