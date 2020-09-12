from funcoes import utils, matematica
import old_funcoes as f

# UTILIZANDO AS FUNÇÕES
a = utils.entrada_de_numero_pelo_usuario(mensagem="Digite um numero: ")
b = utils.entrada_de_numero_pelo_usuario(mensagem="Digite outro numero: ")

resultado = matematica.operacao_aritmetica(a, b)
utils.exibi_mensagem_para_usuario(resultado)

c = utils.entrada_de_numero_pelo_usuario(mensagem="Digite um numero: ")
d = utils.entrada_de_numero_pelo_usuario(mensagem="Digite outro numero: ")

resultado = matematica.operacao_aritmetica(numero2=c, numero1=d, operacao='-')
utils.exibi_mensagem_para_usuario(resultado)

# Programacao Funcional
print(f.operacao(numero1=c, numero2=d, funcao=lambda x, y: x + y))
print(f.operacao(c, d, lambda x, y: x - y))
print(f.operacao(c, d, lambda x, y: x * y))
print(f.operacao(c, d, lambda x, y: x / y))
