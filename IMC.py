peso = float(input('Digite o seu peso: '))
altura = float(input('digite a sua altura: '))

IMC = peso / altura**2

print('IMC: {:.1f}' .format(IMC))

if IMC < 18.5:
  print('Você esta com Magreza')

elif IMC <= 24.9:
  print('Você está saudável')

elif IMC <= 29.9:
  print('Você está sobre peso')

elif IMC <= 34.9:
  print('Você está com Obesidade Grau 1')

elif IMC <= 39.9:
  print('Você está com Obesidade Grau 2')

else:
  print('Você está com Obesidade Morbida')
