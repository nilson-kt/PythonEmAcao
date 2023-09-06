"""
Programa que exibe termos da Sequência de Fibonacci de acordo com
a quantidade digitada pelo usuário.
"""

numero = int(input("Quantos termos você quer mostrar?: "))
CONTADOR_1 = 1
CONTADOR_2 = 0
A = 0
B = 0
C = 1
STRING = ''
while CONTADOR_1 < numero+1:
    STRING += f"{B} {C} "
    if CONTADOR_2 < CONTADOR_1:
        A = C
        C += B
    CONTADOR_2 += 1
    if CONTADOR_2 == CONTADOR_1:
        B = C
        C += A
    CONTADOR_2 -= 1
    CONTADOR_2 += 1
    CONTADOR_1 += 1
STRING = STRING.split()
for elemento in range(0, numero):
    print(f"{STRING[elemento]} >", end=' ')
print("FIM")
