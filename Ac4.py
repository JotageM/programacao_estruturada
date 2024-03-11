
def ler_nome():
    """Retorna o nome do aluno"""
    return(input("informe seu nome: "))


def ler_notas():
    """ Lê as quatro notas das avaliações e retorna os valores. """
    ap1 = float(input("informe sua nota da ap1: "))
    ap2 = float(input("informe sua nota da ap2: "))
    asub = float(input("informe sua nota da asub: "))
    ac = float(input("informe sua nota da ac: "))
    return(ap1, ap2, asub, ac)


def notas_sao_validas(ap1, ap2, asub, ac):
    """
    Retorna true se as quatros notas estão entre 0 e 10,inclusive.
    Retorna false caso contrário
    """
    return( ap1 >=0 and ap1 <=10) and ( ap2 >=0 and ap2 <=10) and ( asub >=0 and asub <=10) and ( ac >=0 and ac <=10)


def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as avaliações apresentadas.
    Substitui a AP1 pela AS caso AS > Ap1
    Substitui a AP2 pela As caso AS > AP2
    A AS só substitui uma das duas provas (a menor delas)
    Caso as AS seja menor que a AP1 e a AP2, retorna AP1 E AP2

    """
    if ap1 < ap2 and asub > ap1:
        return(asub, ap2)
    if ap2 < ap1 and asub > ap2:
        return(asub, ap1)
    else:
        return(ap1, ap2)





def calcular_media(prova1, prova2, ac):
    """
    Retorna a média das avaliações, arredondando para duas casas decimais
    M = (NOTA1 + NOTA2) *0,4 AC * 0.2

    """
    return((prova1 + prova2) * 0.4 + ac * 0.2)


def aluno_foi_aprovado(media):
    """ Retorna true se o aluno tiver média superior a nota mínima
     caso contrário retorne false

    """
    return media >=7


def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            prova1, prova2, = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(prova1, prova2, ac)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado!")
            else:
                print("Aluno foi reprovado!")

main()