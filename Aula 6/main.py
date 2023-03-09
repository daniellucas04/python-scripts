# Aula 6


# # Jogo da soma
# points = 0
# try:
#     # Busca placar salvo
#     save_points_file = open('jogo.txt', 'r')
#     points = int(save_points_file.read())
#     save_points_file.close()
# except FileNotFoundError:
#     pass
#
#
# def save_points():
#     file = open('jogo.txt', 'w')
#     file.write(str(points))
#     file.close()
#
# while True:
#     print("Digite 'sair' para finalizar\n")
#     # sorteando um número entre 0 e 10
#     number1 = random.randint(0, 10)
#     number2 = random.randint(0, 10)
#     # Imprime a pergunta e recebe a resposta do usuário
#     print("Qual o resultado da soma de {} + {}?".format(number1, number2))
#     response = str(input("Resposta: "))
#
#     # Faz a verificação se a soma está correta
#     if response == 'sair':
#         exit()
#     elif response == str((number1 + number2)):
#         points += 1
#         save_points()
#         print("Correto! Você tem {} pontos\n".format(points))
#     else:
#         print("Errou!\n")

# Funções

# Criando uma função sem parâmetro
# def say(word1: str = 'bla'):
#     print(word1)


# # chamando a funcão
# say()
#
# for i in range(5):
#     say()

# Criando uma função com 1 parâmetro
# def falar_mais_um(times: int = 1):
#     for i in range(times):
#         say()


# Criando uma função com 2 parâmetros
# def falar_mais_dois(times: int = 1, word2: str = 'bla'):
#     for i in range(times):
#         say(word2)


# falar_mais_um(times=3)
# falar_mais_dois(times=2, word2='blablabla')

# # Funções de operações matemáticas
def sum_numbers(a: float, b: float):
    return a + b


def subtract_numbers(a: float, b: float):
    return a - b


def multiply_numbers(a: float, b: float):
    return a * b


def divide_numbers(a: float, b: float):
    return a / b


# Chamando as funções e imprimindo os resultados
# print("Soma dos números:", sum_numbers(1.6, 2.5))
# print("Subtração dos números:", subtract_numbers(1, 2))
# print("Multiplicação dos números:", multiply_numbers(1.6, 2.5))
# print("Divisão dos números:", divide_numbers(1.6, 2.5))

# Chamando a função e utilizando o retorno como argumento da função python 'format'
print('A soma de 5 com 6 é igual a: {}'.format(sum_numbers(5, 6)))
