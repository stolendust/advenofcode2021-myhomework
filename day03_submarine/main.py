import os
from collections import Counter

###########################################
## part 1: power consumption

def power_consumption(file):
    line = file.readline().strip()
    result = [0] * len(line)
    line_count = 0 
    while len(line) > 0:
        index = 0
        for bit in line:
            if bit == "1": result[index] += 1       
            index += 1
        line_count += 1
        line = file.readline().strip()

    gamma = ""
    epsilon = ""
    for count in result:
        if count > line_count / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) *  int(epsilon, 2)

# change working path to the directory this file locates in
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

file = open("day3_input.txt", 'r')
ret = power_consumption(file)
file.close()
print("power consumption: %d" % ret)

###########################################
## part 2: life support rate

def the_common_bit(data_array, index, is_most): 
    count = 0
    for data in data_array:
        if data[index] == "1": count += 1       
    if is_most:
        return "1" if count >= len(data_array)/2 else "0"
    else:
        return "0" if count >= len(data_array)/2 else "1"

def search_data(data_array, index, is_most):
    if len(data_array) == 0 or index >= len(data_array[0]):
        print("DATA IS WRONG!!!")
        return

    bit = the_common_bit(data_array, index, is_most)
    filtered_data = []
    for data in data_array:
        if data[index] == bit:
            print("FOUND: " + filtered_data[0])
            filtered_data.append(data) 
    if len(filtered_data) == 1: 
        return filtered_data[0]
    return search_data(filtered_data, index + 1, is_most) 

file = open("input.txt", 'r')
lines = file.read().splitlines()
file.close()

#search for oxygen
oxygen_rate = search_data(lines, 0, True)
#search for co2 
co2_rate = search_data(lines, 0, False)
life_support_rate = int(oxygen_rate, 2) * int(co2_rate, 2)
print("life support rate: %d" % life_support_rate)
