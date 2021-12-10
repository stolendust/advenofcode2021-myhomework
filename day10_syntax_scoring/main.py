from pathlib import Path

###################
## part 1
NULL = 'n'
CHARS_L = {'[':']','{':'}','(':')','<':'>'} 
CHARS_R = {v: k for k, v in CHARS_L.items()}
POINTS_CORRUPTED = {')':3,']':57,'}':1197,'>':25137,'n':0}
POINTS_INCOMPELET= {')':1,']':2,'}':3,'>':4}

def first_corrupted(line):
    q = [] 
    for char in line:
        if char in CHARS_L: q.append(char) 
        if char not in CHARS_R: continue
        if q[-1] == CHARS_R[char]:
            q.pop()
        else:
            return char  # corrupted char found
    return NULL 

def main_part1(lines):
    points = 0 
    for line in lines:
        char = first_corrupted(line) 
        points += POINTS_CORRUPTED[char] 
    return points

#with open(Path(__file__).parent/"input_sample.txt", 'r') as file:
with open(Path(__file__).parent/"input.txt", 'r') as file:
    lines = file.read().splitlines()

points = main_part1(lines)
print("part1:", points)

################################3
## part 2
def incompelete_score(line):
    q = [] 
    for char in line:
        if char in CHARS_L: q.append(char) 
        if char not in CHARS_R: continue
        if q[-1] != CHARS_R[char]: return 0 # corrupted
        q.pop()

    score = 0
    right_char_list = list(map(lambda x: CHARS_L[x], q))
    right_char_list.reverse()
    for char in right_char_list:
        score = score * 5 + POINTS_INCOMPELET[char]  

    print("".join(q), "".join(right_char_list), score)
    return score

def main_part2(lines):
    score_list = [] 
    for line in lines:
        score = incompelete_score(line) 
        if score > 0: score_list.append(score)
    score_list.sort()
    print(score_list)
    return score_list[int(len(score_list) / 2)]

middle = main_part2(lines)
print("part2:", middle)
