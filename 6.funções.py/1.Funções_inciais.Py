import os
os.system("clear")

# Função sem retorno.
# Definindo caracteristicas da função.
def saudacao(nome):
    print(f"Olá {nome}! Bem vindo ao curso de DS!")
    
# crie uma função com o nome: disciplina que receba o nome de
# uma disciplina do curso de ds.
# mostre o texto.

nome = input("Dgite o seu nome: ")
def disciplina(nome):
    print(f"Seja bem vindo ao curso, essa e a sua nova materia : {nome}")
    
saudacao(nome)
disciplina("Logica de progamação") 
