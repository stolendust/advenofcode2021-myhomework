from copy import deepcopy
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
import lib

###################
## part 1
MAX = 9

def dots_xy_filtered(grid, lambda_filter):
    dots_xy = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if lambda_filter(grid[x][y]): dots_xy.append((x,y))
    return dots_xy

def adjacent_dots_xy(xy, max_x, max_y):
    x, y = xy[0], xy[1]
    xy_all = [(x-1,y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y),(x+1,y+1)]
    ret = list(filter(lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] <= max_x and xy[1] <= max_y, xy_all))
    return ret

def dot_flash(grid, dots_xy_flash, flashing_xy):
    dots_xy = adjacent_dots_xy(flashing_xy, len(grid)-1, len(grid[0])-1)
    for xy in dots_xy:
        grid[xy[0]][xy[1]] += 1
        if grid[xy[0]][xy[1]] <= MAX or xy in dots_xy_flash: continue
        dots_xy_flash.append(xy)
        grid, dots_xy_flash = dot_flash(grid, dots_xy_flash, xy)
    return grid, dots_xy_flash

def one_step(grid):
    # all dots increase 1
    grid_ret = [list(map(lambda x: x+1, x)) for x in grid]

    # find the flashing dots
    dots_xy_flash = dots_xy_filtered(grid_ret, lambda x: x > MAX)
    if len(dots_xy_flash) == 0: return 0, grid_ret

    # do flash
    dots_xy_flash_all = deepcopy(dots_xy_flash)
    for xy in dots_xy_flash:
        grid_ret, dots_xy_flash_all = dot_flash(grid_ret, dots_xy_flash_all, xy)

    # set flashed dots to 0
    grid_reset = [list(map(lambda x: x if x <= 9 else 0, x)) for x in grid_ret]
    return len(dots_xy_flash_all), grid_reset

def main_part1(grid, steps):
    count = 0
    for i in range(steps):
        count_step,grid = one_step(grid)
        count += count_step
    return count

grid = lib.grid_load("input_sample.txt")
grid = lib.grid_load("input.txt")
count = main_part1(grid, 100)
print("part1:", count)

##############################
## part 2

def main_part2(grid, steps):
    for i in range(steps):
        count_step,grid = one_step(grid)
        if 0 == lib.grid_sum(grid): return i + 1
    return 0 

step = main_part2(grid, 1000000000)
print("part1:", step)

    
