"""
Programa que lê três segmentos de reta de um triângulo e exibe
na tela se é possível formar um triângulo. Se for possível, o
programa ainda exibe se o triângulo é escaleno, equilátero ou
isósceles.
"""

A = float(input("Digite o primeiro lado: "))
B = float(input("Digite o segundo lado: "))
C = float(input("Digite o terceiro lado: "))
TIPO = 'ESCALENO'
if A + B > C and B + C > A and A + C > B:
    if A == B == C:
        TIPO = 'EQUILÁTERO'
    elif A == B != C or B == C != A or C == A != B:
        TIPO = 'ISÓSCELES'
    print(f"É POSSÍVEL formar o triângulo! O triângulo é \033[1:33m{TIPO}!")
else:
    print('\033[1:33mNÃO\033[m é possível formar um triãngulo!')
