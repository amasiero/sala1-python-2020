# Pedir para o usuário o valor da hora 
valor_hora = float(input("Digite o seu valor hora: "))
# Pedir para o usuário a quantidade de horas trabalhadas
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
# Calcular salario bruto
salario_bruto = valor_hora * horas_trabalhadas
# Calcular desconto IR
## até 900 - isento
ir = 0
percentual = 0
## até 1500 - 5%
if salario_bruto > 900 and salario_bruto <= 1500:
  ir = salario_bruto * 0.05
  percentual = 5
  ## até 2500 - 10%
elif salario_bruto > 1500 and salario_bruto <= 2500:
  ir = salario_bruto * 0.1
  percentual = 10
  ## acima 2500 - 20%
elif salario_bruto > 2500:
  ir = salario_bruto * 0.2
  percentual = 20
# Calcular 3% desconto do sindicato
sindicato = salario_bruto * 0.03
# Calcular 10% desconto do INSS
inss = salario_bruto * 0.1
# Calcular 11% do FGTS (não descontado)
fgts = salario_bruto * 0.11
# Calcular salario liquido que é salario bruto menos os descontos
salario_liquido = salario_bruto - (ir + sindicato + inss)
# Exibir demonstrativo de pagamento
print(f'Salário Bruto: ({valor_hora} * {horas_trabalhadas})\t: R$ {salario_bruto:.2f}')
print(f' (-) IR ({percentual}%)\t\t\t: R$ {ir:.2f}')
print(f' (-) INSS (10%)\t\t\t: R$ {inss:.2f}')
print(f' (-) Sindicato (3%)\t\t: R$ {sindicato:.2f}')
print(f'FGTS (11%)\t\t\t: R$ {fgts:.2f}')
print(f'Total de descontos\t\t: R$ {(ir + sindicato + inss):.2f}')
print(f'Salário Líquido\t\t\t: R$ {salario_liquido:.2f}')