"""
Jogo de Pedra, Papel e Tesoura

Este programa simula o clássico jogo de Pedra, Papel e Tesoura entre um jogador humano
e o computador. O jogador escolhe entre as opções Pedra, Papel e Tesoura, e o computador
faz uma escolha aleatória.

As regras são as seguintes:
- Pedra ganha de Tesoura
- Tesoura ganha de Papel
- Papel ganha de Pedra

Instruções:
1. Execute o programa.
2. Escolha uma das opções: [ 1 ] PEDRA, [ 2 ] PAPEL ou [ 3 ] TESOURA.
3. O programa mostrará a jogada do computador e anunciará o resultado.
"""

from random import randint

print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')

opcoes = 'PEDRA PAPEL TESOURA'.split()
escolha_aleatoria_cpu = randint(1, 3)
escolha_user = int(input('Qual é a sua jogada?: '))
jogada_cpu = opcoes[escolha_aleatoria_cpu - 1]
jogada_user = opcoes[escolha_user - 1]

print('='*30)

print(f'O computador jogou {jogada_cpu}, você jogou {jogada_user}')
checagem = (jogada_user + jogada_cpu).lower()
if 'tesourapapel' in checagem or 'pedratesoura' in checagem or 'papelpedra' in checagem:
    print('Parabéns, você ganhou!')
elif checagem.count(jogada_user.lower()) == 2:
    print('Empate!')
else:
    print('Você perdeu!')
