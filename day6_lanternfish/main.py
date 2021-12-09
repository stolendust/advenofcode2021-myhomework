import os
import sys

###########################################
## part 1

def evolve_one_day(school):
    school_tail = []
    i = 0
    while i < len(school):
        if school[i] == 0:
            school[i] = 6
            school_tail.append(8)
        else:
            school[i] -= 1
        i += 1

    school.extend(school_tail)        
    return school 

def evolve_days(school, days):
    new_school = school
    for i in range(days):
        new_school = evolve_one_day(new_school)
    return new_school 

## main
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "\input.txt", 'r')
school_str = file.readline().strip().split(',')
school_int = list(map(int, school_str)) #convert string to number
file.close()

days = 80
school_evolved = evolve_days(school_int, days)
print("evolved school after %d days: %d" % (days, len(school_evolved)))

###########################################
## part 2
init_timer_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

def daily_evolve(timer_dict):
    print(timer_dict)
    new_dict = init_timer_dict.copy()

    # timer subtracts 1 for fishes with timer larger than 0 
    for key in timer_dict:
        if key == 0: continue
        new_dict[key-1] = timer_dict[key] 

    new_dict[8] = timer_dict[0] # new children
    new_dict[6] += timer_dict[0] # reset timer
    return new_dict

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "\input.txt", 'r')
school_str = file.readline().strip().split(',')
school_int = list(map(int, school_str)) #convert string to number
file.close()

# format a data dict with count of fish for each timer
timer_dict = init_timer_dict.copy() 
for timer in school_int:
    timer_dict[timer] += 1

left_days = 256
for i in range(left_days):
    timer_dict = daily_evolve(timer_dict)

count = sum(timer_dict.values())
print("<< count of shool is %d after %d days" % (count, left_days))
