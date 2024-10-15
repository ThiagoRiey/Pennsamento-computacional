print('Sua media tem que ser 7 ou maior para ser aprovado!!')
p1 = float(input('Digite a sua nota da p1: ')
p2 = float(input('Digite a sua nota da p2: ')

media = (p1 + p2) / 2

print(' A sua média: {:.1f}' .format(media))

if media >= 7:
  print('Parabéns você foi aprovado! :^D')

else:
  print('Infelizmente você foi reprovado  :(')
