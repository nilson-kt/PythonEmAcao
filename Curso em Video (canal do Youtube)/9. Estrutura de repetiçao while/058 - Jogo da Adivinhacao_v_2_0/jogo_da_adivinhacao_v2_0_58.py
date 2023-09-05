"""
Programa que simula um jogo de adivinhação. O programa gera um número
aleatório de 0 a 10 e pede para o usuário adivinhar qual foi esse número
gerado. O usuário terá várias tentativas até que ele acerte o número gerado
pelo computador.
"""

from random import randint

numero_gerado = randint(0, 10)
print('='*30)
print(f'{"JOGO DA ADIVINHAÇÃO":=^30}')
print('='*30)
print('\033[1:33mO computador irá gerar um número de 0 a 10. Tente adivinhar!\033[m')
numero_escolhido = int(input('Digite um número de 0 a 10: '))
CONTADOR = 1
while numero_escolhido != numero_gerado:
    CONTADOR += 1
    print(f'\033[1:31mVocê errou! O computador gerou o número {numero_gerado}!\033[m')
    numero_escolhido = int(input('Tente novamente: '))
    numero_gerado = randint(0, 10)
if numero_escolhido == numero_gerado:
    print(f'\033[1:32mParabéns! O computador gerou o número {numero_gerado}. Você venceu!')
    print(f'Você acertou na {CONTADOR}ª tentativa!')
