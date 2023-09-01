"""
Programa que lê uma string e exibe na tela se ela é um
palíndromo ou não.
"""

print('='*30)
print(f'{"Detector de Palíndromo":=^30}')
print('='*30)
FRASE = input('Digite uma frase qualquer: ').strip().upper()
print('='*30)

FRASE = FRASE.split()
FRASE = ''.join(FRASE)
FRASE_INVERTIDA = ''
for contador in range(len(FRASE) - 1, -1, -1):
    if FRASE.isspace():
        pass
    else:
        FRASE_INVERTIDA += FRASE[contador]
if FRASE_INVERTIDA == FRASE:
    print(f'{FRASE} ao inverso fica {FRASE_INVERTIDA}')
    print('É um palíndromo!')
else:
    print(f'{FRASE} ao inverso fica {FRASE_INVERTIDA}')
    print('Não é um palíndromo.')
