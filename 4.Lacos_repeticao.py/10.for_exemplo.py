import os
os.system("clear")

media = 0 
soma = 0

for i in range (4):
    numero = int(input(f"digite a {i+1}° nota :" ))
    soma += numero

media = soma /4

print()
print(f"media {media}")




