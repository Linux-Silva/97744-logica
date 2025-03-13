import os

os.system("clear")



a=int(input("Digite o primeiro numero: "))
operacao = input("Digite a operação desejada: ")
b =int(input("Digite o segundo numero: "))

import os
os.system("clear")

match operacao:
    case "+": 
        resultado = a + b  
    case "-": 
        resultado = a - b 
    case "/":
        resultado = a / b 
    case "*": 
        resultado = a * b 
    case _:
        print("Opção inválida. ")        

print()
print(f"Primeiro numero: {a}")
print(f"Operação: {operacao}")
print(f"Segundo numero:  numero: {b }")
print(f"Primeiro numero: {a}")
print(f"Resultado: {resultado}")