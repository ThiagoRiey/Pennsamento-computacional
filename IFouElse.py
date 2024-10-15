idade = int(input('Digite a sua idade: ))

if idade >= 18:
  print('Você pode entrar no cinema')

else:
  print('Você não pode entrar no cinema')
  resposta = input('Você esta com algum responsavel? ')
  if resposta == 'sim' or resposta == "SIM":
          print('pode entrar')

  else resposta == 'não' or resposta == 'NÃO':
          print('Não pode entrar')
              
