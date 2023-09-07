"""
Programa que lê vários números inteiros pelo teclado e mostra a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa pergunta ao usuário
se ele quer ou não continuar a digitar valores.
"""

RESPOSTA = "Ss"
MEDIA = 0
SOMA = 0
QUANTIDADE_NUMEROS = 0
MAIOR = 0
MENOR = 0
while RESPOSTA not in "Nn":
    numero = int(input("Digite um número: "))
    QUANTIDADE_NUMEROS += 1
    SOMA += numero
    RESPOSTA = str(input("Deseja continuar? [S/N]: "))
    if numero > MAIOR:
        MAIOR = numero
    if QUANTIDADE_NUMEROS == 1:
        MENOR = numero
    if numero < MENOR:
        MENOR = numero
    while RESPOSTA not in "NnSs" or RESPOSTA == "":
        RESPOSTA = str(input("Opção inválida. Digite [S] para continuar ou [N] para encerrar: "))
MEDIA = SOMA / QUANTIDADE_NUMEROS
print("="*30)
print(f"Quantidade de Números: {QUANTIDADE_NUMEROS}")
print(f"Maior número: {MAIOR}")
print(f"Menor número: {MENOR}")
print(f"Média: {MEDIA:.2f}")
