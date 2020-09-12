# Exercicio 01
def exibe_piramide_numeros(n):
    for linha in range(1, n + 1):
        for i in range(linha):
            print(linha, end=' ')
        print()


# Exercicio 02
def exibe_piramide_contadora(n):
    for linha in range(1, n + 1):
        for i in range(1, linha + 1):
            print(i, end=' ')
        print()


exibe_piramide_contadora(15)


# Exercicio 03
def soma(a, b, c):
    return a + b + c

