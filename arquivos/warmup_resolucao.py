# Gerar um lista de números aleatórios entre 20 e 60 E separar em tuplas os PARES e os IMPARES
from random import randint

quantidade_de_numeros = int(input('Digite o tamanho da lista: '))
numeros = []
cont = 0

while cont < quantidade_de_numeros:
    numero_aleatorio = randint(20, 60) # valores entre 20 e 60, inclusive
    numeros.append(numero_aleatorio)
    cont += 1 # cont = cont + 1

lista_pares = []
lista_impares = []

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)


tupla_pares = tuple(lista_pares)
tupla_impares = tuple(lista_impares)

print(f'A tupla de pares é {tupla_pares}')
print(f'A tupla de impares é {tupla_impares}')
