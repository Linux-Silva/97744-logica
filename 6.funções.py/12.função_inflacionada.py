import os
os.system("clear")

def valor(n1):
    if n1 < 100:
        resultado = n1 * 1.10
        return resultado
    else:
        resultado = n1 * 1.20
        return resultado

print("ㅤㅤㅤㅤ====Compras====ㅤㅤㅤㅤ")
n1 = float(input("Digite o valor da compra realizada: "))

valor_com_aumento = valor(n1)

print("ㅤㅤㅤ====Nota Fiscal====ㅤㅤㅤ")
print(f"O valor final após o aumento é: R$ {valor_com_aumento:.2f}")