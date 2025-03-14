import os
os.system("clear")

numero = int(input("Digite a operação desejada : "))

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")