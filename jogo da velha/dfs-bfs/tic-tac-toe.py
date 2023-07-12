from collections import deque

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def check_winner(board):
    # Verifica linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]

    # Verifica colunas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def bfs(board):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    queue = deque([(board, "X")])
    while queue:
        curr_board, curr_player = queue.popleft()

        winner = check_winner(curr_board)
        if winner:
            return scores[winner]

        if is_board_full(curr_board):
            return scores["tie"]

        for i in range(3):
            for j in range(3):
                if curr_board[i][j] == " ":
                    new_board = [row.copy() for row in curr_board]
                    new_board[i][j] = curr_player
                    queue.append((new_board, "O" if curr_player == "X" else "X"))

    return 0

def dfs(board, depth, player):
    scores = {
        "X": 1,
        "O": -1,
        "tie": 0
    }

    winner = check_winner(board)
    if winner:
        return scores[winner]

    if is_board_full(board):
        return scores["tie"]

    best_score = float("-inf") if player == "X" else float("inf")
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if player == "X":
                    score = dfs(board, depth + 1, "O")
                    best_score = max(best_score, score)
                else:
                    score = dfs(board, depth + 1, "X")
                    best_score = min(best_score, score)
                board[i][j] = " "

    return best_score

def make_best_move(board, algorithm):
    if algorithm == "DFS":
        best_score = float("-inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = dfs(board, 0, "O")
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move
    elif algorithm == "BFS":
        best_score = float("-inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = bfs(board)
                    board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Bem-vindo ao Jogo da Velha!")

    algorithm = input("Escolha o algoritmo para a máquina (DFS ou BFS): ").upper()
    while algorithm != "DFS" and algorithm != "BFS":
        print("Opção inválida. Por favor, escolha entre DFS ou BFS.")
        algorithm = input("Escolha o algoritmo para a máquina (DFS ou BFS): ").upper()

    print(f"Você escolheu o algoritmo {algorithm} para a máquina.")
    print("Você está jogando contra a máquina.")
    print_board(board)

    while True:
        # Jogada do usuário
        row = int(input("Digite o número da linha (0-2): "))
        col = int(input("Digite o número da coluna (0-2): "))

        if board[row][col] != " ":
            print("Posição inválida. Tente novamente.")
            continue

        board[row][col] = "O"
        print_board(board)

        winner = check_winner(board)
        if winner:
            print("Parabéns! Você venceu!")
            break

        if is_board_full(board):
            print("Empate!")
            break

        # Jogada da máquina
        print("A máquina está pensando...")
        row, col = make_best_move(board, algorithm)
        board[row][col] = "X"
        print_board(board)

        winner = check_winner(board)
        if winner:
            print("A máquina venceu! Tente novamente.")
            break

        if is_board_full(board):
            print("Empate!")
            break

play_game()
