# # Aula 3
#
# a = "   Teste   "
# b = 'Teste'
#
# # definindo strings com múltiplas linhas
# c = """Teste"""
# d = '''Teste
# bom dia
# boa tarde
# boa noite
# '''
#
# # mostra conteudo da variavel
# print('Conteudo =', d)
#
# # mostra o comprimento da string
# print('Comprimento', len(d), '\n')
#
# # mostrar o texto em letra maiúscula
# print('Variável A com letra maiúscula:', a.upper())
# # mostrar o texto em letra minúscula
# print('Variável A com letra minúscula:', a.lower(), '\n')
# # mostrar o texto em letra maiúscula
#
# print('Variável B com letra maiúscula:', b.upper())
# # mostrar o texto em letra minúscula
# print('Variável B com letra minúscula:', b.lower(), '\n')
#
# # mostrar o texto em letra maiúscula
# print('Variável C com letra maiúscula:', c.upper())
# # mostrar o texto em letra minúscula
# print('Variável C com letra minúscula:', c.lower(), '\n')
#
# # mostrar o texto em letra maiúscula
# print('Variável D com letra maiúscula:', d.upper())
# # mostrar o texto em letra minúscula
# print('Variável D com letra minúscula:', d.lower())
#
# # Remove espaços em branco antes e depois do texto
# print(a.strip())
#
# # Subtstitui um caractere por outro
# a2 = a.replace('e', 'x')
# print(a2)
#
# # Troca boa e bom por banana
# result = d.replace('boa', 'banana').replace('bom', 'banana') # Encadeamento de função
# print(result)
#

# Booleans
# a = True
# b = 1 == 1
# c = 10 > 0
# d = 'abacaxi' == 'maçã'
# print(d)
#
# # Estrutura de decisão usando variável booleana
# if d:
#     print('São iguais')
# else:
#     print('São diferentes')

# Listas
frutas = ["banana", "abacaxi", "maçã"]
print(frutas)
print('Tipo', type(frutas))
print('Comprimento', len(frutas), '\n')

# imprimindo primeira posição do vetor
print(frutas[0])
# imprimindo segunda posição do vetor
print(frutas[1])
# imprimindo terceira posição do vetor
print(frutas[2])
# imprimindo ultima posição do vetor
print(frutas[-1], '\n')

# Faixas de índices
# Ultimo numero da faixa de valores nao é inclusivo (e sim exclusivo)
print(frutas[0:3]) # [1, 2, 3]

# Omitindo o valor da faixa ele vai até o final
print(frutas[1:])

# Omitindo o valor da faixa ele utiliza desde o início
print(frutas[:2], '\n')

frase = 'Hoje é quinta-feira!'
print("Frase:", frase)

result = 'banana' in frase
print("Resultado:", result)

# aplicando o mesmo conceito com listas
is_in_frase = 'banana' in frutas
print("Resultado:", is_in_frase, '\n')

# alterando a posição de uma lista [vetor/array]
# frutas[0] = 'maçã'

# inserir um valor na lista na posição desejada da lista
frutas.insert(0, 'uva')
# adiciona no final da lista
frutas.append('amora')
print(frutas)

# procura o valor e remove da lista
frutas.remove('maçã')
print(frutas)
