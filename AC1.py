"""
Exercício 1:

"""
a = float(input("informe o parâmetro a da equação: "))
b = float(input("informe o parâmetro b da equação: "))
c = float(input("informe o parâmetro c da equação: "))
delta = (b ** 2) - 4 * a * c
primeira_raiz = (-b + delta ** (1/2)) / (2 * a)
segunda_raiz = (-b - delta ** (1/2)) / (2 * a)
print("a primeira raiz da equação é: ",primeira_raiz)
print("a segunda raiz da equação é: ",segunda_raiz)

"""
Exercício 2:

"""
ano = int(input("Informe o ano: "))
print(ano % 4 == 0 and ano % 100 !=0 or ano % 100 ==0 and ano % 400 == 0)