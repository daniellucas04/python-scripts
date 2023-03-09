# Aula 2
# exemplo de uso de estrutura de decisão
# a = 2
# if a <= 1:
#     print('OK')
# else:
#     print('Não satisfeita a condição!')

# novo exemplo
# solicitando entradas do usuário
# a = input("Digite o primeiro valor:")
# b = input("Digite o segundo valor:")
# resultado = float(a)+float(b)
# print(resultado)

# exemplo calculadora
# op = input("Escolha a operação (1-soma,2-subtração,3-multiplicação): ")
# op = int(float(op))
# # if op >= 1 and op <= 3:
# if 1 <= op <= 3:
#     a = input("Digite o primeiro valor:")
#     b = input("Digite o segundo valor:")
#     if op == 1:
#         resultado = float(a)+float(b)
#     elif op == 2:
#         resultado = float(a)-float(b)
#     elif op == 3:
#         resultado = float(a)*float(b)
#     print(resultado)
# else:
#     print('Operação inválida')


texto = "banana abacaxi melão mamão abacate melancia maçã"
print(texto)
# mostra o comprimento de uma string
print(len(texto))
# verificar se o nome da fruta contém determina letra
r = 'melancia' in texto
print(r)
# verificando quantas vezes a palavra aparece no texto
r = texto.count('melancia')
print(r)


