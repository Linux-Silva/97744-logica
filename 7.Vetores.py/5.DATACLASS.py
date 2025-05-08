import os
from dataclasses import dataclass

os.system("cls||clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    
@dataclass
class Pet:
    nome: str
    idade: int 
    peso: float

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet("Totó", 4, 7.8)
pet2 = Pet("Shark", 6, 9.2)

print("\n= Dados da pessoa =")
print(f"nome: {pessoa1.nome}, idade: {pessoa1.idade} anos.")
print(f"nome: {pessoa2.nome}, idade: {pessoa2.idade} anos.")

print("\n= Dados do pet =")
print(f"nome: {pet1.nome}, idade: {pet1.idade} anos, peso: {pet1.peso} kg.")
print(f"nome: {pet2.nome}, idade: {pet2.idade} anos, peso: {pet2.peso} kg.")
