import math
from math import trunc

'''n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
plus = n1 + n2
print(plus)
'''
'''
#exercicio 2
height = float(input("Enter the height: ")
largure = float(input("Enter the largure: "))
area = largure * height
print(area)
'''
#
# #exercicio 3
# idade = int(input("digite sua idade: "))
# dias = idade * 365
# print(dias)

# n1 = int(input("digite um numero"))
# n2 = int(input("digite outro numero"))
# inteira = trunc(n1/n2)
# print(" a divisao inteira dara {} e o resto de divisao dara {}".format(inteira, resto))
# resto = n1 % n2

# preco = float(input("digite o preço da conta"))
# gorjeta = preco / 10
# print ("o valor da gorjeta sera {} e o valor total sera {}".format(gorjeta, preco+gorjeta))

# n1 = int(input("digite um numero: "))
# raiz = math.sqrt(n1)
# quadrado = math.pow(n1, 2)
# print("a raiz quadrada desse numero é {} e esse numero ao quadrado é {}".format(raiz,quadrado))

# first_name = input("digite seu primeiro nome: ")
# last_name = input("digite seu sobrenome: ")
# nome_completo = f"{first_name} {last_name}"
# print(nome_completo)


# salario = float(input("digite seu salario: "))
# aumento = salario * 1.15
# print(aumento)


distancia = float(input("digite a distancia que sera percorrida em km: "))
velocidade = float(input("digite a velocidade em km/h: "))
horas = distancia / velocidade
minutos = horas * 60
print("o tempo que voce demorara para percorrer essa distancia é de {} horas ou {} minutos".format(horas, minutos))
