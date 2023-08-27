"""
Programa que lê dois números e inteiros e mostra na tela qual
dos dois é o maior. Caso os valores sejam iguais, o programa
mostra que esses valores são iguais.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('\033[1:32mO \033[1:33mPRIMEIRO\033[m \033[1:32mvalor é maior.\033[m')
elif n2 > n1:
    print('\033[1:32mO \033[1:33mSEGUNDO\033[m \033[1:32mvalor é maior.\033[m')
else:
    print('\033[1:31m\033[4:33mNão\033[m existe valor maior. Os dois valores são IGUAIS.')
