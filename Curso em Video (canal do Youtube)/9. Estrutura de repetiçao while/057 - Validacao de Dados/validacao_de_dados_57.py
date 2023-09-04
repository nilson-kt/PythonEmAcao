"""
Programa que lê o sexo de uma pessoa e exibe o sexo na tela.
Obs.: o programa aceita valores de entrada específicos. Caso o usuário
não dê um valor certo, o programa lerá a entrada do usuário até que ele
forneça uma resposta correta.
"""

sexo = input('Informe seu sexo [M/F]: ').upper().strip()
while sexo not in 'MF' or sexo == '':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip()
print(f"\033[1:32mSexo {sexo} registrado com sucesso.")
