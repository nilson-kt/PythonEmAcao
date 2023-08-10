"""
Programa que lê a quantidade de dias pelos quais um carro foi alugado
e a quantidade de kilômetros percorridos e, no final, exibe o preço a pagar pelo aluguel.
"""

dias = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))
km = float(input('Digite a quantidade de Km percorrido(s): '))
preco_km = 0.15 * km
preco_dia = 60 * dias
valor_a_pagar = float(preco_km + preco_dia)
print(f'O preço a pagar é R${valor_a_pagar:.2f}')
