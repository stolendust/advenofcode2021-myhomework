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
## failed: time consuming

K_TIMER = "t"
K_LEFT_DAYS = "d"

def one_fish_generate_children(timer, left_days):
    children = [] 
    count = 0
    for i in range(0, left_days - timer, 7):
        count += 1
        # generate a new child with timer and left days
        children.append({K_TIMER:8, K_LEFT_DAYS:left_days - i -1}) 
    return children

def school_list_evolve(init_count, school_list):
    if len(school_list) < 1: return 0

    count = init_count + len(school_list) 
    for item in school_list:
        children = one_fish_generate_children(item[K_TIMER], item[K_LEFT_DAYS])
        new_count = school_list_evolve(0, children)
        count += new_count
        #print(new_count, end=",")

    return count

# read data 
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "\input.txt", 'r')
school_str = file.readline().strip().split(',')
file.close()

# format data into list of fishes with properties of timer and left_days
left_days = int(sys.argv[1])
school_list = [] 
for item in school_str:
    school_list.append({K_TIMER:int(item), K_LEFT_DAYS:left_days})

school_test = [school_list[0]]
count = school_list_evolve(0, school_test)
print("<< count of shool is %d after %d days" % (count, left_days))
