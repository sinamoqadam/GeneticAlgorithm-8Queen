import numpy as np

#print checss board with queens as 'O' and empty positions as '-'
def printBoard(formation):
    board = []
    for row in range(0, 8):
        array = []
        for column in range(0, 8):
            if row == formation[column]:
                array.append('O')
            else:
                array.append('-')
        board.append(array)

    print("board with current formation is:")
    print(np.matrix(board))