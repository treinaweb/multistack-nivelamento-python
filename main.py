# # Variáveis
# nome_da_variavel = "Treinaweb"
# print(type(nome_da_variavel))
# nome_da_variavel = 5
# print(type(nome_da_variavel))
# variavel_float = 5.5
# variavel_boolean = True
#
# # Constantes
# NOME_DA_CONSTANTE = 10
# print(NOME_DA_CONSTANTE)
# NOME_DA_CONSTANTE = "Treinaweb"
# print(NOME_DA_CONSTANTE)
#
# # Operadores matemáticos
# print(nome_da_variavel + variavel_boolean)
# print(5 - 5)
# print(5 * 5)
# print(5 / 5)
#
# # Operadores de comparação
# print(10 > 5)
# print(10 >= 11)
# print(10 < 5)
# print(10 <= 10)
# print(10 == 10)
# print(10 != 11)
#
# # Operadores lógicos
# print(not(10 > 10))
#
# print((10 == 10) or (10 > 20) or (1 != 1) or (20 < 10))
#
# print((10 != 10) and (10 > 5) and (10 > 0) and (5 < 10))

# Estruturas de condição
# idade = 70
# if idade < 18:
#     print("Você é criança")
# elif idade >= 18 and idade <= 60:
#     print("Você é adulto")
# else:
#     print("Você está na melhor idade")

# # Estruturas de repetição
# for i in range(0, 11):
#     print(i)
# else:
#     print("A lista foi percorrida com sucesso")
#
# teste = 0
# while teste <= 10:
#     print("código sendo executado")
#     teste += 1
# else:
#     print("O while finalizou")

def calcular_idade(idade):
    if idade < 18:
        return "Você é criança"
    elif idade >= 18 and idade <= 60:
        return "Você é adulto"
    else:
        return "Você está na melhor idade"


resposta = calcular_idade(11)
print(resposta)
print(calcular_idade(25))
print(calcular_idade(idade=80))

