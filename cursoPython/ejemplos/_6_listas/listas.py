

# listas
print("LISTA CON 3 ELEMENTOS")
lista = [1, 2, 3]
print(lista[0])
print(lista[1])
print(lista[2])

# Extra
print(lista[-1])

print(lista)

print("AÑADIMOS ELEMENTOS A LA LISTA")
lista.append(4)
print(lista[3])
print(lista)

print("ELIMINAMOS ELEMENTOS DE LA LISTA")
lista.remove(2)
print(lista)

print("INSERTAMOS ELEMENTOS EN LA LISTA")
lista.insert(2, "Hola")
print(lista)

print("ELIMINAMOS ELEMENTO POR ÍNDICE")
del lista[2]
print(lista)

print("MODIFICAMOS ELEMENTO DE LA LISTA")
lista[1] = 2
lista[2] = 3
print(lista)