import os
from dataclasses import dataclass
os.system("clear || cls")

@dataclass
class Carros:
    marca: str
    modelo: str
    categoria: str
    preco: float

lista_carros = []

for i in range(2):
    print(f"Informe os dados do {i+1}º carro:")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    
    carro = Carros(marca=marca, modelo=modelo, categoria=categoria, preco=preco)
    lista_carros.append(carro)
    print()

nome_arquivo = "carros.txt"

with open(nome_arquivo, "w") as arquivo:
    for carro in lista_carros:
        arquivo.write(f"Marca: {carro.marca}\n")
        arquivo.write(f"Modelo: {carro.modelo}\n")
        arquivo.write(f"Categoria: {carro.categoria}\n")
        arquivo.write(f"Preço: R$ {carro.preco:.2f}\n")
        arquivo.write("\n")

print("\nDados dos carros salvos com sucesso em 'carros.txt'!")
