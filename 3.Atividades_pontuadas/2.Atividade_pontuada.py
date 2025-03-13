import os
os.system("clear")

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo (M/F): ")
estado_civil = input("Digite o seu estado civil: ").lower


if sexo == "F" and estado_civil == "casada" or "casado":
    tempo_casado = int(input("Digite o tempo de casado : "))
print()
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
if sexo == "F" and estado_civil == "casada" or "casado":
    print(f"Tempo de casada: {tempo_casado} anos")
