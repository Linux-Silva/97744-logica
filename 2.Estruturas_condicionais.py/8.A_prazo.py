import os
os.system("clear")

valor_produto = float(input("digite o valor do produto:  "))

print(""""
========================FORMA DE PAGAMENTO===========================
1   \tÁ vista
2   \tÁ prazo
""") 

forma_de_pagamento = int(input("digite a forma de pagamento: "))


match forma_de_pagamento:
    case 1:
        desconto = 100 * 0.10
        valor = (valor_produto - desconto)
        print (f"Resultado: {valor}")
        
        
    case 2:
        parcelas = int(input("digite a quantidade de parcelas: "))
        valor = (valor_produto / parcelas)
        print(f"valor do produto: R$ {valor_produto}")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor pro parcela: R$ {valor:.2f}")
        print(f"Forma de pagamento: Á prazo")
        


    case _:
        print("opção invalida")

print(f"desconto {desconto}")
print(f"parcelas {parcela}")
print(f"valor {valor}")