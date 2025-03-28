import os
import time

os.system("clear")


contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0
while True:
    print("""
\nCodigo| Descriçao
     \n1| Adicionar pessoa
     \n2| Exibir resultados
     \n3| Sair
         """)
    opcao = int(input("Digite a opçao desejada: "))

    match opcao:
        case 1:
            idade = int(input("Digite a idade: "))
            sexo = input("Informe o Sexo com 'M' ou 'F': ")
            salario = float(input("Informe o salario: "))
            contador += 1
            soma_salario += salario
            #maior_idade = idade if idade > maior_idade else maior_idade
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
            os.system("clear")
        case 2:
            if contador > 0:
                media_salario_grupo = soma_salario / contador
                print("\n= Exibindo resultados = ")
                print(f"Media de salario do grupo: {media_salario_grupo}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidades de mulheres com salario a partir de 5k: : {mulheres5k}")
            else:
                print("Nao existem dados para Exibir. ")

            time.sleep(5)
            os.system("clear")               
        case 3:
            print("\nfim do programa. ")
            break
        case _:
            print("Nao existem dados para Exibir. ")

            time.sleep(5)
            os.system("clear")
