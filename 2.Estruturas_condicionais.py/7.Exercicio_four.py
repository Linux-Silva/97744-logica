import os
os.system("clear")


print("""
 /=========Calendario=========\
{print}
1        \t Janeiro
2        \t Fevereiro
3        \t Março
4        \t Abril
5        \t Maio 
6        \t Junho
7        \t Julho
8        \t Agosto
9        \t Setembro
10       \t Outubro
11       \t Novembro
12       \t Dezembro
""")
opcao = int(input("digtite o numero correspondente com o mês: "))

match opcao :
    case 1 :
        resultado = "Janeiro"
    case 2 :
        resultado = "Fevereiro"
    case 3 :
        resultado = "Março" 
    case 4 :
        resultado = "Abril"
    case 5 :
        resultado = "Maio"
    case 6 :
        resultado = "Junho"
    case 7 :
        resultado = "Julho"    
    case 8 :
        resultado = "Agosto"    
    case 9 :
        resultado = "setembro"    
    case 10 :
        resultado = "Outubro"    
    case 11 :
        resultado = "Novembro"    
    case 12 :
        resultado = "Dezembro"    

    
print()
print(f"resultado : {resultado}")

      

