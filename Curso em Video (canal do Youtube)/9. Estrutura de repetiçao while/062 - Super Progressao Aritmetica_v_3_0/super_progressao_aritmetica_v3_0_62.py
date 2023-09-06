"""
Programa que lê o primeiro termo e a razão de uma progressão aritmética
e exibe na tela os 10 primeiros termos.

Ao finalizar a exibição dos 10 primeiros termos, o programa pergunta ao
usuário quantos termos a mais ele quer que sejam mostrador. O sistema
será encerrado quando o usuário responder que ele quer que sejam exibidos
0 termos.
"""

print("Gerador de PA")
print('-='*10)
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
CONTADOR = 10
QUANTIDADE_TERMOS = 10
RESPOSTA = 0
while CONTADOR > 0:
    print(f"{termo} >", end=" ")
    termo += razao
    CONTADOR -= 1
    if CONTADOR == 0:
        print("PAUSA")
        RESPOSTA = int(input("Quantos termos você quer mostrar a mais?: "))
        CONTADOR = RESPOSTA
        QUANTIDADE_TERMOS += RESPOSTA
if RESPOSTA == 0:
    print(f"Progressão finalizada com {QUANTIDADE_TERMOS} termos mostrados.")
