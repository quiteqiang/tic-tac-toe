# Tic Tac Toe


import random


def drawBoard(board):
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
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
        return int(move)


def chooseRandomMoveFromList(board, movesList):
    # 随机返回一个可以落子的坐标
    # 如果没有所给的movesList中没有可以落子的，返回None
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # 确定电脑的落子位置
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'


    # Tic Tac Toe AI核心算法:
    # 首先判断电脑方能否通过一次落子直接获得游戏胜利
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i


    # 判断玩家下一次落子能否获得胜利，如果能，给它堵上
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i


    # 如果角上能落子的话，在角上落子
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move


    # 如果能在中心落子的话，在中心落子
    if isSpaceFree(board, 5):
        return 5


    # 在边上落子
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # 如果棋盘满了，返回True
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True




print('Welcome to Tic Tac Toe!')


while True:
    # 更新棋盘
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True


    while gameIsPlaying:
        if turn == 'player':
            #玩家回合
            drawBoard(theBoard)
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
            # 电脑回合
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
