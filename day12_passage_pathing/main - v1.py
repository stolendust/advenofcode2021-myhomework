from copy import deepcopy
from os.path import dirname, abspath
import sys,time
sys.path.append(dirname(dirname(abspath(__file__))))
import lib

###################
## part 1
START = "start"
END = "end"

def steps_next(steps, node):
    return list(filter(lambda s: s[0] == node, steps))

def move_part1(steps_list, path_list, path, next):
    if END in path: return None 
    if next == START : return path 
    if next.islower() and next in path: return path

    path.append(next)
    if next == END: 
        if not path in path_list: path_list.append(path)
        return None 

    options = steps_next(steps_list, next)
    for s in options:
        p = deepcopy(path)
        move_part1(steps_list,path_list, p , s[1])
    return None 

lines = lib.load_input("input.txt")
lines = lib.load_input("input_sample2.txt")

# load all steps
steps = [l.split("-") for l in lines]
f,t = zip(*steps)
steps_list = steps + list(zip(t,f)) # [from, to] + [to,from]

# find paths
path_list = []
for s in  steps_next(steps_list, START):
    p = move_part1(steps_list,path_list, [START], s[1])

print("part 1:", len(path_list))

#########################3
# part 2
def move_part2(steps_list, path_list, path, next, is_twiced):
    t = is_twiced
    if END in path: return None 
    if next == START : return path 
    if next.islower() and next in path:
        if t: return path
        t = True 

    path.append(next)
    if next == END: 
        if not path in path_list: 
            path_list.append(path)
        return None 

    options = steps_next(steps_list, next)
    for s in options:
        p = deepcopy(path)
        move_part2(steps_list,path_list, p , s[1],t)
    return None 

# find paths
t = time.time()
path_list = []
for s in  steps_next(steps_list, START):
    p = move_part2(steps_list,path_list, [START], s[1], False)
print("part 2:", len(path_list), ", time:", round(time.time() - t),"s")

