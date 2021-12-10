from pathlib import Path

###################
## part 1
K_CMD = "cmd"
K_VAL = "val"
CMD_DEPTH = {"up":-1, "down":1}
CMD_HORIZON = {"forward":1}

#with open(Path(__file__).parent/"input_sample.txt", 'r') as file:
with open(Path(__file__).parent/"input.txt", 'r') as file:
    lines = file.read().splitlines()

cmd_list = []
for l in lines:
    two_parts = l.split(" ")
    cmd_list.append({K_CMD:two_parts[0], K_VAL:int(two_parts[1])})

horizontal = depth = 0
for c in cmd_list:
    if c[K_CMD] in CMD_DEPTH: depth += c[K_VAL] * CMD_DEPTH[c[K_CMD]]
    if c[K_CMD] in CMD_HORIZON: horizontal += c[K_VAL] * CMD_HORIZON[c[K_CMD]]

print("part1:", horizontal*depth)

###############################
## part 2

CMD_AIM = {"up":-1, "down":1}
CMD_HORIZON = {"forward":1}
CMD_DEPTH = {"forward": (lambda aim, x: aim*x)}

horizontal = depth = aim = 0
for c in cmd_list:
    if c[K_CMD] in CMD_AIM : aim += c[K_VAL] * CMD_AIM[c[K_CMD]]
    if c[K_CMD] in CMD_HORIZON: horizontal += c[K_VAL] * CMD_HORIZON[c[K_CMD]]
    if c[K_CMD] in CMD_DEPTH: depth += CMD_DEPTH[c[K_CMD]](aim, c[K_VAL]) 

print("part1:", horizontal*depth)

