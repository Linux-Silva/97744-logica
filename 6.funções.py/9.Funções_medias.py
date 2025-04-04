import os
os.system("cls || clear")

def media(n1, n2):
    calcular = (n1 + n2) / 2
    return calcular


print("=====Media Pedida=====")
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

Mediana = media(n1, n2)

print(f"mediana: {Mediana}")