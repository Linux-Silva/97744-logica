import os
os.system("clear")



media = 0 
soma = 0

for i in range (4):
    numero = int(input(f"digite a {i+1}° nota :" ))
    media += numero / 4

print(f"A média do aluno é: {media:.2f}")

if media >= 7:
    print("Parabéns! Você está aprovado!")

elif media <= 4:
     print("Você foi reprovado.")
else:
    print("Você esta em recuperação.")

print(f"media {media}")