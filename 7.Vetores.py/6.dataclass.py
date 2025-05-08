import os
from dataclasses import dataclass

os.system("cls||clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa("Alice", 30, 50.0, 1.76)
pessoa2 = Pessoa("Bob", 25, 75.0, 1.67)


print("\n= Dados da pessoa =")
print(f"nome: {pessoa1.nome}, idade: {pessoa1.idade} anos, peso: {pessoa1.peso} kg, altura: {pessoa1.altura} m.")
print(f"nome: {pessoa2.nome}, idade: {pessoa2.idade} anos, peso: {pessoa2.peso} kg, altura: {pessoa2.altura} m.")


