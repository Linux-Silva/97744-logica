import os
import time
import random

LARGURA = 7  # Largura da pista
ALTURA = 15  # Altura da tela
carro_pos = 3  # Posição inicial do carro

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_pista(obstaculos, carro_pos, score):
    pista = [[' ' for _ in range(LARGURA)] for _ in range(ALTURA)]

    # Coloca os obstáculos
    for (x, y) in obstaculos:
        if 0 <= y < ALTURA:
            pista[y][x] = 'X'

    # Coloca o carro
    pista[-1][carro_pos] = 'A'

    # Desenha a pista
    limpar_tela()
    print(f"Pontuação: {score}")
    print("=" * (LARGURA + 2))
    for linha in pista:
        print("|" + ''.join(linha) + "|")
    print("=" * (LARGURA + 2))

def mover_obstaculos(obstaculos):
    return [(x, y + 1) for x, y in obstaculos if y + 1 < ALTURA]

def verificar_colisao(obstaculos, carro_pos):
    for (x, y) in obstaculos:
        if y == ALTURA - 1 and x == carro_pos:
            return True
    return False

def jogo():
    global carro_pos
    obstaculos = []
    score = 0
    velocidade = 0.2

    while True:
        if random.random() < 0.3:
            obstaculos.append((random.randint(0, LARGURA - 1), 0))

        desenhar_pista(obstaculos, carro_pos, score)

        if verificar_colisao(obstaculos, carro_pos):
            print("💥 Game Over! Você bateu!")
            print(f"Pontuação final: {score}")
            break

        comando = input("Mover (a/esquerda, d/direita, q/sair): ").lower()
        if comando == 'a' and carro_pos > 0:
            carro_pos -= 1
        elif comando == 'd' and carro_pos < LARGURA - 1:
            carro_pos += 1
        elif comando == 'q':
            print("Jogo encerrado.")
            break

        obstaculos = mover_obstaculos(obstaculos)
        score += 1
        time.sleep(velocidade)

if __name__ == "__main__":
    jogo()
