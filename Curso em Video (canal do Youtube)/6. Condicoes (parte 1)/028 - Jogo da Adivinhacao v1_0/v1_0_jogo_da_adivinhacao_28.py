"""
Programa que pede pro usuário digitar um valor de 1 a 5. Após isso, o
programa gera um  número aleatório de 1 a 5 e mostra na tela se o usuário
acertou ou errou o número gerado.
"""

from random import randint
from time import sleep
print('='*31)
print(f'{"Jogo da Adivinhação":=^31}')
print('='*31)
numero_escolhido = int(input('Adivinhe um número de 1 a 5: '))
print('Pensando em um número de 1 a 5...')
sleep(3)
numero_gerado = randint(1, 5)
print('='*45)
if numero_gerado == numero_escolhido:
    print(f'Você venceu! O número gerado foi o número {numero_gerado}!')
else:
    print(f'Você perdeu! O número gerado foi o número {numero_gerado}.')
