# Tuplas

t = 'a', 'b', 'c', 'd', 'e'
print(t)
print(type(t))
print(t[2])

palavras = ('Ola', 'Python', 'eh', 'muito', 'legal')
print(palavras)
print(palavras[0])

print('Ola Python')

texto = 'Ola Python'
print(texto)

print(type(texto))
print(type(palavras[0]))
print(type('Ola Python'))

t = tuple()
print(t)
print(type(t))

t = tuple('lupin')
print(t)
print(type(t))

lista_frutas = ['mamao', 'manga', 'pera', 'maca', 'laranja', 'uva']
lista_frutas[3] = 'maçã'
print(lista_frutas)
print(type(lista_frutas))

tupla_frutas = tuple(lista_frutas)
print(tupla_frutas)
print(type(tupla_frutas))
#tupla_frutas[3] = 'jaboticaba' # Não funciona para tupla

comparacao = (0, 1, 2) < (0, 2, 4)
print(comparacao)

dentro = 10 in (10, 20, 30)
print(dentro)

email = 'andrey.masiero@germinare.org.br'
['andr', 'y.masi', 'ro@g', 'rminar', '.org.br']
print(email.split('e'))
usuario, dominio = email.split('@')
print(usuario)
print(dominio)

print(max(1, 2, 3))

pessoas = ['Breno', 'Gabi', 'Pardim', 'Enzo', 'Samantha', 'Hellen']

print(zip(pessoas, tupla_frutas))
print(list(zip(pessoas, tupla_frutas)))

for pessoa, fruta in zip(pessoas, tupla_frutas):
	print(pessoa, 'gosta de', fruta)

import random
acoes = ('vazio', 'monstro', 'aliado')
print(acoes[random.randint(0,2)])
