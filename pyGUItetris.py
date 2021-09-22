## GUI TETRIS on PYTHON ##
## 20210630 ##


# board == playboard
# stack == block stack

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

curBlock = []

def init_board():
    global board
    board = [[0 for i in range(10)] for i in range(20)] ##comprehension -> for i in range(20): board.append(); for j in range(10): board[i].append();
    return

def init_stack():
    return

def print_board():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    return

def print_stack():
    return

def create_block():
    return

def turn_block():
    return

if __name__ == "__main__":
    init_board()
    print_board()
    