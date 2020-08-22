# Exercicio 1
with open('arquivo.txt', 'r') as arquivo:
    print(f'Total de linhas existentes é {len(arquivo.readlines())}.')

# Exercicio 2
with open('arquivo.txt', 'r') as arquivo:
    vogais = 0
    for linha in arquivo:
        vogais += len([letra for letra in linha if letra in 'aeiou'])
    print(f'Total de vogais é {vogais}.')

# Exercicio 3
with open('arquivo.txt', 'r') as arquivo:
    vogais = 0
    consoantes = 0
    for linha in arquivo:
        vogais += len([letra for letra in linha if letra in 'aeiou'])
        consoantes += len([letra for letra in linha if letra in 'bcdfghjklmnpqrstvwyxz'])
    print(f'Total de vogais é {vogais} e o de consoantes é {consoantes}.')

# Exercicio 4
with open('arquivo.txt', 'r') as arquivo:
    caracter = input('Informe um caracter: ')
    letras = 0
    for linha in arquivo:
        letras += len([letra for letra in linha if letra == caracter])
    print(f'Total de {caracter} é {letras}.')

# Exercicio 5
with open('arquivo.txt', 'r') as arquivo:
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    letras = [0 for letra in alfabeto]
    for linha in arquivo:
        for indice, letra in zip(range(len(alfabeto)), alfabeto):
                letras[indice] += linha.count(letra)

    resultado = 'Total de: '
    for letra, quantidade in zip(alfabeto, letras):
        resultado += f'{letra}="{quantidade}" '
    print(resultado)

# Exercício 6
import re
with open('arquivo.txt', 'r') as file:
    for line in file:
        text = line.strip()
        # text = text.replace('a', '*') usando a funcao replace do string
        text = re.sub(r'[aeiou]', '*', text)
        print(text)

# Exercício 7
origem = input('Digite o nome do arquivo de origem: ')
destino = input('Digite o nome de arquivo de destino: ')

with open(origem, 'r') as o:
    with open(destino, 'w') as d:
        for linha in o:
            d.write(linha.upper())

# converte apenas as vogais para maiusculo
# texto = 'Como podemos ver, uma lista foi retornada'
# def toUpperCase(char):
#   return char.group(0).upper()
#
# novo_texto = re.sub(r'[aeiou]', toUpperCase, texto)
# print(novo_texto)
