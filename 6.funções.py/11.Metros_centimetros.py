import os
os.system("clear")

def metros(n1):
    calcular = (n1 ) *100
    return calcular


print("===+==Metragem Pedida==+===")
n1 = int(input("ㅤDigite a metragem: "))

n1 = metros(n1)


print("=====Resultado Final======")
print(f"ㅤ{n1} Centimetros:")
print("==========================")
