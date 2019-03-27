#! /usr/bin/python3

import random
import copy

def isFree(board_spot):
    return board_spot == ' '

def possibleMoves(board, moves_left):
    movesAvailable = []
    for spot in moves_left:
        if isFree(board[spot]):
            copy.deepcopy(board,)
            possibleMoves(board, )
            # movesAvailable.append(spot)
    if movesAvailable == []:
        return movesAvailable

def main():
    seq = {}
    board = [' ']*10
    moves = possibleMoves(board, range(1,10))
    print(moves)
        

if __name__ == '__main__':
    main()