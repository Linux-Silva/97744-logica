import os

os.system("clear")

6
print("""
 /=========Calendario=========\
 Código  \t Dia da semana 
 1    \t\t Segunda   
 2    \t\t Terca
 3   \t\t  Quarta
 4    \t\t Quinta
 5   \t\t Sexta
 6    \t\t Sabado
 7    \t\t Domingo
 """)

opcao = int(input("digite o codgio correspondente ao dia da semana : "))

match opcao :
    case 1 :
        dia = "segunda"
        semana = "dia útil" 
    case 2 :
        dia = "terça"
        semana = "dia útil"
    case 3 :
        dia = "quarta" 
        semana = "dia útil"
    case 4 :
        dia = "quinta"
        semana = "dia útil"
    case 5 :
        dia = "sexta"
        semana = "dia útil"
    case 6 :
        dia = "sabado"
        semana = "final de semana"
    case 7 :
        dia = "domingo"    
        semana = "final de semana"
    case _:
         dia = "invalido"
         semana = ""
    
print()
print(f"Dia da semana: {dia}")
print(f"corresponde a : {semana}")


