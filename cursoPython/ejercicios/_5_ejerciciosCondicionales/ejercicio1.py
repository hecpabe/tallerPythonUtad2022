

# Pedimos los datos al usuario y los guardamos en las variables nombre y edad
nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
edad = int(edad)

# Mostramos la información en función de la edad
if(edad < 18):
    print("Hola " + nombre + ", eres menor de edad.")
else:
    print("Hola " + nombre + ", eres mayor de edad.")