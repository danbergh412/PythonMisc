from copy import copy, deepcopy


board = [
    ['o', 'x', 'o'], 
    ['x', 'x', 'o'], 
    ['x', 'o', '-']
]

turn = 'x'
winner = '-'

def getWinner(board):
    for i in range(3):
        tmpWin = board[i][0]
        for j in range(3):
            if board[i][j] != tmpWin:
                tmpWin = '-'
        if tmpWin != '-':
            return tmpWin
    
    for i in range(3):
        tmpWin = board[0][i]
        for j in range(3):
            if board[j][i] != tmpWin:
                tmpWin = '-'
        if tmpWin != '-':
            return tmpWin
    
    rightWin = board[0][0]
    leftWin = board[2][0]
    for i in range(2):
        if (board[i + 1][i + 1] != rightWin):
            rightWin = '-'
        if (board[2 - i - 1][i + 1] != leftWin):
            leftWin = '-'
    
    if rightWin != '-':
        return rightWin
    elif leftWin != '-':
        return leftWin
    else:
        return '-'
        
def printBoard(board):
    print ("  a b c")
    for i in range(3):
        line = str(i + 1) + " "
        for j in range(3):
            line += board[i][j] + " "
        print(line)

def isTie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True

def updateBoard(board):
    location = input(turn.upper() + " turn. Please enter a location to add (e.g. a1):")
    
    i = int(location[1]) - 1

    if location[0].lower() == 'a':
        j = 0
    elif location[0].lower() == 'b':
        j = 1
    elif location[0].lower() == 'c':
        j = 2
    
    if (board[i][j] != '-'):
        print("That cell is already used.")
        updateBoard(board)
    else:
        board[i][j] = turn

def switchTurn(turn):
    if turn == 'x':
        return 'o'
    elif turn == 'o':
        return 'x'

while True:
    printBoard(board)

    updateBoard(board)

    if getWinner(board) != '-':
        printBoard(board)
        print(turn.upper() + " won!")
        break
    elif isTie(board):
        printBoard(board)
        print("Its a tie!")
        break
    else:
        turn = switchTurn(turn)