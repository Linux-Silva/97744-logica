import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:
    nome = str
    biografia = str

@dataclass
class Livro:
    titulo = str
    ano = int
    autor = Autor

    def exibir_detalhes(self):
        return [
            f"Título: {self.titulo}",
            f"Ano de publicação: {self.ano}",
            f"Autor: {self.autor.nome}",
            f"Biografia do autor: {self.autor.biografia}"
        ]


autor1 = Autor()
autor1.nome = "Clarice Lispector"
autor1.biografia = "Clarice: Uma Vida que se Conta"

livro1 = Livro()
livro1.titulo = "A hora da estrela"
livro1.ano = 1977
livro1.autor = autor1

detalhes_livro = livro1.exibir_detalhes()

for detalhe in detalhes_livro:
    print(detalhe)
