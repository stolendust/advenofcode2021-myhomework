from copy import deepcopy
from os import pardir
from os.path import dirname, abspath
import sys
sys.path.append(dirname(dirname(abspath(__file__))))
import lib
from collections import Counter

###################
## part 1

lines = lib.load_input("input_sample.txt")
lines = lib.load_input("input.txt")

def step(template, pairs):
    r = [] 
    m = []
    t = template.copy()
    c = t.pop(0)
    r.append(c)
    m.append(" ")
    while t:
        n = t.pop(0)
        key = c+n
        if key in pairs:
            r.append(pairs[key])
            m.append("*")
        r.append(n)
        m.append(" ")
        c = n
    return r 

pairs = {} 
for i in range(2, len(lines)):
    k,v = lines[i].split(" -> ") 
    pairs[k] = v
print(pairs)

steps = 25 
t = list(lines[0])
print("".join(t))
for i in range(steps):
    t = step(t, pairs)
    c = Counter(t).most_common()
    print("%2d"%i, len(t))
    most,least = c[0][1],c[-1][1]
    print("%s-%s = %d-%d = " % (c[0][0],c[-1][0],most,least),most-least)
    print("%.4f" % (most/len(t)), "%.4f" % (least/len(t)))
