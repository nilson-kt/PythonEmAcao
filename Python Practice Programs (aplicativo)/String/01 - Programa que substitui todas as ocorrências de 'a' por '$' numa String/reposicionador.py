"""
Programa que lê uma string qualquer e substitui todas as ocorrências de 'a',
seja em letra minúscula ou maiúscula, por "$".
"""

string = input('Digite uma String: ')
string = string.replace("a", "$")
string = string.replace("A", "$")
print(f'String modificada: {string}')
