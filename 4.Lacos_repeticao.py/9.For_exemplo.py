import os
os.system("clear")

pares = 0
impares = 0

for i in range(5):
    valor = int(input("Digite um numero: "))
    if numero % 2 == 0:
       pares += 1
    else:
        impares += 1

print()
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
