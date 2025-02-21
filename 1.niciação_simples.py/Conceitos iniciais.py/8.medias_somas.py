import os

os.system ("clear")

primeiro_numero =  float(input("digite o primeiro numero:"))
segundo_numero =  float(input("digite o segundo numero:"))

soma =    primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero 
média =  (primeiro_numero + segundo_numero) / 2


maior_numero = max(primeiro_numero, segundo_numero)
menor_numero = min(primeiro_numero, segundo_numero)

print()
print(f"soma: {soma}")
print(f"produto: {produto}")
print(f"média: {média}")

if primeiro_numero == segundo_numero:
    print(f"Os números são iguais")
else:
    print(f"maior número: {maior_numero}")
    print(f"menor número: {menor_numero}")W