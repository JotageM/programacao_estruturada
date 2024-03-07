"""
exercício 1:

"""


def eq_seg_grau(a,b,c):
    """Mostra as raizes de uma equação de segundo grau, dado os parametros a, b e c."""
    delta = (b ** 2) - 4 * a * c
    primeira_raiz = (-b + delta ** (1/2)) / (2 * a)
    segunda_raiz = (-b - delta ** (1/2)) / (2 * a)
    return(primeira_raiz, segunda_raiz)



"""
-------------------------------------------------------------------------------------------------

"""

def bissexto(ano):
    """calcula se o ano é bissexto ou não"""
    return(ano % 4 == 0 and ano % 100 !=0 or ano % 100 ==0 and ano % 400 == 0)




"""
Exercício 2:

"""

 
def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    """ calcula o salário liquido mensal"""
    return(valor_hora * num_horas - (valor_hora * num_horas * irpf))
   
    
    