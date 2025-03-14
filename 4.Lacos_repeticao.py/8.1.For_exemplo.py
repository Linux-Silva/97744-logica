import os
os.system("clear")

soma = 0

for i in range(5):
    numero = int(input(f"Digite os {i+1}º números inteiros : "))
    soma += numero

print()
print(f"A soma dos números inteiros é : {soma}")
