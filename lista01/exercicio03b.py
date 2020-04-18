notas = []
contador = 1

quantidade_notas = int(input("Informe quantas notas precisam ser digitadas: "))

while(contador <= quantidade_notas):
  numero = float(input("Informe uma nota: "))
  notas.append(numero)
  contador += 1

soma = 0
for nota in notas:
  soma += nota

media = soma / len(notas)
print("A media foi {}".format(round(media, 2)))