import os
os.system("clear") 

def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = [0] * 6  

for i in range(6):
    numeros[i] = int(input(f"Digite o primeiro número: "))

pares, impares = contar_pares_impares(numeros)
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")