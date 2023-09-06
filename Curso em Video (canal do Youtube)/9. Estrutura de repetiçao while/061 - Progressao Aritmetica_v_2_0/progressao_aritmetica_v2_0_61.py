"""
Programa que lê o primeiro termo e a razão de uma progressão aritmética
e exibe na tela os 10 primeiros termos da P.A.
"""

print("Gerador de PA")
print('-='*10)
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
CONTADOR = 10
while CONTADOR > 0:
    print(termo, end=" > " if CONTADOR > 1 else " > FIM")
    termo += razao
    CONTADOR -= 1
