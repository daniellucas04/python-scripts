# cidades = ("Barretos", "São José do Rio Preto", "Viana", "São Carlos")
#
# print(cidades[0])
# print(cidades[1])
# print(cidades[2])
# print(cidades[3])
# print("Quantidade de cidades visitadas:", len(cidades))

# Tupla de inteiros
# notas = (3, 9, 6, 2)
# print(notas)

# Tupla de um elemento
# cidade = ("Barretos",)
# print(type(cidade))

# Usando sum
# precos1 = (9.99, 6.9, 8.01, 9.99, 10.30)
#
# media1 = sum(precos1) / len(precos1)
# print("Média com sum:", media1)
#
# # Usando indices
# precos2 = (9.99, 6.9, 8.01, 9.99, 10.30)
# media2 = (precos2[0] + precos2[1] + precos2[2] + precos2[3] + precos2[4]) / len(precos2)
# print("Média com indices:", media2)
#
# precos3 = (9.99, 6.9, 8.01, 9.99, 10.30)

# alunos = ("Leonardo", 10, "Raphael", 9, "Michelangelo", 5)
# print(alunos[2:4])

# notas_aluno = (9, 3, 4.5, 5.3, 2, 10.0, 6)
#
# if 10 in notas_aluno:
#     print("Parabéns pela nota dez!")
# else:
#     print("Não tirou nota dez.")

# frutas = ("abacaxi", "goiabada", "maçã")
# print(type(frutas))
# print(frutas)
#
# nova = list(frutas)
# print(type(nova))
#
# nova[1] = "goiaba"
# print(nova)
# nova.append("melancia")
#
# frutas = tuple(nova)
# print(frutas)

# frutas = ("abacaxi", "goiabada", "maçã")
# print(frutas)
# frutas += ("melancia",)
# print(frutas)

# frutas = ("abacaxi", "goiabada", "maçã")
# nova = list(frutas)
# nova.remove("abacaxi")
# frutas = tuple(nova)
# print(frutas)

# frutas = ("abacaxi", "goiabada", "maçã")
# # Recebe valores na sequência
# (primeira, segunda, terceira) = frutas;
# print(frutas)

# frutas = ("abacaxi", "goiabada", "maçã")
# (primeira, *resto) = frutas
# print(resto)
# # print(type(resto))
# frutas = ("abacaxi", "goiaba", "maçã")
#
# for fruta in frutas:
#     print(fruta)
#
# cidades = ("Barretos", "São José do Rio Preto", "Viana", "São Carlos")
#
# for id, cidade in enumerate(cidades):
#     id += 1
#     print("Cidade", id, ":", cidade)
#
# alunos = ("Leonardo", "Raphael", "Michelangelo")
# notas = (10, 9, 5)
# sala = alunos + notas
# # Multiplica as tuplas
# print(sala * 2)
#
