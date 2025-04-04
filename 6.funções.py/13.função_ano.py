import os
os.system("clear")

def ano(n1):
    if n1 > 2025: 
        return "Error 404"
    
    calculo = 2025 - n1
    return calculo

n1 = int(input("Digite o seu ano de nascimento: "))
ano_nascimento = ano(n1)

print(f"A sua idade {ano_nascimento}")