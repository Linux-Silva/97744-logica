import os

os.system("cls | clear")

while True:
    nota = int(input("digite a primeira nota: "))
    nota_2 = int(input("digite a segunda nota: "))
    
    print()

    if nota < 0 or nota > 10:
        print("nota invalida> \ntente novamente: ")
        
        print()

    elif nota_2  or nota_2 > 10:
        print("nota invalida. \nTente novamente: ")

        print()

    else:
        break

soma = (nota = nota_2)
media = (Soma) / 2

print()
print (f"A sua media é: {media}")
print()
print("fim.")

 