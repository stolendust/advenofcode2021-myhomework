import os,sys
from itertools import *

############################3
# part 1

P_WITH_UNIQUE_LENGTH = {2:1,3:7,4:4,7:8}

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
#with open(os.path.join(sys.path[0], "input_sample.txt"), "r") as file:
    lines = file.read().splitlines()

count = 0
for l in lines:
    digits = l.split(" | ")[1].split()
    for d in digits:
        if len(d) in P_WITH_UNIQUE_LENGTH.keys(): count+= 1
print("part1:", count)

####################################
# part 2

# borrowed from hyper neutrino, much better than mine(see v1)
CODES_OLD = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
LETTERS = "abcdefg"

t = 0
for k in lines:
    a, b = k.split(" | ")
    req = set(CODES_OLD)
    for x in permutations("abcdefg"):
        # mapping for all 7 letter from one to another
        m = {i: j for i, j in zip(x, LETTERS)}

        # decode all new patterns with mapping 
        patterns_new = a.split()
        r = {"".join(sorted(map(m.get, q))) for q in patterns_new}
        if r != req: continue

        # bingo
        b = ["".join(sorted(map(m.get, q))) for q in b.split()]
        b = "".join(str(CODES_OLD.index(q)) for q in b)
        t += int(b)

print("part2:", t)