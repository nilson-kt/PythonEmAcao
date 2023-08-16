"""
Programa que lê um nome completo e exibe na tela o mesmo nome em
maiúsculo, minúsculo, bem como a quantidade de caracteres na String
(desconsiderando os espaços) e o número de caracteres no primeiro nome.
"""

nome = input('Digite seu nome completo: ')
nome = nome.strip()
print(f'Em maiúsculo: {nome.upper()}')
print(f'Em minúsculo: {nome.lower()}')
print(f'Número de letras: {len("".join(nome.split()))}')
print(f'Número de letras no primeiro nome: {len(nome.split()[0])}')
