import os
os.system("cls || clear")

numeros = []
pares = 0
impares = 0

print("===Lista numérica <>===")
for i in range(6):
    num = int(input("Digite um número: "))
    numeros.append(num)


for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("\nOs números informados:", numeros)

for num in numeros:
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
print()
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")