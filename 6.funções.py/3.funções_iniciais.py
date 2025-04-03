import os
os.system("clear")

def tabuada(Num):

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

num = int(input("digite um numero: "))
tabuada(num)