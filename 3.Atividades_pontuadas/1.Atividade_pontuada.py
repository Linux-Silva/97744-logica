import os
os.system("clear")

numero_1 = int(input("digite o primeiro numero:"))
numero_2 = int(input("digite o segundo numero:"))
numero_3 = int(input("digite o terceiro numero:"))

if numero_1 + numero_2 < numero_3:
  print()
  print("A soma do primeiro numero e do segundo e menor que o terceiro")
else :
 numero_1 + numero_2 > numero_3
 print()
 print("a soma do primeiro e do segundo numero e maior que o terceiro")

 print()
 print(f"soma do 1 e 2 numero:{numero_1 + numero_2}")
 print(f"terceiro numero:{numero_3}")