"""
Programa que nega ou aceita um pedido de empréstimo para a compra
de uma casa, com base no valor do imóvel, no salário do comprador e
no tempo estabelecido para a quitação do empréstimo.
"""

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite seu salário: R$'))
anos = int(input('Em quantos anos o senhor vai pagar?: '))
meses = anos * 12
prestacao_mensal = valor_casa / meses

if prestacao_mensal < salario*0.30:
    print(f'\033[1:32mPara pagar uma casa de R${valor_casa:.2f}, a prestação '
          f'será de R${prestacao_mensal:.2f}\nO empréstimo pode ser concedido!')
else:
    print(f'\033[1:31mPara pagar uma casa de R${valor_casa:.2f}, a prestação '
          f'será de R${prestacao_mensal:.2f}\nEmpréstimo negado!')
