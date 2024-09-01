import random

board = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
draw, player1, player2, computer = 0, 0, 0, 0

def startboard(board):
    print('''
    {}|{}|{}    1 | 2 | 3
    -+-+-    --+---+---
    {}|{}|{}    4 | 5 | 6
    -+-+-    --+---+--
    {}|{}|{}    7 | 8 | 9
    '''.format(board['1'], board['2'], board['3'],
               board['4'], board['5'], board['6'],
               board['7'], board['8'], board['9']))

def printboard(board):
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print("-----")
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print("-----")
    print(board['7'] + "|" + board['8'] + "|" + board['9'])

def isWinner(board, let):
    if (board['1'] == let and board['2'] == let and board['3'] == let or
        board['4'] == let and board['5'] == let and board['6'] == let or
        board['7'] == let and board['8'] == let and board['9'] == let or
        board['1'] == let and board['5'] == let and board['9'] == let or
        board['7'] == let and board['5'] == let and board['3'] == let):   
        printboard(board)
        print("The player " + let + " won!!!")
        return True
    return False

def Computermove(board, let):
    available_moves = [k for k, v in board.items() if v == ' ']
    if available_moves:
        computer_move = random.choice(available_moves)
        board[computer_move] = let
        print("The computer has chosen the move: " + computer_move)

def computervs():
    global player1, computer  # Declare as global
    board = {str(i): ' ' for i in range(1, 10)}  # Reset the board

    print("Do you want to be X or O:")
    turn = input().upper()
    startboard(board)
    if turn == 'X':
        let = 'O'
    else:
        let = 'X'
    print("The computer took " + let)
    
    for i in range(9):
        printboard(board)

        if i % 2 == 0:
            current_turn = turn
        else:
            current_turn = let
        
        if current_turn == turn:
            print('Turn for ' + turn + '. Move on which space?')
            move = input()
            
            # Error checking for wrong move typed
            while move not in board or board[move] != ' ':
                print("Invalid or occupied space. Enter for " + turn + " again: ")
                move = input()
            board[move] = turn
        else:
            Computermove(board, let)

        # To check if there is a winner
        if isWinner(board, current_turn):
            if current_turn == 'X':
                computer += 1
            else:
                player1 += 1
            break        

        # Draw condition
        if i == 8: 
            print("The game is a draw.")
            printboard(board)
            draw += 1
            break

def playervs():
    global player1, player2  # Declare as global
    board = {str(i): ' ' for i in range(1, 10)}  # Reset the board

    print("Do you want to be X or O:")
    turn = input().upper()
    startboard(board)

    for i in range(9):
        printboard(board)

        if i % 2 == 0:
            current_turn = turn
        else:
            current_turn = 'O' if turn == 'X' else 'X'
        
        print('Turn for ' + current_turn + '. Move on which space?')
        move = input()
        
        # Error checking for wrong move typed
        while move not in board or board[move] != ' ':
            print("Invalid or occupied space. Enter for " + current_turn + " again: ")
            move = input()
        board[move] = current_turn

        # To check if there is a winner
        if isWinner(board, current_turn):
            if current_turn == 'X':
                player1 += 1
            else:
                player2 += 1
            break        

        # Draw condition
        if i == 8: 
            print("The game is a draw.")
            printboard(board)
            draw += 1
            break

def Scores():
    print("\nScores:")
    print(f"Player 1 score: {player1}")
    print(f"Player 2 score: {player2}")
    print(f"Computer score: {computer}")
    print(f"Total no. of draws: {draw}")

def Mainmenu():
    print("---------------------------------")
    print("Welcome to the Tic Tac Toe game.")
    print("---------------------------------")
    print("1. Player vs Player")
    print("2. Player vs Computer\n")
    print("Please select a choice: ")
    choice = int(input())
    
    while choice != 1 and choice != 2:
        print("Invalid choice. Please enter again: ")
        choice = int(input())

    if choice == 1:
        playervs()
    elif choice == 2:
        computervs()

    Scores()  # Show scores after each game

    print("Do you want to continue? (yes or no): ")
    replay = input().lower()
    while replay == 'yes' or replay == 'y':
        print("\n1. Player vs Player")
        print("2. Player vs Computer")
        print("3. Exit\n")
        print("Please select a choice: ")
        choice = int(input())
        
        while choice != 1 and choice != 2 and choice != 3:
            print("Invalid choice. Please enter again: ")
            choice = int(input())
        
        if choice == 1:
            playervs()
        elif choice == 2:
            computervs()
        elif choice == 3:
            break
        
        Scores()  # Show scores after each replay
        print("Do you want to continue? (yes or no): ")
        replay = input().lower()

    print("Thank you for playing!")

Mainmenu()
