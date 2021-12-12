from pathlib import Path
from operator import sub, mul
from copy import deepcopy
from sys import call_tracing

###################
## part 1
BOARD_SIZE = 5
MARKED = -1 

def print_board(board):
    for l in board:
        list(map(lambda x: print("%2d" % x, end=" "), l))
        print(" ")

def mark_board(board, number):
    for i in range(len(board)):
        board[i] = list(map(lambda x: MARKED if x == number else x, board[i]))
    
def is_bingo(board):
    # check row
    for row in board:
        if sum(row) == len(row) * MARKED: return True 
    # check column
    for c in range(BOARD_SIZE):
        column = [board[i][c] for i in range(BOARD_SIZE)]
        if sum(column) == BOARD_SIZE * MARKED: return True 
    return False

def sum_unmarked(board):
    board_sum = 0
    for line in board:
        line = list(map(lambda x: 0 if x==MARKED else x, line)) # set 0 on marked postions
        board_sum += sum(line)
    return board_sum

def main_part1(number_list, board_list):
    screen_list = deepcopy(board_list)
    called_number = None 
    for number in number_list:
        for board in screen_list:
            mark_board(board, number)
            if not is_bingo(board): continue

            called_number = number
            board_sum = sum_unmarked(board)
            return called_number, board_sum

#with open(Path(__file__).parent/"input.txt", 'r') as file:
with open(Path(__file__).parent/"input_sample.txt", 'r') as file:
    lines = file.read().splitlines()

#load data
number_list = list(map(int,lines[0].strip().split(",")))
board_list = []
for i in range(2, len(lines), BOARD_SIZE+1):
    board = []
    for j in range(BOARD_SIZE):
        line = list(map(int, lines[i+j].strip().replace("  "," ").split(" ")))
        board.append(line)
    board_list.append(board) 

print(number_list)
for i in range(len(board_list)):
    print(">> board:", i)
    print_board(board_list[i])

called_number, board_sum = main_part1(number_list, board_list)
print("part1: %d*%d=%d\n" % (called_number,board_sum, called_number*board_sum))

######################
## part 2

def main_part1(number_list, board_list):
    screen_list = deepcopy(board_list)
    won_board_dict = {}
    for number in number_list:
        for i_board in range(len(screen_list)):
            board = screen_list[i_board]
            mark_board(board, number)

            if not is_bingo(board): continue
            if i_board in won_board_dict: continue

            won_board_dict[i_board] = sum_unmarked(board)
            print("> bingo board:%2d, number=%2d, sum=%d" % (i_board,number,won_board_dict[i_board]))
            if len(won_board_dict) == len(board_list): return number, won_board_dict[i_board]

called_number, board_sum = main_part1(number_list, board_list)
print("part2: %d*%d=%d" % (called_number,board_sum, called_number*board_sum))