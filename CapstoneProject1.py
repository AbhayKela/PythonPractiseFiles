import os
import random


def clear1():  # Function to clear the screen
    os.system('clear')


def display_board(board):   # Function to display the board
    clear1()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():  # Function asking for player input
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input("Player1: Do you want to be 'X' or 'O'\n").upper()
        print('\n')
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def place_marker(board, marker, position):   # Function to position mark on the board
    board[position] = marker


def win_check(board, mark):  # Function to check if any player won
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or   # Top row
            (board[4] == mark and board[5] == mark and board[6] == mark) or   # Middle row
            (board[1] == mark and board[2] == mark and board[3] == mark) or   # Bottom row
            (board[7] == mark and board[5] == mark and board[3] == mark) or   # Diagonal1
            (board[1] == mark and board[5] == mark and board[9] == mark) or   # Diagonal2
            (board[7] == mark and board[4] == mark and board[1] == mark) or   # Left column
            (board[8] == mark and board[5] == mark and board[2] == mark) or   # Middle column
            (board[9] == mark and board[6] == mark and board[3] == mark))     # Right column


def choose_first():   # Function random selecting player for starting game
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):   # Check if there is any space on board
    for i in range(1, 10):
        if space_check(board, i):
            return False    # Not using else statement as checking space in the range 1 to 10.
    return True


def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9)')
    return int(position)


def replay():
    return input('Do you want to play again? Enter Yes or No').lower().startswith('y')


print ('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10   # Reset the board
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + ' will go first')
    game_on = True

    while game_on:

        if turn == 'Player 1':  # Player 1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulation Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:   # Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulation Player 2! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break