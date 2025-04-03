import os
os.system("clear")

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    if media >= 7:
        return "Aluno aprovado!"
    else:
        return "Aluno reprovado."

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = calcular_media(nota1, nota2)
print(f"Média do aluno: {media:.2f}")
print(verificar_aprovacao(media))
