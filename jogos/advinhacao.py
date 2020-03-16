import random

print("***********************************")
print("  Bem-vindo ao Jogo da Advinhação  ")
print("***********************************")

numero_secreto = random.randint(1, 100)
print(numero_secreto)
numero_escolhido = input("Escolha um número: ")
numero_escolhido = int(numero_escolhido)

if numero_secreto == numero_escolhido:
  print("Uhuuuuu!!!")
  print("Parabéns!!!!!")
  print("Voce eh foooogoooo =D")
else:
  print("Errrrooooouuuuu!!!! =(")

print("Fim do Jogo")