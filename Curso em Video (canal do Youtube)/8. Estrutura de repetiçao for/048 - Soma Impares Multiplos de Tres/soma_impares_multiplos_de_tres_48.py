"""
Programa que calcula e exibe na tela a soma de todos os números ímpares
que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
"""

SOMA = 0
CONTADOR = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        CONTADOR += 1
        SOMA += numero
print(f"A soma de todos os {CONTADOR} valores é igual a {SOMA}")
