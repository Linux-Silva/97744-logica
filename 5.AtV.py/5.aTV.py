import os
import time
os.system("cls | clear")

quantidade = 3
soma = 0
for i in range(quantidade):
     while True:
            nota = float(input(f"digite a {i+1}ª nota: "))
           
            if nota < 0 or nota > 10:
                print("nota invalida, tente novamente. ")
            else:
                 soma += nota
                 break
      
            
            
media = soma / quantidade
print()
print(f"media: {media:.1f}")
print()
if media >= 7:
      print("APROVED")
      print("deseja inserir mais uma nota?")
elif media >= 5 and media < 7:
      print("recuperação")
      print("deseja inserir mais uma nota?")
else:
      print("reprovado")
      print("deseja inserir mais uma nota?")
      print()
