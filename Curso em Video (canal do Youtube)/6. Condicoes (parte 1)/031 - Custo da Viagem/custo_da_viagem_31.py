"""
Programa que lê a distância de uma viagem em Km e exibe na tela
o preço dessa viagem dependendo da distância que será percorrida.
"""

distancia = int(input('Digite a distância da viagem em Km: '))
if 1 <= distancia <= 200:
    print(f'O preço da viagem fica R${float(distancia*0.50):.2f}')
elif distancia > 200:
    print(f'O preço da viagem fica R${float(distancia*0.45):.2f}')
else:
    print('Reinicie o programa e e estabeleça uma distância maior que 0Km.')
