import os
os.system("cls || clear")

soma = 0
notas = []
contador = 0
for i in range(3):
    nota = float(input("Digite uma nota: "))
    soma += nota
    notas.append(nota)
    contador += 1

def calcular(soma):
    return soma / contador


soma = sum(notas)

media = calcular(soma)
if media >= 7:
    resultado = "vc esta Aprovado!"
else:
    resultado = "vc esta Reprovado!"

print()
for nota in notas:
    print(f"Notas: {nota}")

print(f"Sua media foi de {media:.1f}!")
print(f"{resultado}")