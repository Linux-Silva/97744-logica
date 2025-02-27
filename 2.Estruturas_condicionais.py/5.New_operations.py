import os

os.system("clear")


print("""
 =========MENIVIS=========
 Código  \t prato     \tvalor
 1    \t\tPicanha     \t\t250,00
 2    \t\tLasanha      \t\t20,00
 3   \t\tStrogonoff    \t\t15,00
 4    \t\tBife acebolado\t\t15,00
 5    \t\tPão com ovo    \t\t5,00

 """)

opcao = int(input("entrez l'option souhaitée:"))

match opcao :
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
    
print()
print(f"prato: {prato}")
print(f"valor: R$ {valor: .2f}")






