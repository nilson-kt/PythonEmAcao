"""
Programa que lê um número inteiro qualquer e exibe na tela
a sua tabuada.
"""

numero = int(input('Digite um número para ver sua tabuada: '))
for contador in range(1, 11):
    print(f"{numero} X {contador} = {numero*contador}")
