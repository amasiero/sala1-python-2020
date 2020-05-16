print('Lojas Tabajara')
while True:
	produtos = []
	print('\nPróximo Cliente\n')
	while True:
		valor_produto = float(input('Digite o valor do produto: '))
		if valor_produto == 0:
			break
		produtos.append(valor_produto)

	total_compra = 0
	print('\nLista de Produtos')
	for produto, id in zip(produtos, range(len(produtos))):
		print(f'Produto {id + 1}: R$ {produto:.2f}')
		total_compra += produto
	print(f'\nTotal: R$ {total_compra:.2f}')
	dinheiro = float(input('\nDigite o valor recebido: '))
	print(f'Dinheiro: R$ {dinheiro:.2f}')
	print(f'Troco: R$ {(dinheiro-total_compra):.2f}')
# para parar o programa Ctrl+C