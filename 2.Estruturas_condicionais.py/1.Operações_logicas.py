import os

os.system("clear")

primeiro_numero: int(input("digite o primeiro numero: "))
segundo_numero: int(input("digite o segundo numero:  "))

if primeiro_numero > segundo_numero:
     maior = primeiro_numero
     menor = segundo_numero
else:
     maior = primeiro_numero
     menor = segundo_numero

print()
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")