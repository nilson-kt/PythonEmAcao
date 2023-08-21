"""
Programa que lê a velocidade de um carro (Km/h) e verifica se
essa velocidade está acima de 80 Km/h. Caso esteja, o programa
exibe ao usuário que ele ultrapassou o limite e que deve pagar
uma multa de 7 reais a cada kilômetro ultrapassado.

No final, o programa exibe uma mensagem de bom dia.
"""


from time import sleep

#Painel
print('='*30)
print(f'{"RADAR ELETRÔNICO":=^30}')
print('='*30)

#Escopo de variáveis
velocidade = int(input('Digite a velocidade do seu carro (Km/h): '))

#Código
print('='*30)
print('ANALISANDO A VELOCIDADE...')
sleep(3)
print('='*30)
if velocidade > 80:
    print('Você ultrapassou o limite de 80 Km/h e foi multado!\n'
          f'Sua multa é de R${float((velocidade - 80) * 7):.2f} reais!')
print('Tenha um bom dia! Dirija com segurança!')
