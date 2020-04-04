def jogar():
  print("***********************************")
  print("    Bem-vindo ao Jogo da Forca     ")
  print("***********************************")

  palavra_secreta = "banana"
  letras_certas = ["_", "_", "_", "_", "_", "_"]

  enforcou = False
  acertou = False
  erros = 0

  #enquanto nao enforcou e nao acertou
  while not enforcou and not acertou:
    print(letras_certas, end="\n\n")
    chute = input("Qual a letra? ")
    chute = chute.strip()
    
    if chute.upper() in palavra_secreta.upper():
      indice = 0
      for letra in palavra_secreta:
        if letra.upper() == chute.upper():
          letras_certas[indice] = letra
        indice = indice + 1
    else:
      erros = erros + 1

    acertou = "_" not in letras_certas
    enforcou = erros == 6

  if acertou:
    print("A palavra era {}.".format("".join(letras_certas)))
    print("Parabéns! Você ganhou!")
  else:
    print("A palavra era {}.".format(palavra_secreta))
    print("You lose!")
    
  print("Fim de jogo.")

    
