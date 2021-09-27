## GUI TETRIS on PYTHON ##
## 20210630 ##


# board == playboard

from tkinter import *
import random as ran

board = []
blocks = [

        [[0,0,0],
         [1,1,1],
         [0,1,0]],

        [[0,1,1],
         [1,1,0],
         [0,0,0]],

        [[1,1,0],
         [0,1,1],
         [0,0,0]],

        [[0,0,1],
         [1,1,1],
         [0,0,0]],

        [[1,0,0],
         [1,1,1],
         [0,0,0]],

        [[0,1,0,0],
         [0,1,0,0],
         [0,1,0,0],
         [0,1,0,0]],

        [[1,1],
         [1,1]],
]

curBlock = []
x,y = 0,0

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

def set_curBlock():
    global curBlock
    curBlock = choice_block()
    return

def set_startpoint():   ##startpoint 설정. startpoint의 기준점은 block[0][0].
    global x,y
    x = int(len(board[0])/2)-int(len(curBlock[0])/2)
    y = 0
    return

def draw_block():       ## 리스트 값을 없애고 리스트 안에 집어넣는 형식
    return

def create_block():
    set_startpoint()
    return

def turn_block():
    return

##최종 실행 코드
def play():
    return


##main
if __name__ == "__main__":
    init_board()
    print_board()
    print("\n")
    set_curBlock()
    print("\n")
    print(curBlock)
    
