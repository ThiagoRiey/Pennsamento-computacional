vendedores = ['Jony', 'Luiz', 'Peter', 'Rubens', 'Bruce', 'Clark']
vendas = [12, 10, 20, 50, 10, 25]
#for venda in vendas:
#  print(venda)
for i, venda in enumerate(vendas):
  print(f'{vendedores[i]}: {venda}')

___________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Imprima apenas os valores >= 20, com
# os respectivos vendedores
vendedores = ['Jony', 'Luiz', 'Peter', 'Rubens', 'Bruce', 'Clark']
vendas = [12, 10, 20, 50, 10, 25]

for i, venda in enumerate(vendas):
  if venda >= 20:
    print(f'{vendedores[i]}: {venda}')
