#Vendedor
vendedor = float(input('Funcionario 1 vendeu R$: '))

#salarios
salario = 1200

if vendedor  <1000 :
  print('Você não bateu a meta, seu salario é de R$:{}'.format(salario))

elif vendedor <2000:
 bonus = salario * 0.1
 novo_salario = salario + bonus
 print('Parabens você ganhou R$: {}'.format(novo_salario))

else:
 vendedor >=2000
 bonus =salario * 0.15
 novo_salario = salario + bonus
 print('Parabens você ganhou R$: {}'.format(novo_salario))
