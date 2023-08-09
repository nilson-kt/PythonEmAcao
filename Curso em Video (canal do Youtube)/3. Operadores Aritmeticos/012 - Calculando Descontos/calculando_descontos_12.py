"""
Algoritmo que lê o valor de um produto e exibe na tela o seu preço com 5% de desconto.
"""

valor = float(input('Digite o preço do produto: R$'))
valor_com_desconto = valor - valor * 0.05
print(f'O valor R${valor:.2f}, com 5% de desconto, fica: R${valor_com_desconto:.2f}')
