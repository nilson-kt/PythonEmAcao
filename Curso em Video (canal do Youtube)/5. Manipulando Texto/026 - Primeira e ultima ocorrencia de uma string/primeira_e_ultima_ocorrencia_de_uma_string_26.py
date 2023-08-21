"""
Programa que lê uma frase qualquer e mostra na tela:
-a quantidade de ocorrências da letra "A";
-a posição da primeira ocorrência;
-a posição da última ocorrência
"""

frase = input('Digite uma frase qualquer: ').lower().strip()
print(f'Quantidade de ocorrências da letra "A": {frase.count("a")}')
print(f'Posição de primeira aparição: {frase.find("a")+1}')
print(f'Posição de última aparição: {frase.rfind("a")+1}')
