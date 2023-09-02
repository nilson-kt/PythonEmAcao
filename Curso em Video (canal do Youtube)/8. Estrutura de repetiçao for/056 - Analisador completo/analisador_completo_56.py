"""
Programa que lê o nome, idade e sexo de 4 pessoas e exibe a
média de idade do grupo, o nome do homem mais velho e a quantidade
de mulheres com menos de 20 anos.
"""
SOMA_IDADES = 0
MAIOR_IDADE = 0
HOMEM_MAIS_VELHO = ''
MULHERES_COM_MENOS_20 = 0
for pessoa in range(1, 5):
    print("="*14)
    print(f"===\033[1:33m{pessoa}ªPESSOA\033[m===")
    print("="*14)
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = int(input("[1] Masculino [2] Feminino: "))
    SOMA_IDADES += idade
    if idade > MAIOR_IDADE and sexo == 1:
        MAIOR_IDADE = idade
        HOMEM_MAIS_VELHO = nome
    if idade < 20 and sexo == 2:
        MULHERES_COM_MENOS_20 += 1
media = SOMA_IDADES / 4
print(f"A média de idade do grupo é {media} anos")
print(f"O nome do homem mais velho é {HOMEM_MAIS_VELHO}, com {MAIOR_IDADE} anos")
print(f"No total, há {MULHERES_COM_MENOS_20} mulheres com menos de 20 anos.")
