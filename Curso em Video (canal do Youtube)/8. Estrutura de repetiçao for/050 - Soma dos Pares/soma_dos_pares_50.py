"""
Programa que lê seis números e mostra na tela a soma de todos
os números pares digitados. O programa desconsidera números ímpares.
"""

SOMA = 0
NUMEROS_PARES = ''
QUANTIDADE = 0
for contador in range(1, 7):
    numero = int(input(f'Digite o {contador}º número: '))
    if numero % 2 == 0:
        SOMA += numero
        NUMEROS_PARES += str(numero)
        QUANTIDADE += 1
print('='*30)
print(f'Você digitou {QUANTIDADE} número(s) par(es)! Agora vou mostrar a soma de todos eles!')
print(f'{"+".join(NUMEROS_PARES)} = {SOMA}')
