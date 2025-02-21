import os

os.system("clear")

primeiro_numero = int(input("digite o primeiro número:"))
operacao = input("digite a operação desejada :")
segundo_numero = int(input("digite o segundo número:"))

match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case"-":
        resultado = primeiro_numero - segundo_numero
    case"*":
        resultado = primeiro_numero * segundo_numero
    case"/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print:("Opção inválida.")


print(f"Primeiro número: {primeiro_numero}")
print(f"operação: {operacao}")
print(f"Segundo numero: {segundo_numero}")
print(f"resultado {resultado}")


          