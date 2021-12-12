from copy import deepcopy
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
import lib

###########################################
## part 1: power consumption

grid = lib.grid_load("input_sample.txt")
grid = lib.grid_load("input.txt")

grid_horizon = lib.grid_switch_row_and_column(grid) 
m = list(max(k,key=k.count) for k in grid_horizon) 
l = list(min(k,key=k.count) for k in grid_horizon)
m_s = list(map(str,m))
l_s = list(map(str,l))
print("part1:", int("".join(m_s),2) * int("".join(l_s),2))

###########################################
## part 2: life support rate

def shrink(grid, is_most):
    g = deepcopy(grid)
    index = 0
    while len(g) > 1:
        c = lib.grid_column(g, index)
        if is_most:
            b = 1 if sum(c) >= len(c)/2 else 0
        else:
            b = 0 if sum(c) >= len(c)/2 else 1
        g = list(filter(lambda l: l[index] == b, g))
        index += 1

    if len(g) == 0: return 0
    l_s = list(map(str,g[0]))
    return int("".join(l_s), 2)

print("part2: ", shrink(grid, True) * shrink(grid, False))
