# Exibir tabela de preços
print('\t\t\tAté 5 kg\t\tAcima de 5 kg')
print(u'\u2022','Morango\t\tR$ 2,50 por kg\t\tR$ 2,20 por kg')
print(u'\u2022','Maçã\t\t\tR$ 1,80 por kg\t\tR$ 1,50 por kg')
# Informar quantidade kg maçã
quilos_maca = float(input('Digite a quantidade de quilos para maçã: '))
# Informar quantidade kg morango
quilos_morango = float(input('Digite a quantidade de quilos para morango: '))
# Calcular quantidade de quilos total
quilos_total = quilos_morango + quilos_maca
# Calcular quantidade do valor total
if quilos_maca > 5:
	valor_maca = quilos_maca * 1.5
else:
	valor_maca = quilos_maca * 1.8

if quilos_morango > 5:
	valor_morango = quilos_morango * 2.2
else:
	valor_morango = quilos_morango * 2.5

valor_total = valor_maca + valor_morango
# Calcular valor do desconto
desconto = 0
if valor_total > 25 or quilos_total > 8:
	desconto = valor_total * 0.1
# Calcular pagamento total
pagamento = valor_total - desconto
print(f'O total em quilos é {quilos_total:.1f} kg.')
print(f'O valor total é R$ {valor_total:.2f}.')
print(f'O desconto aplicado é R$ {desconto:.2f}.')
print(f'O valor pago é R$ {pagamento:.2f}.')