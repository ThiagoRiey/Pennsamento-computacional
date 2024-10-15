alunos = ['Alberto', 'Bento', 'Carlos', 'Denis', 'Evaldo', 'Fabiano', 'Gustavo']
notas = [10, 8, 6, 8, 5, 2, 1]

print('Aprovados: \n-------------')
for i, nota in enumerate(notas):
  if nota >= 7:
    print(f'{alunos[i]}: {nota}')
print('\nReprovados: \n-------------')
for i, nota in enumerate(notas):
  if nota < 7:
    print(f'{alunos[i]}: {nota}')
