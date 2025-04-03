import os
os.system("cls | clear")

while True:
    print(""""
    ===============MENU============
    1\tPicanha             \t\tR$25,00
    2\tlasanha             \t\tR$20,00
    3\tstrogonoff          \t\tR$18,00
    4\tbife acebolado      \t\tR$15,00
    5\tPão com ovo         \t\tR$5,00
  
    """)
  o
    match opcao:
      case 1:
        prato = "picanha"
        valor = 250
      case 2:
        prato = "Lasanha"
        valor = 20
      case 3:
        prato = "Strogonoff"
        valor = 15
      case 4:
        prato = "Bife acebolado"
        valor = 15
      case 5:
        prato = "Pão com ovo"
        valor = 5
      case _:
        prato = "opção invalida"
        valor = 0
        
    preco_total += preco
    mais_pedidos = input("deseja fazer um novo pedido?\nuse 's' or 'n' para responder:").lower()
    if mais_pedidos =="n":
        break
    
if preco_total > 0:
    gorjeta_garcom = input("deseja pagar 10% do valor da sua nota como gorjeta para o garçom?")
    if gorjeta_garcom == "s":
        valor_gorjeta = preco_total * 0.10
        
total_pagar = preco_total + valor_gorjeta

print("\n====Nota fiscal ===")
print(f"valor da gorjeta : R$ {valor_gorjeta}") 
print(f"valor total da compra: R$ {total_pagar}")           
