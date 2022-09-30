"""
Plain minimax search vs alpha-beta prunning
"""
from minimax_search import minimax_search
from alpha_beta_search import alpha_beta_search
from game import Game
import time


def validate_range(move):

    row, col = move

    if row >= 0 and row <= 2 and col >= 0 and col <= 2:
        return True

    return False


def validate_position(board, move):

    row, col = move
    if board[row][col] == "":
        return True

    return False


def get_token(turn):
    if turn:
        return "x"
    return "o"


def print_board(board):
    for row in board:
        out_str = ""
        for col in row:
            if col == "":
                new_token = " "
            else:
                new_token = col
            out_str += "|" + new_token + "|"
        print(out_str)


if __name__ == "__main__":
    game = Game()
    board = [["", "", ""], ["", "", ""], ["", "", ""]]

    turn = True
    times = []
    alpha_beta_times = []

    while True:

        if turn:
            # Human move
            while True:
                print("Turno humano")
                print_board(board)
                print("Ingresa un movimiento")
                row = int(input("Fila: "))
                col = int(input("Columna: "))
                move = (row, col)
                if validate_position(board, move) and validate_range(move):
                    break
                print("Movimiento inválido")

        else:
            # AI move
            print("Turno IA")
            print_board(board)

            # Plain minimax move
            start = time.time()
            move = alpha_beta_search(game, board)
            end = time.time()

            decision_time = end - start
            alpha_beta_times.append(decision_time)

            # alpha beta search minimax move
            start = time.time()
            move = minimax_search(game, board)
            end = time.time()

            decision_time = end - start
            times.append(decision_time)

        board[move[0]][move[1]] = get_token(turn)

        # Check end of game
        if game.is_terminal(board):
            print("Resultados:")
            print_board(board)
            utility = game.utility(board, "x")
            if utility == 1:
                print("Ganó humano!")

            elif utility == -1:
                print("Ganó IA")
            else:
                print("Empate!")

            mean_minimax = sum(times) / len(times)
            print(f"Tiempo de decision promedio minimax: {mean_minimax}")

            mean_alpha_beta = sum(alpha_beta_times) / len(alpha_beta_times)
            print(
                f"Tiempo de decision promedio minimax con poda alfa - beta: {mean_alpha_beta}"
            )

            print(f"Razón alfa - beta / minimax: {mean_alpha_beta / mean_minimax}")
            break
        turn = not turn
