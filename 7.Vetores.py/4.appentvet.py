import os
os.system("clear || cls")

menu = []

print("""
 =========MENU=========
 Código  \t prato     \tvalor
 1    \t\tPicanha     \t\t250,00
 2    \t\tLasanha      \t\t20,00
 3   \t\tStrogonoff    \t\t15,00
 4    \t\tBife acebolado\t\t15,00
 5    \t\tPão com ovo    \t\t5,00
 """)

while True:
    try:
        opcao = int(input("entrez l'option souhaitée (0 pour terminer): "))
        if opcao == 0:
            break
        match opcao:
            case 1:
                prato = "Picanha"
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
                print("opção inválida\n")
                continue

        menu.append((prato, valor))
        print(f"{prato} adicionado ao pedido.\n")
    except ValueError:
        print("Entrada inválida. Digite apenas números.\n")

print()
print("======= RESUMO DO PEDIDO =======")
total = 0
for i, item in enumerate(menu, 1):
    print(f"{i}. prato: {item[0]} | valor: R$ {item[1]:.2f}")
    total += item[1]

print(f"\nvalor total: R$ {total:.2f}")
