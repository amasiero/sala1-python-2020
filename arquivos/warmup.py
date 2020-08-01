# Gerar um lista de números aleatórios entre 20 e 60 E separar em tuplas os PARES e os IMPARES

import random

quantidade_elementos = int(input("Digite a quantidade de elementos: "))

numeros = []
cont = 0
while cont <= quantidade_elementos:
    numero = random.randint(20, 60)
    numeros.append(numero)
    cont += 1

lista_pares = []
lista_impares = []

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

tupla_pares = tuple(lista_pares)
tupla_impares = tuple(lista_impares)

print(f'O numeros pares são {tupla_pares}')
print(f'O numeros impares são {tupla_impares}')


pares = list(filter(lambda numero: numero % 2 == 0, numeros))
impares = list(filter(lambda numero: numero % 2 == 1, numeros))
print(pares)
print(impares)




