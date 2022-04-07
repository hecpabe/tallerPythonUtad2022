

# funciones

def suma(num1, num2):
    return num1 + num2

def saluda():
    print("Holaaaa!!!")

def esNegativo(num):
    if(num < 0):
        return True
    else:
        return False

print("EJECUTAMOS LA SUMA")
primerSumando = 5
segundoSumando = 3
resultadoSuma = suma(primerSumando, segundoSumando)
print(str(primerSumando) + " + " + str(segundoSumando) + " = " + str(resultadoSuma))

print("EJECUTAMOS EL SALUDO")
saluda()

print("EJECUTAMOS ES NEGATIVO")
primerNumero = 7
segundoNumero = -9
print("Comprobamos si " + str(primerNumero) + " es negativo:")
print(esNegativo(primerNumero))
print("Comprobamos si " + str(segundoNumero) + " es negativo")
print(esNegativo(segundoNumero))