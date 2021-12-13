from copy import deepcopy
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
import lib

###################
## part 1

def print_paper(xys):
    max_x,max_y = max(lib.grid_column(xys,0)) + 1, max(lib.grid_column(xys,1)) + 1 
    grid = [[0 for x in range(max_x)] for y in range(max_y)] # creat two dimention array 
    for xy in xys:
        grid[xy[1]][xy[0]] = 1
    return lib.grid_print(grid)

def fold(xys, fold):
    ret, f = [], fold[1]
    if fold[0] == 'x':
        for xy in xys:
            x,y = xy[0],xy[1]
            if x == f: continue 
            if x > f: x = (f+1) - (x-f) - 1
            if x > -1 and [x,y] not in ret : ret.append([x,y])
    elif fold[0] == 'y':
        for xy in xys:
            x,y = xy[0],xy[1]
            if y == f: continue 
            if y > f: y = (f+1) - (y-f) - 1
            if y > -1  and [x,y] not in ret: ret.append([x,y])
    return ret

lines = lib.load_input("input.txt")
lines = lib.load_input("input_sample.txt")

# load data
xys, folds = [], []
for l in lines:
    if l.find("fold") > -1:
        xy = (l.replace("fold along ","")).split("=")
        xy[1] = int(xy[1])
        folds.append(xy)
    elif len(l) > 0:
        xys.append(list(map(int,l.split(","))))

new_xys = deepcopy(xys)
new_xys = fold(new_xys, folds[0])
print_paper(new_xys)
print("part1:", len(new_xys))

#####################
## part 2

def find_letter(xys, letters):
    print(xys)
    x_l = []
    x_list = sorted(lib.grid_column(0))
    x = x_list[0]
    for i in range(len(x_list)):
        if x_list[i] > x+1: break
        x = x_list[i]

new_xys = deepcopy(xys)
for f in folds:
    new_xys = fold(new_xys, folds[0])

letters = []
find_letter(xys, letters)
