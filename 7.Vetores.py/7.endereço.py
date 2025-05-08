import os
from dataclasses import dataclass

os.system("cls||clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
   #variaveis = atributos
    nome: str
    idade: int
    endereco: Endereco
    
   #Função = Metodo
    def exibir_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}, número {self.endereco.numero}")
        
    #Aplicando caracteristicas da classe.
endereco1 = Endereco("Rua 21 de setembro", 123)
pessoa1 = Pessoa("Titako", 44, endereco1)
pessoa1.exibir_dados()

print()

endereco2 = Endereco("Rua Tamanduá", 47)
pessoa2 = Pessoa("Mario", 76, endereco2)
pessoa2.exibir_dados()
