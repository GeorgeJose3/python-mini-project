import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def evaluate(board):
    
    for row in board:
        if all(cell == 'X' for cell in row):
            return 10
        elif all(cell == 'O' for cell in row):
            return -10
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 10
        elif all(board[row][col] == 'O' for row in range(3)):
            return -10
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 10
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return -10
    
    return 0

def is_moves_left(board):
    return any(cell == ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)

    if score == 10:
        return score - depth
    elif score == -10:
        return score + depth
    elif not is_moves_left(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while is_moves_left(board) and evaluate(board) == 0:
        print_board(board)
        if current_player == 'X':
            row, col = find_best_move(board)
            print(f"Computer chooses row {row}, col {col}")
        else:
            row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter col (0, 1, 2): "))
        board[row][col] = current_player
        current_player = 'O' if current_player == 'X' else 'X'
    print_board(board)
    score = evaluate(board)
    if score == 10:
        print("Computer wins!")
    elif score == -10:
        print("Player O wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()

