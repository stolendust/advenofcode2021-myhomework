from pathlib import Path
from copy import deepcopy

###################
## part 1

#with open(Path(__file__).parent/"input_sample.txt", 'r') as file:
with open(Path(__file__).parent/"input.txt", 'r') as file:
    lines = file.read().splitlines()

depth_list = list(map(int, lines))

def main_part1(data_list):
    temp_list = deepcopy(data_list)
    depth_prev = temp_list.pop(0)
    count = 0
    while temp_list:
        depth_current = temp_list.pop(0)
        if depth_current > depth_prev: count += 1
        depth_prev = depth_current
    return count

print("part1:", main_part1(depth_list))

####################
# part 2
sum_list = []
sum_prev = 0
for i in range(len(depth_list) - 2):
    sum_list.append(sum(depth_list[i:i+3]))

print("part2:", main_part1(sum_list))




