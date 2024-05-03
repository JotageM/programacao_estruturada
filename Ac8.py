"""
Exercício 1028:

"""
from math import gcd


n = int(input())
for i in range (n):
    f1, f2 = map(int,input().split())
    print(gcd(f1,f2))


"""
Exercício 1087:

"""

x1,y1,x2,y2= map(int,input().split())
while x1 != 0 or x2 != 0 or y1 != 0 or y2 != 0:
    mov = 0
    if x1 == x2 and y1 == y2:
        print(mov)
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        print(mov +1)
    else:
        print(mov+2)
    x1,y1,x2,y2= map(int,input().split())


"""
Exercício 1161:

"""

while True:
    try:
        m,n = map(int,input().split())
        fatorial_n = 1
        for i in range(1,n+1):
            fatorial_n *= i
        fatorial_m=1
        for i in range(1,m+1):
            fatorial_m *= i
        print(fatorial_m + fatorial_n)
    except EOFError:
        break


"""
Exercício 1170:

"""

n = int(input())
for i in range(n):
    x = float(input())
    dias = 0
    while x > 1:
        x/=2
        dias += 1
    print(f"{dias} dias")


"""
Exercício 1171:

"""

n = int(input())
lista = {}
for i in range(n):
	x = int(input())
	if(x in lista):
		lista[x] += 1
	else:
		lista[x] = 1


chaves = lista.keys()
chaves = sorted(chaves)

for k in chaves:
	print("%d aparece %d vez(es)" %(k,lista[k]))



"""
Exercício 1221:

"""

from math import sqrt
def is_prime(num):
  for i in range(2, int(sqrt(num))+1):
      if num % i == 0:
          return False
  return True

n = int(input())
for i in range(n):
    num = int(input())

    is_num_prime = is_prime(num)

    if (is_num_prime):
        print("Prime")
    else:
        print("Not Prime")



"""
Exercício 1329:

"""

n = int(input())
while n > 0:
    x =[int(i) for i in input().split()]
    mary = 0
    john = 0
    for i in range(len(x)):
        if x[i] == 0:
            mary += 1
        else:
            john += 1
    print(f"Mary won {mary} times and John won {john} times")
    n = int(input())



"""
Exercício 1555:

"""


def func_Rafael(x,y):
    return ((3*x)**2 + (y**2))


def func_Beto(x,y):
    return (2 *(x**2) + (5*y) ** 2)


def func_Carlos(x,y):
    return ((-100*x) + (y **3))





n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    if  func_Beto(x,y) < func_Rafael(x,y) > func_Carlos(x,y):
        print("Rafael ganhou")
    elif func_Rafael(x,y) < func_Beto(x,y) > func_Carlos(x,y):
        print("Beto ganhou")
    else:
        print("Carlos ganhou")