import os
os.system("cls || clear")

numeros = []

print("Lista numerica <>")
for i in range(5):
    num = int(input("Digite um numero: "))
    numeros.append(num)
    
maior = max(numeros)
menor = min(numeros)
    
print("\nOs números informados:", numeros)
print("O menor número é:", menor)
print("O maior número é:", maior)
