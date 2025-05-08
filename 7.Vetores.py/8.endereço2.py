import os
from dataclasses import dataclass
os.system

class Endereco:
    def solicitar_dados(self):
        self.logradouro = input("Digite o seu endereço
                                : ")
        self.numero = int(input("Digite o número da residência: "))
        self.cidade = input("Digite a cidade: ")

class Pessoa:
    def solicitar_dados(self):
        self.nome = input("Digite o nome: ")
        self.email = input("Digite o email: ")
        self.endereco = Endereco()  # Criando a instância de Endereco aqui
        self.endereco.solicitar_dados()

    def exibir_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, {self.endereco.numero} - {self.endereco.cidade}")


pessoa = Pessoa()
pessoa.solicitar_dados()
pessoa.exibir_dados()
