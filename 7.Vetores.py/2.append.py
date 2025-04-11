import os
os.system("cls || clear")

lista_de_compras = []
QUANTIDADE = 3

print("=ㅤLISTA DE COMPRASㅤ=")
for i in range(QUANTIDADE):
    item = input ("Digite um item para lista: ")
    lista_de_compras.append(item)
    
print("\nㅤITENS DA LISTA DE COMPRAㅤ")
for item in lista_de_compras:
    print(item)