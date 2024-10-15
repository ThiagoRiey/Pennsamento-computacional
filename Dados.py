import random
dado = random.randint(1, 10)

print('Atacar: ')
if dado >= 7:
  print(f'Dado: {dado}. Ataque bem sucedido!')

elif dado > 1 and dado < 7:
  print(f'Dado: {dado}. Você errou o golpe!')

else:
  print(f'Dado; {dado}. erro crítico. Voc~e quebrou o braço')
