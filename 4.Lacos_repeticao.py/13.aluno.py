import os

os.system("cls | clear")

while True:

  idade = int(input("digite a sua idade: "))

  if idade < 18:
     print("Não autorizado> \nsomente maiores de 18. \n")
  else:
     break
  
print("acesso permitido")
print("FIM")


