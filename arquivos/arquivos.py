
# arq = open('arquivo.txt','w+')
# arq.write('1\n')
# arq.write('2\n')
# arq.write('3\n')
# arq.write('4\n')
# arq.write('5\n')
# arq.write('6\n')
# arq.write('7\n')
# arq.close()

# arq = open('arquivo.txt', 'r')

# for linha in arq.readline():
#     print(linha)

# numeros = [int(numero) for numero in arq.readline()]
# print(numeros)

# with open('arquivo.txt', 'r') as file:
#     for line in file:
#         print(line.strip().split(',')[1])
#     numbers = [int(number) for number in file.readline()]
#
# print(numbers)

andrey = 'Andrey Masiero'
giroto = 'Carlos Giroto'

print('%-15s é o cara' % andrey)
print(f'{giroto:<15} é o cara') # 15 espaços alinhado na esquerda
print(f'{giroto:>15} é o cara') # 15 espaços alinhado na direita
print(f'{giroto:^15} é o cara') # 15 espaços alinhado na centrelizado

