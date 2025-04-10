import os
import random
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_mapa(player_pos, inimigos, tiros, fase, kills, pontos, vida):
    mapa = [[' ' for _ in range(20)] for _ in range(10)]
    
    jogador = [
        "  O  ",
        " /|\\ ",
        " / \\ "
    ]
    for i, linha in enumerate(jogador):
        for j, char in enumerate(linha):
            x, y = player_pos[0] + j - 2, player_pos[1] + i - 1
            if 0 <= x < 20 and 0 <= y < 10:
                mapa[y][x] = char
    
    inimigo_sprite = [
        " I ",
        "/|\\",
        "/ \\" 
    ]
    for inimigo in inimigos:
        for i, linha in enumerate(inimigo_sprite):
            for j, char in enumerate(linha):
                x, y = inimigo[0] + j - 1, inimigo[1] + i - 1
                if 0 <= x < 20 and 0 <= y < 10:
                    mapa[y][x] = char
    
    for tiro in tiros:
        if 0 <= tiro[1] < 10 and 0 <= tiro[0] < 20:
            mapa[tiro[1]][tiro[0]] = '|'
    
    print(f"Fase: {fase} | Kills: {kills} | Pontos: {pontos} | Vida: {vida}")
    for linha in mapa:
        print(''.join(linha))

def mover_jogador(player_pos, comando, inimigos):
    direcoes = {'a': (-1, 0), 'd': (1, 0), 'w': (0, -1), 's': (0, 1)}
    if comando in direcoes:
        nova_pos = [player_pos[0] + direcoes[comando][0], player_pos[1] + direcoes[comando][1]]
        if tuple(nova_pos) not in inimigos and 0 <= nova_pos[0] < 20 and 0 <= nova_pos[1] < 10:
            player_pos[:] = nova_pos

def mover_inimigos(inimigos, player_pos):
    novos_inimigos = set()
    for inimigo in inimigos:
        dx = (player_pos[0] > inimigo[0]) - (player_pos[0] < inimigo[0])
        dy = random.choice([-1, 1]) if random.random() < 0.5 else 0
        novo_x, novo_y = inimigo[0] + dx, inimigo[1] + dy
        if 0 <= novo_x < 20 and 0 <= novo_y < 10:
            novos_inimigos.add((novo_x, novo_y))
        else:
            novos_inimigos.add(tuple(inimigo))
    return list(novos_inimigos)

def disparar(player_pos, tiros, inimigos):
    if inimigos:
        alvo = min(inimigos, key=lambda inimigo: abs(inimigo[0] - player_pos[0]) + abs(inimigo[1] - player_pos[1]))
        tiros.append([alvo[0], alvo[1]])

def mover_tiros(tiros):
    return [[x, y - 1] for x, y in tiros if y - 1 >= 0]

def checar_colisao(tiros, inimigos, pontos, player_pos, kills):
    tiros_restantes = []
    inimigos_restantes = set(inimigos)
    for tiro in tiros:
        if tuple(tiro) in inimigos_restantes:
            inimigos_restantes.remove(tuple(tiro))
            kills += 1
            pontos += 15
            inimigos_restantes.add((random.randint(0, 19), player_pos[1] + 2))
        else:
            tiros_restantes.append(tiro)
    return tiros_restantes, list(inimigos_restantes), pontos, kills

def jogo():
    fase = 1
    player_pos = [10, 9]
    tiros = []
    pontos = 0
    kills = 0
    vida = 100
    inimigos = {(random.randint(0, 19), random.randint(0, 5)) for _ in range(3)}  # Começa com 3 inimigos
    
    while True:
        limpar_tela()
        desenhar_mapa(player_pos, inimigos, tiros, fase, kills, pontos, vida)
        
        comando = input("Use 'a', 'd', 'w', 's' para mover, 'r' para atirar, 'quit' para sair: ")
        
        if comando.lower() == 'quit':
            print(f"Você saiu do jogo. Sua pontuação final foi: {pontos} | Kills: {kills}")
            break
        
        if comando == 'r':
            disparar(player_pos, tiros, inimigos)
        
        mover_jogador(player_pos, comando, inimigos)
        inimigos = mover_inimigos(inimigos, player_pos)
        tiros = mover_tiros(tiros)
        tiros, inimigos, pontos, kills = checar_colisao(tiros, inimigos, pontos, player_pos, kills)
        
        if tuple(player_pos) in inimigos:
            limpar_tela()
            desenhar_mapa(player_pos, inimigos, tiros, fase, kills, pontos, vida)
            print("Game Over! Você foi atingido por um inimigo!")
            break
        
        time.sleep(0.1)
    
    print(f"Fim de jogo. Sua pontuação final foi: {pontos} | Kills: {kills}")

if __name__ == "__main__":
    jogo()
