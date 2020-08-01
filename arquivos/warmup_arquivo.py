from random import randint

quantidade_de_numeros = int(input('Digite o tamanho da lista: '))
with open('numeros.txt', 'w') as numeros:
    cont = 0
    while cont < quantidade_de_numeros:
        numero_aleatorio = randint(20, 60) # valores entre 20 e 60, inclusive
        numeros.write(str(numero_aleatorio) + '\n')
        cont += 1 # cont = cont + 1


with open('numeros.txt', 'r') as numeros:
    lista_pares = []
    lista_impares = []

    for linha in numeros:
        numero = int(linha.strip())
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)


    tupla_pares = tuple(lista_pares)
    tupla_impares = tuple(lista_impares)

    print(f'A tupla de pares é {tupla_pares}')
    print(f'A tupla de impares é {tupla_impares}')
    