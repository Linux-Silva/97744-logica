import os
import time
os.system("clear")
soma = 0 
contador = 0
while True:
        
        nota = float(input(f"Digite uma nota: "))
        soma += nota
        contador += 1

        desejo = input("Deseja adicionar mais uma nota ? ")
        if desejo == "n":
            
         break

media = soma / contador

print()
print(f"Media: {media}")
print()
if media >= 7:
    print("APROVADO: ")
elif media >= 5 and media < 7: 
    print("Recuperaçao")
else:
    print("Reprovado")
print()