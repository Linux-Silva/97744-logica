import os
os.system("cls || clear")

def somar(n1,n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular


def divisao(n1, n2):
    calcular = n1 / n2
    return calcular


def multiplicacao(n1, n2):
    calcular = n1 * n2
    return calcular

print("=====Numeros Pedidos=====")
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))

soma = somar(n1, n2)
subtracao = subtrair(n1, n2)
divisao = divisao(n1, n2)
multiplicacao = multiplicacao(n1, n2)


print("=====Resultado Final======")
print(f"Soma: {soma}")
print(f"subtração: {subtracao}")
print(f"divisao: {divisao}")
print(f"multiplição: {multiplicacao}")
print("===========================")