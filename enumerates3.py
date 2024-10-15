alunos = ['Alberto', 'Bento', 'Carlos', 'Denis', 'Evaldo', 'Fabiano', 'Gustavo']
notas = [10, 8, 6, 8, 5, 2, 1]
aprovados = []
reprovados = []

for i, nota in enumerate(notas):
    if nota >= 7:
        aprovados.append(f'{alunos[i]}: {nota}')
    else:
        reprovados.append(f'{alunos[i]}: {nota}')

print('Aprovados: \n-------------')
print('\n'.join(aprovados))
print('\nReprovados: \n-------------')
print('\n'.join(reprovados))
