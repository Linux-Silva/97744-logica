import os
os.system("clear")

cor = input("Digite a cor do CD: ").lower()

if cor == "Verde":
    preco = 20.00
elif cor == "Azul":
    preco = 25.00
elif cor == "Amarelo":
    preco = 30.00
elif cor == "Vermelho":
    preco = 35.00
else:
    preco = "Cor inválida"

print(f"O preço do CD é: {preco}")
