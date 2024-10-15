#Vão informar quantos estão reprovados e quantos aprovados

notas = [0, 10, 10, 10, 9, 8, 5, 4, 2, 6, 6, 5, 4]
aprovados = []
reprovados = []

for nota in notas:
  if nota >= 7:
    aprovados.append(nota)
  else:
    reprovados.append(nota)

num_reprovados = len(reprovados)
num_aprovados = len(aprovados)
print(f'Número de alunos aprovados: {num_aprovados}\n Números de alunos reprovados: {num_reprovados}')
