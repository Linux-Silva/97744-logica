import os
os.system("clear")

print("====Negativos e Positivos====")

def parouimpar(num):
        if num > 0:
          print("Postivo. ")
        elif num == 0:
            print("Neutro")
        else:
            print("Negativo. ")

num = int(input("Digite um numero: "))
parouimpar(num)