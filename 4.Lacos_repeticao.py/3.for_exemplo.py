import os
import time

os.system("clear")

print("contagem de 2 em 2.")
for i in range(1 ,11, 2):
    print(f"valor da variavel i: {i}")
    time.sleep(1) #espera 1 segundo


print("acabou")