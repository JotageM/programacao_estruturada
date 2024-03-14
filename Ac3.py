""" Ac3 PROGAMAÇÃO ESTRUTURADA  """


""" Exercício 1: 
"""

def determina_tipo_triangulo(a,b,c):
    """ 
    recebe três lados de um triângulo e retorna uma string, "Escaleno", "Isósceles" ou "Equilátero", 
    conforme o tipo do triângulo. retorna "Não é um triângulo" se os três lados não formarem um triângulo.
    """
    
    if (a + b < c) or (a + c < b) or (b + c < a):
        print("Não é um triangulo")
    elif (a == b) and (a == c) :
        print("Equilátero")
    elif (a==b) or (a==c) or (b==c):
        print("Isósceles")
    else:
        print("Escaleno")





""" Exercício 2: 
"""

def dia_semana(num):
    """ 
    recebe um número inteiro e retorna uma string indicando o dia da semana equivalente, 
    considerando que o dia da semana igual a 1 é o domingo, 2 é segunda-feira, etc. 
    A função retorna uma string vazia caso o número seja inválido. 
    
    """

    if num == 1:
        print("Domingo")
    elif num == 2:
        print("Segunda-feira")    
    elif num == 3:
        print("Terça-feira")    
    elif num == 4:
        print("Quarta-feira")    
    elif num == 5:
        print("Quinta-feira")    
    elif num == 6:
        print("Sexta-feira")    
    elif num == 7:
        print("Sábado")
    else:
        print("")
        




""" 
Exercício 3:
 
"""       


def soma(num1,num2):
    """ Soma dois números """
    return(num1 + num2)



def subtracao(num1,num2):
    """ Subtrai dois números """
    return(num1 - num2)


def multiplicacao(num1,num2):
    """ Multiplica dois números """
    return(num1 * num2)


def divisao(num1,num2):
    """ Divide dois números """
    return(num1 / num2)



def main():
    """ Le 2 numeros e uma operação, e mostra na tela o resultado. """
    num1 = float(input("Informe um número: "))
    num2 = float(input("Infome outro número: "))
    operacao = input("Informe a operação: ")
    if operacao == "soma":
        print("resultado: ", soma(num1,num2))
    elif operacao == "subtração":
        print("resultado: ", subtracao(num1,num2))
    elif operacao == "multiplicação":
        print("resultado: ", multiplicacao(num1,num2))
    elif operacao == "divisão":
        print("resultado: ", divisao(num1,num2))
    else:
        print("operação inválida")   

       





























