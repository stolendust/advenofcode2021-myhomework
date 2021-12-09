import os
import sys

################################
# part 1

def calc_fuel_part1(pos_dict, the_pos):
    fuel = 0
    for pos in pos_dict:
        fuel +=  pos_dict[pos] * abs(pos - the_pos)
    return fuel

def calc_fuel_part2(pos_dict, the_pos):
    fuel = 0
    for pos in pos_dict:
        steps = sum(range(1, abs(pos - the_pos) + 1))
        fuel +=  pos_dict[pos] * steps 
    return fuel

# read data
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "\input.txt", 'r')
pos_str = file.readline().strip().split(',')
pos_int = list(map(int, pos_str))
pos_int.sort()
file.close()

# format data to a position dict
pos_dict = {}
for pos in pos_int: 
    pos_dict[pos] = pos_dict[pos] + 1 if pos in pos_dict else 1

fuel_dict_part1 = {}
fuel_dict_part2 = {} 
pos_min = min(pos_dict.keys())
pos_max = max(pos_dict.keys())
for the_pos in range(pos_min, pos_max):
    fuel_dict_part1[the_pos] = calc_fuel_part1(pos_dict, the_pos)
    fuel_dict_part2[the_pos] = calc_fuel_part2(pos_dict, the_pos)

print("min fuel part1 = %d" % min(list(fuel_dict_part1.values())))
print("min fuel part2 = %d" % min(list(fuel_dict_part2.values())))


