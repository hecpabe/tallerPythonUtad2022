

# Creamos la función factorial
def factorial(n):
    resultado = 1
    for i in range(n, 1, -1):
        resultado = resultado * i
    return resultado

# Realizamos el factorial
numero = input("Introduzca un número: ")
numero = int(numero)

resultado = factorial(numero)

print("El factorial de " + str(numero) + " es: " + str(resultado))