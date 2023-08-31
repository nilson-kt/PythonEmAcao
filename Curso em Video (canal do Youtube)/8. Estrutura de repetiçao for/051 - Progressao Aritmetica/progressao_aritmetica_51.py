"""
Programa que lê o primeiro termo e a razão de uma progressão
aritmética e exibe os 10 primeiros termos dessa progressão.
"""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
progressao = primeiro_termo
for contador in range(1, 11):
    print(progressao, end=' > ')
    progressao += razao
print('Acabou!')
