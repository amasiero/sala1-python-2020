
def jogar():
  print("***********************************")
  print("    Bem-vindo ao Jogo da Forca     ")
  print("***********************************")

  palavra_secreta = "banana"

  enforcou = False
  acertou = False

  #enquanto nao enforcou e nao acertou
  while not enforcou and not acertou:
    chute = input("Informe uma letra: ")
    
    indice = 0
    for letra in palavra_secreta:
      if letra == chute:
        print("Encontrei a letra {} na posicao {}.".format(letra, indice))
      indice = indice + 1


  print("Fim de jogo.")

    