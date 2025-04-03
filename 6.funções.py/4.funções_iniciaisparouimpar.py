import os
os.system("clear")


print("====Calculadora de Pares e Impares====")

def parouimpar(num):
        if num % 2 == 1:
          print("Este numero e impar. ")
        else:
            print("Este numero e par. ")

num = int(input("Digite um numero: "))
num = int(input("Digite outro numero: "))
parouimpar(num)