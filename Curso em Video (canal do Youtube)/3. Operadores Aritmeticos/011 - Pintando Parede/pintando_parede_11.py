"""
Programa que lê, em metros, a largura e altura de uma parede e exibe sua dimensão e área,
bem como a quantidade de tinta, em litros, necessária para pintá-la.
"""

largura = float(input('Digite, em metros, a largura da parede: '))
altura = float(input('Agora, digite, em metros, a altura da parede: '))
area = float(largura * altura)
print(f'A parede tem a dimensão {largura:.2f}x{altura:.2f} e sua área é igual a {area:.2f}m²')
print(f'Nesse caso, você precisa de {area/2:.2f} litros para pintar a parede')
