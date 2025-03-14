import os
import time

os.system("clear")
numero = int(input("digite o numero solicitado : "))

print("======Contagem regressiva======")

for i in range(numero,0, -1):
   print(f"Contagem regressiva: {i}")
   time.sleep(1)

print("====END====2")
