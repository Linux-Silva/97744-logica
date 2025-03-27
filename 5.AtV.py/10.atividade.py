import os

os.system("cls || clear")

pares = impares = soma_pares = soma_total = 0

while True:
    num = int(input("Digite um número inteiro positivo: "))
    
    if num == 0:
        break

    soma_total += num
    
    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1

total_numeros = pares + impares
media_pares = soma_pares / pares if pares > 0 else 0
media_geral = soma_total / total_numeros if total_numeros > 0 else 0

print()
print(f"Quantidade de pares: {pares}, ímpares: {impares}")
print(f"Média dos pares: {media_pares:.2f}")
print(f"Média geral: {media_geral:.2f}")
