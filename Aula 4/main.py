# # Aula 4
# # comida = ['arroz', 'feijão', 'macarrão', 'frango']
# #
# # print('Lista completa:', comida)
# #
# # # Remove um item
# # comida.remove('macarrão')
# # print('Removendo valor: ', comida)
# #
# # # Remove o último elemento
# # comida.pop()
# # print('Remove último elemento:', comida)
# #
# # # Remove o índice indicado
# # comida.pop(0)
# # print('Remove o índice indicado:', comida)
# #
# # # Deleta item da lista
# # del comida[0]
# # print('Deleta item da lista', comida)
# #
# # numbers = [1, 2, 3, 4]
# # print('Lista de números:', numbers)
# # # Limpa lista
# # numbers.clear()
# # print('Lista de números vazia:', numbers)
#
# # Ordenação de listas
#
# comida2 = ['arroz', 'feijão', 'macarrão', 'frango']
# numbers2 = [1, 3, 4, 6, 7, 8, 12, 1]
# print(comida2)
# print(numbers2, '\n')
#
# # Ordena a lista em ordem alfabética ou crescente
# comida2.sort()
# print('Lista ordenada em ordem alfabética:', comida2)
#
# numbers2.sort()
# print('Lista ordenada em ordem crescente', numbers2)
#
# numbers2.sort(reverse=True)
# print('Lista ordenada em ordem decrescente:', numbers2)
#
# numbers2.reverse()
# print('Lista do último para o primeiro:', numbers2)

# Copiando listas
# cores = ['amarelo', 'verde', 'azul', 'vermelho', 'rosa']
#
# # cores2 = cores  # A mesma posição de memória de cores agora está armazenada em cores2
# # cores2[0] = 'roxo'
# # print(cores)
# # print(cores2)
#
# # Cria cópia da lista atual e armazena o ponteiro em cores2
# # cores2 = cores.copy()
# cores2 = list(cores)
# cores2[0] = 'roxo'
#
# print('Lista original:', cores)
# print('Lista copiada e modificada:', cores2)

# Junção listas
# cores = ['amarelo', 'verde', 'azul', 'vermelho', 'rosa']
# cores2 = ['preto', 'branco']
#
# # Concatena listas
# # juntar_listas = cores + cores2
# # print(cores2)
# # print(cores)
# # # print(juntar_listas)
#
# # Concatena cores com o conteúdo de cores2
# cores.extend(cores2)
# print(cores)

# Laços de repetição
# number = 0

# Repetição While (Enquanto number se mantiver menor ou igual 10)
# while number <= 10:
#     if number < 10:
#         print(number, end=', ')
#     else:
#         print(number)
#     number += 1

# laço mostrando os valores menores que 5
# number = 0
# LIMIT = 10

# laço de repetição while
# while number <= LIMIT:
#     number += 1
#     if number == 5:
#         print('Cinco')
#         break
#     print(number)

# laço mostrando os valores menores que 5
# while number <= LIMIT:
#     number += 1
#     if number >= 5:
#         continue
#     print(number)

# laço FOR
# mostra valores de 0 a 9
# for i in range(10):
#     if i < 9:
#         print(i, end=', ')
#     else:
#         print(i)

# # definindo o valor de início do intervalo
# for j in range(5, 10):
#     print(j)
#
# o ultimo parametro define o incremento do range
# for x in range(6, 20, 2):
#     print(x, end=', ')
