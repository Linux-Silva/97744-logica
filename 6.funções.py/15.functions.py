import os

def limpar_tela():
    os.system("clear")  # Use "cls" se estiver no Windows

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3 (obesidade mórbida)"

# Execução direta (sem função main)
limpar_tela()
try:
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"\nO seu Índice de Massa Corporal (IMC) é: {imc:.2f}")
    print("Classificação:", classificacao)
except ValueError:
    print("Por favor, digite valores numéricos válidos.")