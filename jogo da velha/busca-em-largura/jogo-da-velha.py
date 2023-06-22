def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], "|", end=" ")
        print("\n-------------")

def game_over(board):
    # Verificar linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True

    # Verificar colunas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # Verificar empate
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def evaluate(board):
    # Verificar linhas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return 1
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return -1

    # Verificar colunas
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return 1
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return -1

    # Verificar diagonais
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        return -1

    if board[0][2] == board[1][1] == board[2][0] == "X":
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        return -1

    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1:
        return score - depth
    elif score == -1:
        return score + depth
    elif game_over(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while not game_over(board):
        print_board(board)

        if player == "X":
            print("Jogador X, é sua vez.")
            row = int(input("Digite o número da linha (0-2): "))
            col = int(input("Digite o número da coluna (0-2): "))
            if board[row][col] == " ":
                board[row][col] = player
                player = "O"
            else:
                print("Posição inválida. Tente novamente.")
        else:
            print("Jogador O, é sua vez.")
            move = find_best_move(board)
            row, col = move
            board[row][col] = player
            player = "X"

    print_board(board)
    score = evaluate(board)
    if score == 1:
        print("O jogador X venceu!")
    elif score == -1:
        print("O jogador O venceu!")
    else:
        print("O jogo terminou em empate!")

play_game()