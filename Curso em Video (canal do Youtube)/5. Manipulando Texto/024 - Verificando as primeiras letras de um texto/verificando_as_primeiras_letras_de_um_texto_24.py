"""
Programa que lê o nome de uma cidade e mostra se esse nome
começa com a palavra "santo".
"""

cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.strip().split(' ')
cidade = cidade[0][:5]
CHECA_TEXTO = str('santo' in cidade.lower())
CHECA_TEXTO = CHECA_TEXTO.replace('True', 'Verdade')
CHECA_TEXTO = CHECA_TEXTO.replace('False', 'Falso')
print(CHECA_TEXTO)
