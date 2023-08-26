"""
Programa que lê uma string qualquer e substitui todas as ocorrências de 'a',
seja em letra minúscula ou maiúscula, por "$".
"""

string = input('\033[1:32mDigite uma String: \033[m')
string = string.replace("a", "$")
string = string.replace("A", "$")
print(f'\033[1:32mString modificada: \033[1:31m{string}')
