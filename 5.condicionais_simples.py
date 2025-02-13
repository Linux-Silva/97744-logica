import os

#Limpa o terminal.
os.system("clear")

# Solicitando Dados (Entrada)
idade = int(input("digite sua idade:"))

# Verificando (Processamento)
if idade < 18:
    print("menor de idade!")
else:
    print("maior de idade!")

# Exibindo dados (saida)
print("----The Majestic END----")

