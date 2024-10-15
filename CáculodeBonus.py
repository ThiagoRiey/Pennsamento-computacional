#funcionarios
vendedor1 = float(input('Funcionario 1 vendeu R$: '))
vendedor2 = float(input('Funcionario 2 vendeu R$: '))
vendedor3 = float(input('Funcionario 3 vendeu R$: '))

#Salario
salario = 1000
meta = 1000

if vendedor1 >= 1000:
  bonus = vendedor1 * 0.1
  novo_salario = salario + bonus
  print('Parabens você ganhou R$: {}' .format(novo_salario))

else:
  print('Você não bateu a meta e recebeu R$: {}' .format(salario))

if vendedor2 >= 1000:
  bonus = vendedor2 * 0.1
  novo_salario = salario + bonus
  print('Parabens você ganhou R$: {}'.format(bonus + salario))

else:
  print('Você não bateu a meta e recebeu R$: 1000')

if vendedor3 >= 1000:
  bonus = vendedor3 * 0.1
  novo_salario = salario + bonus
  print('Parabens você ganhou R$: {:.2f}'.format(bonus + salario))

else:
  print('Você não bateu a meta e recebeu R$: 1000')
