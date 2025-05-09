import os
from dataclasses import dataclass
os.system ("clear || cls")


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = []  # Criando uma lista para adicionar clientes.
QUANTIDADE_CLIENTES = 2  # Constante que define a quantidade de clientes.

# Laço de repetição para adicionar clientes.
print("Informe os dados do cliente: ")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(  # Instanciando um objeto.
        nome=input("Nome: "),
        email=input("E-mail: "),
        telefone=input("Telefone: ")
    )
    lista_clientes.append(cliente)  # Adicionando um cliente na lista.
    print()

# Laço de repetição para exibir dados dos clientes.
print("\nExibindo dados dos clientes:")
for cliente in lista_clientes:  # Mostra os dados por elementos na lista.
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
    print()

print("= Salvando os dados dos clientes =")
nome_arquivo = "dados_clientes.txt"

with open(nome_arquivo, "a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome},{cliente.email},{cliente.telefone}\n")

print("\nSalvo com sucesso!")
