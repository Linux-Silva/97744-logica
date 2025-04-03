import os
os.system("clear")

print("==== Calculadora de Pares e Ímpares ====")

def par_ou_impar(num):
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num1 + num2
print(f"A soma de {num1} + {num2} = {soma}")

par_ou_impar(soma)