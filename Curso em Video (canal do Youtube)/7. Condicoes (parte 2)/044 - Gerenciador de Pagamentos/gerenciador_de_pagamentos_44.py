"""
Este programa simula uma experiência de compras, calculando preços
com descontos e juros para diferentes formas de pagamento.
Com base na escolha, o programa calcula e exibe o valor final a ser pago.
Certifique-se de inserir valores numéricos válidos e seguir as instruções do programa.
"""

print(f'{"LOJA INCRÍVEL":=^30}')
preco_normal = float(input('\033[1:33mDigite o preço do produto: R$\033[m'))

print(f'{"="*30}\n'
      'FORMAS DE PAGAMENTO\n'
      '[1] à vista (dinheiro/cheque)\n'
      '[2] à vista no cartão\n'
      '[3] em até 2x no cartão\n'
      '[4] 3x ou mais no cartão\n'
      f'{"="*30}')

condicao_pag = int(input('Digite a forma de pagamento: '))
if condicao_pag == 1:
    preco_com_desconto = preco_normal - preco_normal * 0.10
    print(f'{"="*30}\n'
          f'Você obteve um desconto de 10%!\n'
          f'Sua compra vai ficar R${preco_com_desconto:.2f}')
elif condicao_pag == 2:
    preco_com_desconto = preco_normal - preco_normal * 0.05
    print(f'{"="*30}\n'
          f'Você obteve um desconto de 5%!\n'
          f'Sua compra vai ficar R${preco_com_desconto:.2f}')
elif condicao_pag == 3:
    print(f'{"=" * 30}\n'
          f'Sua compra vai ficar parcelada em 2x de R${preco_normal / 2:.2f}\n'
          f'Somando as parcelas, o valor final fica R${preco_normal:.2f}')
elif condicao_pag == 4:
    parcelas = int(input('Quantas parcelas?: '))
    if parcelas >= 3:
        preco_com_juros = preco_normal + preco_normal * 0.20
        print(f'{"="*30}\n'
              f'Sua compra vai ficar parcelada em {str(parcelas)}x de '
              f'R${preco_com_juros/parcelas:.2f} com JUROS\n'
              f'O valor R${preco_normal:.2f} obteve JUROS de 20%. '
              f'Somando as parcelas, o valor final '
              f'fica R${preco_com_juros:.2f}')
    elif parcelas == 2:
        print('Por favor, para parcelar em 2x, reinicie o sistema e '
              'digite, na forma de pagamento, a opção [3].')
    else:
        print('Opção inválida! Reinicie o programa e insira, por favor, uma opção válida.')
