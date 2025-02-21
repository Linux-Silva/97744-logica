import os

os.system("clear")


quantidade_maca = int(input("digite quantas maçãs deseja comprar:"))

if quantidade_maca < 12:
    preco_maca = 1.30
else:
    preco_maca = 1.00

valor_total = quantidade_maca * preco_maca

print()
print(f"Valor total da compra R$ {valor_total: .2f}")

print("---------------------------------------------------");