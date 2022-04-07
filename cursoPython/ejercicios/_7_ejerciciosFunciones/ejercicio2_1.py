

# Creamos la función para retirar dinero
def retiraDinero(dineroCuenta, dineroARetirar):
    return dineroCuenta - dineroARetirar

# Creamos la función para ingresar dinero
def ingresaDinero(dineroCuenta, dineroAIngresar):
    return dineroCuenta + dineroAIngresar

# creamos la variable que contendrá el dinero que tenemos en el banco
dineroBanco = input("Introduzca cuánto dinero tiene en el banco: ")
dineroBanco = float(dineroBanco)
print("Dinero en el banco: " + str(dineroBanco))

# Realizamos los movimientos
cantidadARetirar = input("Introduzca una cantidad a retirar: ")
cantidadARetirar = float(cantidadARetirar)
dineroBanco = retiraDinero(dineroBanco, cantidadARetirar)
print("Dinero en el banco: " + str(dineroBanco))

cantidadAIngresar = input("Introduzca una cantidad a ingresar: ")
cantidadAIngresar = float(cantidadAIngresar)
dineroBanco = ingresaDinero(dineroBanco, cantidadAIngresar)
print("Dinero en el banco: " + str(dineroBanco))