import os
os.system("clear")

renda_mensal = float(input("digite o valor da sua renda: "))
valor_emprestimo = float(input("digite o valor do emprestimo: "))
num_prestacoes = int(input("digite o numero de prestações desejadas: "))

valor_prestacao = valor_emprestimo / num_prestacoes

if valor_emprestimo <= 10* renda_mensal and valor_prestacao:
    print("Emprestimo autorizado!")
else:
    print("Emprestimo não autorizado")


