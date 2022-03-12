# Kółko i krzyżyk:
# Program będący implementacją gry w "kółko i krzyżyk" dla dwóch graczy. Wpisz w google "tic tac toe game" i zagraj z google.
#    • Zacznij od zaprojektowania rozgrywki
#   • Możliwość nazwania graczy inaczej niż X / O
#   • Rozszerzeniem gry będzie zmiana 2 gracza na komputer.
#   ◦ Konieczność użycia modułu random.

# stałe ogólne
from ast import main

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Wyświetl instrukcję gry."""
    print(
        """Witaj w grze'Kółko i krzyżyk'. Będzie to rozgrywka między Dwoma graczami lub komuterem.
    
        Swoje posunięcie wskażesz poprzez wprowadzenie cyfry z zakresu 1 - 9.
        Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    
    
                            1 | 2 | 3
                            ---------
                            4 | 5 | 6
                            ---------
                            7 | 8 | 9
    
    Gotowi?. No to zaczynamy!!. \n
        """
    )


def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Ustalić, czy pierwszy ruch należy do gracza P1, czy do gracza P2."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nPierwszy ruch należy do Gracza P1.")
        player1 = X  # gracz człowiek
        player2 = O  # gracz komputer
    else:
        print("\nPierwszy ruch należy do Gracza P2.")
        player2 = X  # gracz komputer
        player2 = O  # gracz człowiek
    return player2, player1

def display_board(board):
    """Wyświetl planszę gry na ekranie."""
    print("\n\t", board[1], "|", board[2], "|", board[3])
    print("\t", "---------")
    print("\t", board[4], "|", board[5], "|", board[6])
    print("\t", "---------")
    print("\t", board[7], "|", board[8], "|", board[9], "\n")


def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Ustal zwycięzcę gry."""
    WAYS_TO_WIN = ((1, 2, 3),
                   (4, 5, 6),
                   (7, 8, 9),
                   (1, 4, 7),
                   (2, 5, 8),
                   (3, 6, 9),
                   (1, 5, 9),
                   (3, 5, 7))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None


def player1_move(board, player1):
    """Odczytaj ruch człowieka."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte!!!  Wybierz inne.\n")
    print("Znakomicie...")
    return move


def computer_move(board, player2, player1):
    """Spowoduj wykonanie ruchu przez komputer."""
    # utwórz kopię roboczą, ponieważ funkcja będzie zmieniać listę
    board = board[:]
    # najlepsze pozycje do zajęcia według kolejności
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Wybieram pole numer", end=" ")

    # jeśli komputer może wygrać, wykonaj ten ruch
    for move in legal_moves(board):
        board[move] = player2
        if winner(board) == player2:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # jeśli człowiek może wygrać, zablokuj ten ruch
    for move in legal_moves(board):
        board[move] = player1
        if winner(board) == player1:
            print(move)
            return move
        # ten ruch został sprawdzony, wycofaj go
        board[move] = EMPTY

    # ponieważ nikt nie może wygrać w następnym ruchu, wybierz najlepsze wolne pole
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """Zmień wykonawcę ruchu."""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, player2, player1):
    """Pogratuluj zwycięzcy."""
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")

    if the_winner == player2:
        print("Zwycięstwo Gracza nr 2!! \n")

    elif the_winner == player1:
        print("Zwycięstwo Gracza nr 1!! \n")


    elif the_winner == TIE:
        print("Remis!!  \n")


def main():
    display_instruct()
    player2, player1 = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == player1:
            move = player1_move(board, player1)
            board[move] = player1
        else:
            move = computer_move(board, player2, player1)
            board[move] = player2
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, player2, player1)

    # rozpocznij program


main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")
