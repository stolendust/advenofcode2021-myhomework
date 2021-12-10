from pathlib import Path
from operator import sub, mul
from copy import deepcopy
import sys

###################
## part 1
MAX_HEIGHT = 9
def print_map(data_map):
    for l in data_map:
        list(map(lambda x: print(x, end=""), l))
        print("")

# base line sub next line, mark the bigger location as False 
def compare_lines(line, line_next):
    diff = list(map(sub, line, line_next))
    return list(map(lambda x: 1 if x < 0 else 0, diff))  # if bigger or equal, it's 0 

def compare_in_line(line, screen):
    # insert and append a dummy item before and after the data, making the comparision smooth
    # find the bigger location in line and mark it as False
    line_temp = [MAX_HEIGHT] + line.copy() + [MAX_HEIGHT]
    for j in range(1, len(line_temp)-1):
        if line_temp[j] >= line_temp[j-1] or line_temp[j] >= line_temp[j+1]:
            screen[j-1] = 0 
    return screen

def main_part1(heightmap):
    screen_map= [] 
    # insert and append a dummy line before and after the data, making the comparision smooth
    line_dummp = [MAX_HEIGHT] * len(heightmap[0]) 
    tempmap = heightmap.copy() 
    tempmap.insert(0, line_dummp)
    tempmap.append(line_dummp)
    count = risk = 0

    for i in range(1, len(tempmap) -1):
        # campare to previous and next line
        screen_prev = compare_lines(tempmap[i], tempmap[i-1])
        screen_next = compare_lines(tempmap[i], tempmap[i+1])
        screen = list(map(lambda x,y: x & y, screen_prev, screen_next))

        screen = compare_in_line(tempmap[i],screen)
        screen_map.append(screen)
        count += screen.count(1)
        risk += sum(list(map(mul, screen, tempmap[i]))) + screen.count(1)

    return count, risk, screen_map

#with open(Path(__file__).parent/"input_sample.txt", 'r') as file:
with open(Path(__file__).parent/"input.txt", 'r') as file:
    lines = file.read().splitlines()

heightmap = [] 
for l in lines:
    heightmap.append( [int(i) for i in list(l)] )

print_map(heightmap)
count,risk, screen_map = main_part1(heightmap)
print("part 1: count=%d, risk=%d\n" % (count, risk))
print_map(screen_map)

#####################################3
## part 2
IS_CRAWLED = 2 
def crawl_about(count,map_basin,row,col):
    global heightmap
    # stop if point is on the edge
    if row < 0 or col < 0: return count 
    if row >= (len(heightmap)): return count 
    if col >= (len(heightmap[0])): return count 
    # stop if point's height is MAX_HEIGHT
    if heightmap[row][col] >= MAX_HEIGHT: return count
    if map_basin[row][col] == IS_CRAWLED: return count 

    # mark and count
    count += 1
    map_basin[row][col] = IS_CRAWLED 

    # scrawl to next
    count = crawl_about(count, map_basin, row, col-1) #left
    count = crawl_about(count, map_basin, row, col+1) #right
    count = crawl_about(count, map_basin, row-1, col) #up
    count = crawl_about(count, map_basin, row+1, col) #down
    return count 

def main_part2(screen_map):
    global heightmap
    map_basin = deepcopy(screen_map)
    sizes = []
    for row in range(len(screen_map)):
        for col in range(len(screen_map[row])):
            if screen_map[row][col] == 0: continue
            # find the lowest point and crawl about it
            count = crawl_about(0, map_basin, row, col) 
            sizes.append(count)
            print("[%d,%d]=%d, size=%d" % (row, col, heightmap[row][col], count))

    sizes_sorted = list(sorted(sizes, reverse=True))
    return map_basin, sizes_sorted[0] * sizes_sorted[1] * sizes_sorted[2]

map_basin, result = main_part2(screen_map)
print_map(map_basin)
print("part 2: ", result)