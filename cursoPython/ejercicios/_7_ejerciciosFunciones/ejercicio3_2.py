

# Creamos la función de la suma
def suma(num1, num2):
    return num1 + num2

# Creamos la función de la resta
def resta(num1, num2):
    return num1 - num2

# Creamos la función del producto
def producto(num1, num2):
    return num1 * num2

# Creamos la función de la división
def division(num1, num2):
    if(num2 != 0):
        return num1 / num2
    else:
        print("ERROR: Se ha intentado dividir entre 0.")
        return 0

# Pedimos los datos
operacion = input("Introduzca la operación (+, -, *, /): ")
primerOperando = int(input("Introduzca el primer número: "))
segundoOperando = int(input("Introduzca el segundo número: "))

if(operacion == "+"):
    resultado = suma(primerOperando, segundoOperando)
    print(str(primerOperando) + " + " + str(segundoOperando) + " = " + str(resultado))
elif(operacion == "-"):
    resultado = resta(primerOperando, segundoOperando)
    print(str(primerOperando) + " - " + str(segundoOperando) + " = " + str(resultado))
elif(operacion == "*"):
    resultado = producto(primerOperando, segundoOperando)
    print(str(primerOperando) + " * " + str(segundoOperando) + " = " + str(resultado))
elif(operacion == "/"):
    resultado = division(primerOperando, segundoOperando)
    print(str(primerOperando) + " / " + str(segundoOperando) + " = " + str(resultado))
else:
    print("ERROR: No se ha introducido bien la operación.")