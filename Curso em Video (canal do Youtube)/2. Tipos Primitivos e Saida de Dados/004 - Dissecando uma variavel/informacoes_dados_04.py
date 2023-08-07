"""
Programa que lê uma entrada fornecida pelo usuário e mostra as características desses dados.
"""
dado = input('Digite qualquer coisa: ')
print(f'O tipo dessa variável é: {type(dado)}')
print('É Numérico?:', dado.isnumeric())
print('É Dígito?:', dado.isdigit())
print('É Decimal?:', dado.isdecimal())
print('É Alfanumérico?:', dado.isalnum())
print('É Alfabético?:', dado.isalpha())
print('Está Tudo em maiúsculo?:', dado.isupper())
print('Está Tudo em minúsculo?:', dado.islower())
print('Está Capitalizada?:', dado.istitle())
print('É Espaço?:', dado.isspace())
print('É Imprimível?:', dado.isprintable())
print('É Um identificador válido?:', dado.isprintable())
