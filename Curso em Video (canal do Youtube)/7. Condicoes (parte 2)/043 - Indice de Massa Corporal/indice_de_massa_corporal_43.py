"""
Programa que pergunta o peso e a altura de uma pessoa, calcula
o IMC (Índice de Massa Corporal) e exibe, conforme esse índice,
se a pessoa está abaixo do peso, no peso ideal, em sobrepeso,
em obesidade ou em obesidade mórbida.
"""

peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = round(peso / pow(altura, 2), 1)
mensagem = f"Seu IMC é {imc}\n"

if imc < 18.5:
    print(f'{mensagem}Você está abaixo do peso!')
elif 25 > imc >= 18.5:
    print(f'{mensagem}PARABÉNS! Você está no peso normal!')
elif 30 > imc >= 25:
    print(f'{mensagem}Você está em sobrepeso!')
elif 40 > imc >= 30:
    print(f'{mensagem}Você está em obesidade!')
else:
    print(f'{mensagem}Você está em obesidade mórbida! Cuidado!')
