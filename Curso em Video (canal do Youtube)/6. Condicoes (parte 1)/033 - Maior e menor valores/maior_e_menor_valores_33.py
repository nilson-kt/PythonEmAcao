"""
Programa que lê três números e exibe na tela qual é o maior
e qual é o menor.
"""

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maior = a
menor = a
if a < b > c:
    maior = b
if a < c > b:
    maior = c
if c > b < a:
    menor = b
if a > c < b:
    menor = c
if a == 0 and b == 0 and c == 0:
    print('Os números são iguais!')
else:
    print(f'O maior número é {maior}\n'
          f'O menor número é {menor}')
