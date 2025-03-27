import os
os.system("cls || clear")
dados = []

def adicionar_pessoa():
    os.system('cls' if os.name == 'nt' else 'clear')
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").strip().upper()
    salario = float(input("Salário: "))
    dados.append((idade, sexo, salario))

def exibir_resultados():
    if not dados:
        print("Nenhum dado disponível.")
        return
    
    salarios = [s for _, _, s in dados]
    idades = [i for i, _, _ in dados]
    mulheres_5000 = sum(1 for i, s, sal in dados if s == 'F' and sal >= 5000)
    
    print(f"Média salarial: R$ {sum(salarios) / len(salarios):.2f}")
    print(f"Maior idade: {max(idades)}, Menor idade: {min(idades)}")
    print(f"Mulheres com salário >= R$ 5000: {mulheres_5000}")

def menu():
    while True:
        print("\n1 - Adicionar pessoa\n2 - Exibir resultados\n3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar_pessoa()
        elif opcao == '2':
            exibir_resultados()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")

menu()
