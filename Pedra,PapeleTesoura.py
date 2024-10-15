from random import randint
from time import sleep

intens = ('pedra' ,'papel' , 'tesoura')

computador = randint(0, 2)

print(''' Suas opções :
[0] pedra
[1] papel
[2] tesoura''')

jogador =int(input('Qual é a sua jogada? :  '))

print('jo')
sleep(1)
print('ken')
sleep(1)
print('pô')
sleep(2)
print('-=' * 11)

print(f'Computador jogou: {intens[computador]}')
print(f'jogador jogou: {intens[jogador]}')
print('-=' * 11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
      print('EMPATE')
    elif jogador == 1:
      print('Jogador venceu!')
    elif jogador ==2:
      print('Computador venceu!')
    else:
      print('jogada inválida!')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
      print('Computador venceu!')
    elif jogador == 1:
      print('EMPATE!')
    elif jogador ==2:
      print('Jogador venceu!')
    else:
      print('jogada inválida!')


elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
      print('Jogador venceu!')
    elif jogador == 1:
      print('COMPUTADOR venceu!')
    elif jogador ==2:
      print('EMPATE!')
    else:
      print('jogada inválida!')
