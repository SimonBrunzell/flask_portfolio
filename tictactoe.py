import random

#set up the tic tac toe board
board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

#print the board
def make_board(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("---------")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("---------")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

make_board(board)

move = "player" #to check whose turn it is for the while loop

#to make the first move of the game
def first_player_move(board, move):
    # get the player's first move
    position = input("where would you like to move? ")
    position = int(position)

    # ensure the player's move is valid
    while (position < 1 or position > 9):
        position = input("please give a position between 1 and 9 ")
        position = int(position)


    board[position] = 'X'
    make_board(board)
    move = "computer"

first_player_move(board, move)

#to make the computer's first move
def computer_move(board, move):
    computer_position = random.randint(1,9)
    while board[computer_position] == 'X':
        computer_position = random.randint(1,9)

    board[computer_position] = 'O'

    make_board(board)
    move = "player"

computer_move(board, move)

#to make the player's subsequent moves
def player_next_move(board, move):
    position = input("Please input your next move: ")
    position = int(position)

    while (position < 1 or position > 9 or board[position] == 'X' or board[position] == 'O'):
        position = input("Please input your next move between 1 and 9 or in an empty space: ")
        position = int(position)

    board[position] = 'X'
    make_board(board)
    move = "computer"

player_next_move(board, move)

#to make the computer's subsequent moves
def computer_next_move(board, move):
    computer_position = random.randint(1,9)
    while (computer_position < 1 or computer_position > 9 or board[computer_position] == 'X' or board[computer_position] == 'O'):
        computer_position = random.randint(1,9)

    board[computer_position] = 'O'

    make_board(board)
    move = "player"

computer_next_move(board, move)

win = False #to use in while loop

#to check if a player has won
def check_if_won(board):

    position_1 = board[1]
    position_2 = board[2]
    position_3 = board[3]
    position_4 = board[4]
    position_5 = board[5]
    position_6 = board[6]
    position_7 = board[7]
    position_8 = board[8]
    position_9 = board[9]

    if (position_1 == position_2 == position_3 == 'X') or (position_4 == position_5 == position_6 == 'X') or (position_7 == position_8 == position_9 == 'X') or (position_1 == position_4 == position_7 == 'X') or (position_2 == position_5 == position_8 == 'X') or (position_3 == position_6 == position_9 == 'X') or (position_1 == position_5 == position_9 == 'X') or (position_3 == position_5 == position_7 == 'X'):
        print("you win!")
        return True
    if (position_1 == position_2 == position_3 == 'O') or (position_4 == position_5 == position_6 == 'O') or (position_7 == position_8 == position_9 == 'O') or (position_1 == position_4 == position_7 == 'O') or (position_2 == position_5 == position_8 == 'O') or (position_3 == position_6 == position_9 == 'O') or (position_1 == position_5 == position_9 == 'O') or (position_3 == position_5 == position_7 == 'O'):
        print("computer wins :(")
        return True
    else:
        return False

check_if_won(board)

#to continue the game and then end it
def end_game(win, move):
    while (win == False):
        if (move == "player"):
            player_next_move(board, move)
            move = "computer"
            win = check_if_won(board)
        if (move == "computer"):
            computer_next_move(board, move)
            move = "player"
            win = check_if_won(board)

            #could change while loop to a for loop that iterates 9 times, but if someone wins is broken, otherwise prints tie

end_game(win, move)


# class TicTacToe:
#
#     def __init__(self):
#         self.board = []
#
#     def create_board(self):
#         for i in range(3):
#             row = []
#             for j in range(3):
#                 row.append('-')
#             self.board.append(row)
#
#     def get_random_first_player(self):
#         return random.randint(0, 1)
#
#     def fix_spot(self, row, col, player):
#         self.board[row][col] = player
#
#     def is_player_win(self, player):
#         win = None
#
#         n = len(self.board)
#
#         # checking rows
#         for i in range(n):
#             win = True
#             for j in range(n):
#                 if self.board[i][j] != player:
#                     win = False
#                     break
#             if win:
#                 return win
#
#         # checking columns
#         for i in range(n):
#             win = True
#             for j in range(n):
#                 if self.board[j][i] != player:
#                     win = False
#                     break
#             if win:
#                 return win
#
#         # checking diagonals
#         win = True
#         for i in range(n):
#             if self.board[i][i] != player:
#                 win = False
#                 break
#         if win:
#             return win
#
#         win = True
#         for i in range(n):
#             if self.board[i][n - 1 - i] != player:
#                 win = False
#                 break
#         if win:
#             return win
#         return False
#
#         for row in self.board:
#             for item in row:
#                 if item == '-':
#                     return False
#         return True
#
#     def is_board_filled(self):
#         for row in self.board:
#             for item in row:
#                 if item == '-':
#                     return False
#         return True
#
#     def swap_player_turn(self, player):
#         return 'X' if player == 'O' else 'O'
#
#     def show_board(self):
#         for row in self.board:
#             for item in row:
#                 print(item, end=" ")
#             print()
#
#     def start(self):
#         self.create_board()
#
#         player = 'X' if self.get_random_first_player() == 1 else 'O'
#         while True:
#             print(f"Player {player} turn")
#
#             self.show_board()
#
#             # taking user input
#             row, col = list(
#                 map(int, input("Enter row and column numbers to fix spot: ").split()))
#             print()
#
#             # fixing the spot
#             self.fix_spot(row - 1, col - 1, player)
#
#             # checking whether current player is won or not
#             if self.is_player_win(player):
#                 print(f"Player {player} wins the game!")
#                 break
#
#             # checking whether the game is draw or not
#             if self.is_board_filled():
#                 print("Match Draw!")
#                 break
#
#             # swapping the turn
#             player = self.swap_player_turn(player)
#
#         # showing the final view of board
#         print()
#         self.show_board()
#
#
# # starting the game
# tic_tac_toe = TicTacToe()
# tic_tac_toe.start()