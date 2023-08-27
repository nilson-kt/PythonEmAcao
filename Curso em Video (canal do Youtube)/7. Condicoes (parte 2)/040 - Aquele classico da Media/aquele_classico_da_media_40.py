"""
Programa que lê duas notas de um aluno, calcula a média aritmética
e exibe se o aluno está aprovado, reprovado ou de recuperação.
"""

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = round((nota_1 + nota_2) / 2, 1)
print(f'Sua média é igual a {media}')
if media >= 7.0:
    print('APROVADO! Parabéns!')
elif 7.0 > media >= 5.0:
    print('Você está de RECUPERAÇÃO!')
else:
    print('Você está REPROVADO! Tente novamente ano que vem. Não desista!')
