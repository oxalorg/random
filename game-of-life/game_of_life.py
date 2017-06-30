"""
Conways game of life
====================

Author: @oxalorg
"""
import time
import copy
import os

os.system('clear')

DEAD = '  '
ALIVE = '-*'


def get_board(n=32):
    board = [[DEAD for _ in range(n)] for _ in range(n)]
    return board


def dead(nebs):
    if nebs.count(ALIVE) == 3:
        return ALIVE
    return DEAD


def alive(nebs):
    alive_count = nebs.count(ALIVE)
    if 2 <= alive_count <= 3:
        return ALIVE
    return DEAD


def get_nebs(x, y, board):
    xmov = [-1, 0, 1]
    ymov = [-1, 0, 1]
    nebs = []
    N = len(board[0])
    for i in xmov:
        for j in ymov:
            if i == 0 and j == 0:
                continue
            nebs.append(board[(x+i)%N][(y+j)%N])
    return nebs


def game(board, n=32):
    while True:
        os.system('clear')
        for row in board:
            print('| ', ''.join(row), ' |')

        new_board = get_board(n)
        for i, x in enumerate(board):
            for j, y in enumerate(board[i]):
                cell = board[i][j]
                nebs = get_nebs(i, j, board)

                if cell == DEAD:
                    new_board[i][j] = dead(nebs)
                else:
                    new_board[i][j] = alive(nebs)

        time.sleep(0.1)
        board = new_board


def create_drops(i, j, board):
    a = 0
    b = 1
    c = 2
    d = 3
    board[a+j][a+i] = ALIVE
    board[b+j][a+i] = ALIVE
    board[c+j][a+i] = ALIVE
    board[c+j][b+i] = ALIVE
    board[a+j][b+i] = ALIVE
    board[b+j][b+i] = ALIVE
    board[b+j][c+i] = ALIVE
    board[d+j][c+i] = ALIVE


def create_random(a, b, board):
    pulsar = [
        (a+1, b), (a+2, b), (a+3, b),
        (a, b+1), (a+5, b+1),
        (a, b+2), (a+5, b+2),
        (a, b+3), (a+5, b+3),
        (a+1, b+5), (a+2, b+5), (a+3, b+5)
    ]

    for a, b in pulsar:
        board[b][a] = ALIVE


def init_state(board):
    # set init board config
    N = len(board[0])
    drops = [(0, 0), (0, -9), (10, -14), (18, -3), (28,-21),(23,-12)]
    for drop in drops:
        create_drops(*drop, board)
    create_random(N-10, N-10, board)
    create_random(N-16, N-16, board)
    create_random(6, 6, board)
    # create_random(N-6, 6, board)
    # create_random(10, 20, board)


def main():
    n = 32
    board = get_board(n)
    init_state(board)
    game(board, n)


if __name__ == '__main__':
    main()
