"""
Programa que lê vários números inteiros digitados pelo usuário. O programa
só se encerra quando o usuário digita 999. No final, é exibido a quantidade
dos números digitados, bem como a soma entre eles - desconsiderando a flag "999".
"""

NUMERO = 0
SOMA = 0
QUANTIDADE_NUMEROS = 0
while NUMERO != 999:
    SOMA += NUMERO
    NUMERO = int(input("Digite um número [999 para parar]: "))
    if NUMERO != 999:
        QUANTIDADE_NUMEROS += 1
if NUMERO == 999:
    print(f"Ao todo, foram digitados {QUANTIDADE_NUMEROS} números!")
    print(f"A soma entre todos os números é igual a {SOMA}")
