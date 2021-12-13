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

lines = lib.load_input("input_sample.txt")
lines = lib.load_input("input.txt")

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
print("part1:", len(new_xys))

#####################
## part 2

def adjacent_xys(xy, max_x, max_y):
    x, y = xy[0], xy[1]
    xy_all = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y),(x+1,y+1)]
    ret = list(filter(lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] <= max_x and xy[1] <= max_y, xy_all))
    return ret

def print_letter(xys):
    max_x,max_y = max(lib.grid_column(xys,0)) + 1, max(lib.grid_column(xys,1)) + 1 
    grid = [[0 for x in range(max_x)] for y in range(max_y)] # creat two dimention array 
    for xy in xys:
        grid[xy[1]][xy[0]] = " #" 

    for l in grid:
        list(map(lambda x: print(x, end="") if x  else print("  ", end=""), l))
        print("")

folded_xys = deepcopy(xys)
for f in folds:
    folded_xys = fold(folded_xys, f)

print_letter(folded_xys)