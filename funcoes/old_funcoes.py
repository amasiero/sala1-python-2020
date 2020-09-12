# CRIANDO AS FUNÇÕES
def entrada_de_numero_pelo_usuario(mensagem):
    return int(input(mensagem))


def exibi_mensagem_para_usuario(mensagem):
    print(mensagem)


def operacao_aritmetica(numero1, numero2, operacao='+'):
    if operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        return numero1 / numero2
    else:
        return numero1 + numero2


def operacao(numero1, numero2, funcao):
    return funcao(numero1, numero2)
