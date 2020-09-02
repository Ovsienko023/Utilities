
X = "X"
O = "0"
EMPTY = " "
TIE = "Draw"
NUM_SQUARES = 9


def display_instruct():
    """Displays instructions for the player. """

    print(
        """
        To make a move, enter a number from 0 to 8.
        The numbers correspond to the position on the
        board, as shown below:

                0 | 1 | 2
                ---------
                3 | 4 | 5
                ---------
                6 | 7 | 8
            """
    )


def ask_yes_no(question):
    """ Asks a question, Yes or No """

    response = None

    while response not in("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """ Asks to enter a number from the range 0 to 8 """

    response = None

    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """ Determines who walks first """

    go_first = ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")

    if go_first == 'y':
        print("Ты ходишь крестиком: ( X )")
        human = 'X'
        computer = '0'
    else:
        print("Ты ходишь ноликом: ( 0 )")
        human = '0'
        computer = 'X'
    return computer, human


def new_board():
    """ Creat new game-board """

    board = list()
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """ Print game-board """

    print(
        f"""
        {board[0]} | {board[1]} | {board[2]}
        ---------
        {board[3]} | {board[4]} | {board[5]}
        ---------
        {board[6]} | {board[7]} | {board[8]}
        """
    )


def legal_moves(board):
    """ list moves """

    moves = list()
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE


def human_move(board, human):
    """ Gets the move of man """

    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход. Выбери поле от 0 до 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("Поле занято, выбери другое. ")
    return move


def computer_move(board, computer, human):
    """ Makes a move for a computer adversary """

    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Я выбераю поле №", end=' ')

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if board[move] == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """ Transition  """

    if turn == 'X':
        return '0'
    else:
        return 'X'


def congrat_winner(the_winner, computer, human):
    """ Congratulations to the winner of the game """

    if the_winner != TIE:
        print("Три", the_winner, "в ряд! \n")
    else:
        print("Ничья")

    if the_winner == computer:
        print("Ты проиграл! \n")
    elif the_winner == human:
        print("Победа! \n")

    elif the_winner == TIE:
        print("Ничья! \n")


def main():
    display_instruct()
    computer, human = pieces()
    turn = 'X'
    board = new_board()
    display_board(board)
    while not winner(board):
        print(winner(board))
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input("\n\nНажмите Enter, что бы выйти.")
