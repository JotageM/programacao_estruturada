"""

Exercício   1048:


"""

salary = float(input())
if salary <= 400.00:
    increasy_salary = 1.15
    new_salary = salary * increasy_salary
    percentual = "15 %"
elif  400.00 < salary <= 800.00:
    increasy_salary = 1.12
    new_salary = salary * increasy_salary
    percentual = "12 %"
elif 800.00 < salary <= 1200.00:
    increasy_salary = 1.10
    percentual = "10 %"
    new_salary = salary * increasy_salary
elif  1200.00 < salary <= 2000.00:
    increasy_salary =1.07
    new_salary = salary * increasy_salary
    percentual = "7 %"
elif salary > 2000.00:
    increasy_salary = 1.04
    new_salary = salary * increasy_salary
    percentual = "4 %"
print(f"Novo salario: {new_salary:.2f}")
print(f"Reajuste ganho: {(new_salary - salary):.2f}")
print(f"Em percentual: {percentual}")


"""

Exercício 1065:

"""

pares = 0
for i in range(5):
    num = float(input())
    if num % 2 == 0:
        pares += 1
print(f"{pares} valores pares")


"""

Exercício 1132:

"""

num1 = int(input())
num2 = int(input())
soma = 0
if num2 > num1:
    for i in range(num1,num2 +1):
        if i % 13 != 0:
            soma += i
else:
    for i in range(num2,num1 +1):
        if i % 13 != 0:
            soma += i
print(soma)

"""

Exercício 1180:

"""

num = int(input())
x = [int(i) for i in input().split()]
print(f"Menor valor: {min(x)}")
print(f"Posicao: {x.index(min(x))}")

"""

Exercício 1182:

"""

c = int(input())
t = input()
lista=[]
for i in range(12):
    lista.append([])
for i in range(12):
    for j in range(12):
        num = float(input())
        lista[i].append(num)
if t == "S":
    soma = 0

    for k in range(12):
        soma+=lista[k][c]
    print(f"{soma:.1f}")
if t == "M":
    media = 0
    soma = 0

    for k in range(12):
        soma +=lista[k][c]
    media = soma/12
    print(f"{media:.1f}")

"""

Exercício 1244:

"""

n = int(input())
while n > 0:
    n -= 1
    c = input().split()
    c.sort(key=len, reverse=True)
    for i in range(len(c)):
        print(c[i], end = '')
        if i != len(c)-1:
            print(' ', end = '')
    print()