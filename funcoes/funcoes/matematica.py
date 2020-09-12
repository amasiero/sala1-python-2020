def operacao_aritmetica(numero1, numero2, operacao='+'):
    if operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        return numero1 / numero2
    else:
        return numero1 + numero2