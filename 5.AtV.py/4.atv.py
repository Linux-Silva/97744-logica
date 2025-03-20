import os
os.system("cls | clear")

usuario_correto = "adm of his page"
senha_correta = "mia khalifa 123"

for i in range(3):
    login = input("digite o seu login: ")

    print()

    senha = input("digite a sua senha: ")

    if login == usuario_correto and senha == senha_correta:
        print("Seja bem vindo novamente -==adm of his page==-")

        break

    else:
     print("login e senha incorretos")
     if i == 3:

         print("\nTente o login novamente")
     