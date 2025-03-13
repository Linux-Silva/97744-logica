import os

os.system("clear")


print("""
 ===========HORTI FRUTI============
 Código  \t frutas    \tvalor
       \t\tMelancia    \t\t2,20
       \t\tMorango     \t\t1,80
 """)

quant_melancia = float(input("Diga a quantidade de melancias: "))
quant_morango = float(input("Diga a quantidade de morangos: "))

melancia = float(2.50)
melancia_2 = float(2.50)
morango = float(1.80)
morango_2 = float(1.50)

if quant_melancia or quant_morango <=5:
    total=(quant_melancia*melancia)+(quant_morango*morango)
    print(f"total: {total}")
elif quant_melancia or quant_morango >8:
    total=(quant_melancia*melancia)+(quant_morango*morango)
    total_final+(total*0.10)
    print(f"valor a ser pago: {total_final} ")





























