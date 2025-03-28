import os
import time

os.system("clear")
contador =  total_familia =  media_salario_populacao =  numero_filhos = maior_salario = 0
menor_salario = 999999
while True:
    print("""
\nCodigo | Descriçao
    \n1  |  Adicionar familia
    \n2  |  Sair e Exibir resultados
""")
    
    opcao = int(input("Digite a opçao desejada: "))

    match opcao:
        case 1:
            filhos = float(input("Informe a quantidade de filhos: "))
            salario = float(input("Informe o salario ganho pela familia: "))
            contador += 1
            total_familia += 1
            media_salario_populacao += salario / contador
            numero_filhos += filhos / contador

            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario
            os.system("clear")

        case 2:
            if contador > 0:
                print("\n= Exibindo resultados = ")
                print(f"Total de familias: {total_familia}")
                print(f"Media de salario da populaçao: {media_salario_populacao}")
                print(f"Media dos numeros de filhos da familias: {numero_filhos}")
                print(f"Maior salario do grupo: R${maior_salario}")
                print(f"Menor salario do grupo: R${menor_salario}")
            else:
                print("Nao existem dados para Exibir. ")

            time.sleep(15)
            os.system("clear")
            break