## GUI TETRIS on PYTHON ##
## 20210630 ##


# board == playboard
# stack == block stack

from tkinter import * ## tkinter 기반 gui 구현.
import random as ran
import time

board = []
blocks = [

        [[1,1,1],
         [0,1,0]],

        [[0,1,1],
         [1,1,0]],

        [[1,1,0],
         [0,1,1]],

        [[0,0,1],
         [1,1,1]],

        [[1,1,1,1]],

        [[1,1],
         [1,1]],

]

stack = []
curBlock = []

def init_board():
    global board
    board = [[0 for i in range(10)] for i in range(20)] ##comprehension -> for i in range(20): board.append(); for j in range(10): board[i].append();
    return

##편의상 작성한 코드
def print_board():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    return

def choice_block():
    i = ran.randrange(6)
    return blocks[i]

def init_stack():
    global stack
    for n in range(3):  ##stack size == 3
        stack.append(choice_block())
    return

##편의상 작성한 코드
def print_stack():
    for i in stack:
        print(i, end=" ")
    return

def set_curBlock():
    global stack
    global curBlock
    curBlock = stack[0]
    for n in range(1,3):
        stack[n-1] = stack[n]
    
    stack[2] = choice_block()
    return

def stackIsFull():  ##stack이 차있는가?
    return

def create_block():
    return

def turn_block():
    return

##최종 실행 코드
def play():
    return


##main
if __name__ == "__main__":
    init_board()
    init_stack()
    print_board()
    print("\n")
    print_stack()
    set_curBlock()
    print("\n")
    print(curBlock)
    print_stack()
    

    # how to make timer?
    # 일단 구현하고 나중에 객체지향 시스템으로 바꾼다.
