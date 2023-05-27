# Define o tabuleiro do jogo
tabuleiro = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Define os símbolos dos jogadores
jogador1 = "X"
jogador2 = "O"

# Função para imprimir o tabuleiro
def imprimir_tabuleiro():
    for linha in tabuleiro:
        print("|".join(linha))

# Função para verificar se um jogador venceu o jogo
def verificar_vitoria(jogador):
    # Verifica as linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    
    # Verifica as colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True
    
    # Verifica as diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    
    return False

# Loop principal do jogo
jogador_atual = jogador1
while True:
    # Imprime o tabuleiro atual
    imprimir_tabuleiro()
    
    # Pede ao jogador atual para fazer sua jogada
    linha = int(input(f"{jogador_atual}, escolha uma linha (0, 1 ou 2): "))
    coluna = int(input(f"{jogador_atual}, escolha uma coluna (0, 1 ou 2): "))
    
    # Verifica se a jogada é válida
    if tabuleiro[linha][coluna] != "-":
        print("Jogada inválida, tente novamente.")
        continue
    
    # Faz a jogada
    tabuleiro[linha][coluna] = jogador_atual
    
    # Verifica se o jogador venceu
    if verificar_vitoria(jogador_atual):
        imprimir_tabuleiro()
        print(f"{jogador_atual} venceu o jogo!")
        break
    
    # Verifica se o jogo terminou em empate
    if all("-" not in linha for linha in tabuleiro):
        imprimir_tabuleiro()
        print("O jogo terminou em empate!")
        break
    
    # Passa a vez para o próximo jogador
    jogador_atual = jogador2 if jogador_atual == jogador1 else jogador1