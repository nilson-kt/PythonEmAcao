"""
Programa que lê um número inteiro qualquer, calcula e exibe seu fatorial.
"""

numero = int(input("Digite um número: "))
CONTADOR = numero
FATORIAL = 1
print(f"Calculando {numero}!")
while CONTADOR > 0:
    print(f"{CONTADOR}", end='x' if CONTADOR > 1 else f" = {FATORIAL}")
    FATORIAL *= CONTADOR
    CONTADOR -= 1
