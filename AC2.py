"""
exercício 1:

"""


def eq_seg_grau(a,b,c):
    """Mostra as raizes de uma equação de segundo grau, dado os parametros a, b e c."""
    delta = (b ** 2) - 4 * a * c
    primeira_raiz = (-b + delta ** (1/2)) / (2 * a)
    segunda_raiz = (-b - delta ** (1/2)) / (2 * a)  

    print("a primeira raiz é: ", primeira_raiz)
    print("a segunda raiz é: ", segunda_raiz)




a = float(input("informe o parâmetro a da equação: "))
b = float(input("informe o parâmetro b da equação: "))
c = float(input("informe o parâmetro c da equação: "))
eq_seg_grau(a,b,c)

"""
-------------------------------------------------------------------------------------------------

"""

def bissexto(ano):
    """calcula se o ano é bissexto ou não"""
    print(ano % 4 == 0 and ano % 100 !=0 or ano % 100 ==0 and ano % 400 == 0)

ano = int(input("Informe o ano: "))
bissexto(ano)


"""
Exercício 2:

"""

 
def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    """ calcula o salário liquido mensal"""
    salario = valor_hora * num_horas
    imposto = float(irpf) * salario
    salario_liquido = salario - imposto
    print("o salário líquido mensal foi: ", salario_liquido)



num_horas = int(input("quantas horas trabalhadas no mes: "))
valor_hora = float(input("qual o valor do salário por hora: "))
calcula_salario(valor_hora, num_horas, irpf=0.275)
    
    




