"""

docstrings

Comentário de várias linhas

progração estruturada
26/02/20204

Introdução à Python
- Comentários
- Exibição de dados na tela
- Tipos de dados
- Leitura de dados
- Variáveis


"""


print("olá,mundo")
print("olá","mundo" )
print("ana tem",18,"anos")
print("ana tem", 18 , "anos", sep="--")

""""
Tipos de dados em Python

-4 tipos de dados primitivos:
    - Números inteiros (int)
    - Números decimais (float)
    - Booleanos (bool)
    - Texto(string)

"""
#string
print("""representação
de um texto de multiplas linhas""")


# Essas 4 linhas representam coisas diferentes

print(2)
print(2.0)
print("2")
print("2.0")


#escape char- \
print("olá, \"mundo\"")
print("texto \nde duas linhas")
print("texto\\novo")
print("texto\t novo")

#None
print(print("olá, mundo"))


# O resultado do input é SEMPRE uma string
# print(input("informe o seu nome: "))
# print(type(input("informe a sua idade: ")))

# nome = input("informe o seu nome: ")
# print("Olá,", nome)

# Python é uma linguagem de tipagem fraca e dinâmica
nome = 48
print(nome)

#type hint
idade : int=16
print(idade)

# Python não possui o conceito de constante
PI = 3,1415
TAM_MAX = 15
#quando voce quer "estabelecer" uma constante voce coloca a variavel em caixa alta

#todo dado diferente de 0, 0.0,"",etc são considerados como true
print(bool(""))
print(bool("olá, mundo"))
print(bool(0))
print(bool (36.95))

