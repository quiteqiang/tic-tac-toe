# Tic Tac Toe


import random


def drawBoard(board=['0','1','2','3','4','5','6','7','8','9']):
    print('\n\n\n\n')
    print('\t\t\t┌─┬─┬─┐')
    print('\t\t\t│'+board[7]+'│'+board[8]+'│'+board[9]+'│')
    print('\t\t\t├─┼─┼─┤')
    print('\t\t\t│'+board[4]+'│'+board[5]+'│'+board[6]+'│')
    print('\t\t\t├─┼─┼─┤')
    print('\t\t\t│'+board[1]+'│'+board[2]+'│'+board[3]+'│')
    print('\t\t\t└─┴─┴─┘')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():# or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
        if board[int(move)] != ' ':
            print ('The spot was token')
            return getPlayerMove(board)
        return int(move)


def chooseRandomMoveFromList(board, movesList):
    # random return a location to put 
    # if movesList has no place to put，return None
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # check the computer's input pocation
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    # Tic Tac Toe AI algorithm:
    # check if the Ai can win the game within one step
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i


    # check if the player can win with one more step, stop him
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i


    # in the corner
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move


    # in the center
    if isSpaceFree(board, 5):
        return 5


    # on the endge
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # if board full，return True
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def whoStart():
    print('Who do you want go first? ([C]omputer/[P]layer)')
    start = input().upper()
    print(start)
    while start != 'C' and start !='P':
        print('Invalid input try again')
        whoStart()
    if start == 'C':
        start = 'computer'
    if start =='P':
        start = 'player'
    return start
    
def validInput(board, move):
    if board[move] == 'X' or board[move] == 'O':
        canPut = False
    else:
        return True
    while canPut == False:
        print ('The spot was token')
        getPlayerMove(board)
        validInput(board, letter, move)

        
    
print('Welcome to Tic Tac Toe!')


while True:
    # renew the playboard 
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    drawBoard()
    turn = whoStart()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True


    while gameIsPlaying:
        if turn == 'player':
            #Player turn
            drawBoard(theBoard)  #check the position before draw the board
            print ('length of theBoard' +str(len (theBoard)))
            for i in range(len (theBoard)):
                print ("theBoard------>"+theBoard[i])
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)


            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'


        else:
            # computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)


            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'


    if not playAgain():
        break
