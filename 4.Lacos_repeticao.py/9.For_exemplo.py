import os
os.system("clear")

pares = 0
impares = 0

numero = int(input("Digite um numero: "))

for i in range(200):
    valor = int(input("Digite um numero: "))
    if numero % 2 == 0:
       pares += 1
    else:
        impares += 1

print()
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Numero {numero}")