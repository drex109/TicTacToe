# returns basic 3x3 board
def newBoard():
    return [[0]*3 for i in range(0, 3)]

# figure out if the game is over by win or draw
def checkBoard(board):
    # check for horizontal win
    for row in board:
        if row == [1, 1, 1]:
            return quit(print('player 1 wins!'))
        if row == [2, 2, 2]:
            return quit(print('player 2 wins!'))
    
    # check vertical win
    if board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        return quit(print('player 1 wins!'))
    if board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return quit(print('player 1 wins!'))
    if board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        return quit(print('player 1 wins!'))
    
    if board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        return quit(print('player 2 wins!'))
    if board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return quit(print('player 2 wins!'))
    if board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        return quit(print('player 2 wins!'))
    
    # check diagnoal win
    if board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return quit(print('player 1 wins!'))
    if board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return quit(print('player 1 wins!'))

    if board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return quit(print('player 2 wins!'))
    if board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return quit(print('player 2 wins!'))

    # check for full board draw.
    boardFill = 0
    for x in range(0, len(board[0])):
        for y in range(0, len(board)):
            currentPos = board[x][y]
            if boardFill < 9 and currentPos != 0:
                boardFill += 1
            if boardFill == 9:
                return quit(print('draw!'))  

#visualize the board in the console
def boardRender(board):
    #print(board)
    boardRender = newBoard()
    # check for symbols
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            currentPos = board[x][y]
            if currentPos == 1:
                boardRender[x][y] = 'X'
            elif currentPos == 2:
                boardRender[x][y] = 'O'
            else:
                boardRender[x][y] = ' '
    #print(boardRender)

    # construct board with above data
    rows = []
    lines = '-'*5
    for row in boardRender:
        row = row[0] + '|' + row[1] + '|' + row[2]
        rows.append(row)
    #print(rows)
    boardRender = '\n' + str(rows[0]) + '\n' + lines + '\n' + str(rows[1]) + '\n' + lines + '\n' + str(rows[2]) + '\n'
    return print(boardRender)

# receive input from the player
def playerMove1(board):
    # show board layout with selection numbers
    selectionBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('\n'+'1|2|3'+'\n'+'-----'+'\n'+'4|5|6'+'\n'+'-----'+'\n'+'7|8|9'+'\n')
    playerInput1 = input('Player 1, please selct a postiion on the board: ')
    # compare player input to selection board and change the board accordingly
    for x in range(0, 3):
        for y in range(0, 3):
            currentPos = selectionBoard[x][y]
            if currentPos == int(playerInput1):
                if board[x][y] == 0:
                    board[x][y] = 1
                else:
                    return print('Error: position already taken')

def playerMove2(board):
    # show board layout with selection numbers
    selectionBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('\n'+'1|2|3'+'\n'+'-----'+'\n'+'4|5|6'+'\n'+'-----'+'\n'+'7|8|9'+'\n')
    playerInput2 = input('Player 2, please selct a postiion on the board: ')
    # compare player input to selection board and change the board accordingly
    for x in range(0, 3):
        for y in range(0, 3):
            currentPos = selectionBoard[x][y]
            if currentPos == int(playerInput2):
                if board[x][y] == 0:
                    board[x][y] = 2
                else:
                    return print('Error: position already taken')
    return board

def runGame():
    board = newBoard()
    running = True
    while running:
        boardRender(board)
        playerMove1(board)
        checkBoard(board)
        boardRender(board)
        playerMove2(board)
        checkBoard(board)
runGame()