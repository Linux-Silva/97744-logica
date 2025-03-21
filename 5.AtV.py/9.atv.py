import os
import time
os.system("clear")

soma = 0
contador = 0

while True:
    numero = int(input("Digite um valor inteiro positivo (ou um número negativo para finalizar): "))
    
    if numero < 0:
        break
    
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média aritmética dos valores inseridos é: {media:.2f}")
else:
    print("Nenhum valor positivo foi inserido.")