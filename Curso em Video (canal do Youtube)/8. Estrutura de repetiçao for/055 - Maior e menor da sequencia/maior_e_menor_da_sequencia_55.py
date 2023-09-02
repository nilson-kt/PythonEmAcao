"""
Programa que lê o peso de cinco pessoas e exibe na tela
qual é o maior e o menor peso lido.
"""

MAIOR_PESO = 0
MENOR_PESO = 0
for contador in range(1, 6):
    peso = float(input(f"Digite o peso da {contador}ª pessoa: "))
    if contador == 1:
        MENOR_PESO = peso
    if peso > MAIOR_PESO:
        MAIOR_PESO = peso
    else:
        if peso < MENOR_PESO:
            MENOR_PESO = peso
print(f"O maior peso é {MAIOR_PESO}Kg")
print(f"O menor peso é {MENOR_PESO}Kg")
