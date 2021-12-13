from copy import deepcopy
from os.path import dirname, abspath
import sys,time
sys.path.append(dirname(dirname(abspath(__file__))))
import lib

####################################################
## v1 is too slow, about 290 seconds
## it's 8 seconds after optimization in this version
###################
## part 1
START = "start"
END = "end"

def steps_options(steps, node):
    return list(filter(lambda s: s[0] == node, steps))

def move(path_list, path, next, end_node=END):
    global steps_all
    if end_node in path or END in path: return None 
    if next == START : return path 
    if next.islower() and next in path: return path

    path.append(next)
    if next == end_node: 
        if not path in path_list: path_list.append(path)
        return None 

    options = steps_options(steps_all, next)
    for s in options:
        p = deepcopy(path)
        move(path_list, p , s[1], end_node)
    return None 

lines = lib.load_input("input_sample2.txt")
lines = lib.load_input("input.txt")

# load all steps
steps = [l.split("-") for l in lines]
f,t = zip(*steps)
steps_all = steps + [list(a) for a in zip(t,f)] # swap from to to and verse versa 

# find paths
path_list_part1 = []
for s in  steps_options(steps_all, START):
    p = move(path_list_part1, [START], s[1])

print("part 1:", len(path_list_part1))

#########################3
# part 2

# find all detours for each lower letter
detour_of_nodes = {}
set_lower_letters_of_nodes = {}

nodes_lower = list(set(lib.grid_column(steps_all, 0))) # unique values left
nodes_lower = list(filter(lambda n: n.islower() and n not in [START,END], nodes_lower)) 
for node in nodes_lower:
    detour_path = []
    for f,t in  steps_options(steps_all, node):
        p = move(detour_path, [], t, node)
    if not detour_path: continue

    for i in range(len(detour_path)):
        detour_path[i].pop() # delete node from the end of detour
    detour_of_nodes[node] = detour_path # all detour pathes for node

    # create set of lower letters for detours, for faster running later 
    for d in detour_path:
        key = ",".join(d)
        if key in set_lower_letters_of_nodes:continue
        set_lower_letters_of_nodes[key] = set(filter(lambda n: n.islower(), d))

# add up new pathes with valid detours 
t = time.time()
path_list_part2 = []
for p in path_list_part1:
    set_p = set(p)
    for node in p:
        if node.isupper() or node in [START,END]:continue
        if node not in detour_of_nodes: continue

        # find valid detours to be inserted into path
        for d in detour_of_nodes[node]:
            if set_lower_letters_of_nodes[",".join(d)] & set_p: continue
            pd = p.copy()
            index = p.index(node)
            pd[index:index] = [node] + d + [node]
            path_list_part2.append(pd)

print("part2v2:", len(path_list_part1) + len(path_list_part2), ", time:", round(time.time() - t),"s")
