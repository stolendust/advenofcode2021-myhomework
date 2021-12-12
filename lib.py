import os,sys,copy

def grid_print(data_grid):
    print(" ")
    for l in data_grid:
        list(map(lambda x: print("%4s" % x, end=""), l))
        print("")

def grid_load(file_name):
    with open(os.path.join(sys.path[0], file_name), "r") as file:
        lines = file.read().splitlines()
    return [list(map(int,l)) for l in lines]

def grid_column(grid, i_col):
    return [row[i_col] for row in grid]

def grid_switch_row_and_column(grid):
    return list(zip(*grid))

def grid_sum(grid):
    return sum([sum(l) for l in grid])