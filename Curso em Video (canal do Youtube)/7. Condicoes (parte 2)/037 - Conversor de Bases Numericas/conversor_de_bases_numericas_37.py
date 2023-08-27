"""
Programa que lê um número inteiro qualquer e converte para uma das
bases (binária, octal, hexadecimal).
"""

numero = int(input('Digite um número inteiro qualquer: '))
print('[1] binário\n'
      '[2] octal\n'
      '[3] hexadecimal')

base_de_conversao = int(input('Qual será a base de conversão?: '))
if base_de_conversao == 1:
    print(f'{numero} convertido para binário é igual a {bin(numero)[2:]}')
elif base_de_conversao == 2:
    print(f'{numero} convertido para octal é igual a {oct(numero)[2:]}')
elif base_de_conversao == 3:
    print(f'{numero} convertido para hexadecimal é igual a {hex(numero)[2:]}')
else:
    print('Por favor, reinicie o programa e digite um valor que '
          'corresponda a alguma das opções listadas acima.')
