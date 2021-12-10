from pathlib import Path

###################
## part 1

K_FX = "fx"  # x of point_from
K_FY = "fy"  
K_TX = "tx"  # x o point_to
K_TY = "ty"
K_TYPE = "line_type"
TYPE_V = "v" # vertical line
TYPE_H = "h" # horizontal line
TYPE_D_UP = "d_up" # diagonal line, goes up
TYPE_D_DOWN = "d_down" # diagonal line, goes down
K_POINTS = "points"

# input points: "x,y"
# return: FX <= TX, FY <= TY
def get_line(p_from_str, p_to_str):
    from_xy = p_from_str.split(",")
    to_xy = p_to_str.split(",")
    line = {K_FX:int(from_xy[0]), K_FY:int(from_xy[1]),K_TX:int(to_xy[0]), K_TY:int(to_xy[1]), K_TYPE:None}

    ret = line.copy() 
    if line[K_FX] == line[K_TX]:
        ret[K_TYPE] = TYPE_V
        ret[K_FY] = min(line[K_FY], line[K_TY])
        ret[K_TY] = max(line[K_FY], line[K_TY])
    elif line[K_FY] == line[K_TY]:
        ret[K_TYPE] = TYPE_H
        ret[K_FX] = min(line[K_FX], line[K_TX])
        ret[K_TX] = max(line[K_FX], line[K_TX])
    elif (line[K_FX] - line[K_FY]) == (line[K_TX] - line[K_TY]): # y = x + k
        ret[K_TYPE] = TYPE_D_UP
        k = line[K_FY] - line[K_FX]
        ret[K_FX] = min(line[K_FX], line[K_TX])
        ret[K_FY] = ret[K_FX] + k 
        ret[K_TX] = max(line[K_FX], line[K_TX])
        ret[K_TY] = ret[K_TX] + k 
    elif (line[K_FX] + line[K_FY]) == (line[K_TX] + line[K_TY]): # y = k - x
        ret[K_TYPE] = TYPE_D_DOWN
        k = line[K_FX] + line[K_FY]
        ret[K_FX] = min(line[K_FX], line[K_TX])
        ret[K_FY] = k - ret[K_FX] 
        ret[K_TX] = max(line[K_FX], line[K_TX])
        ret[K_TY] = k - ret[K_TX]
    return ret 

# return all points in a line, format of point: 422,24
def get_points_in_line(line):
    if K_POINTS in line and line[K_POINTS] is not None:
        return line[K_POINTS]
    points = [] 
    if line[K_TYPE] == TYPE_V:
        for i in range(line[K_FY], line[K_TY]+1):
            points.append("%d,%d" % (line[K_FX],i))
    if line[K_TYPE] == TYPE_H:
        for i in range(line[K_FX], line[K_TX]+1):
            points.append("%d,%d" % (i, line[K_FY]))
    if line[K_TYPE] == TYPE_D_UP:
        k = line[K_FY] - line[K_FX]
        for x in range(line[K_FX],line[K_TX]+1):
            points.append("%d,%d" % (x, x + k))
    if line[K_TYPE] == TYPE_D_DOWN:
        xy_sum = line[K_FX] + line[K_FY]
        for x in range(line[K_FX], line[K_TX]+1):
            points.append("%d,%d" % (x,xy_sum - x))
    return points 

def main(lines_str, types):
    lines_list = []
    overlap = [] 
    for l_str in lines_str:
        two_parts = l_str.split(" -> ")
        line = get_line(two_parts[0], two_parts[1])
        if line[K_TYPE] not in types: continue 

        line_points = get_points_in_line(line)
        for l in lines_list: 
            points = l[K_POINTS]
            temp = list(set(line_points) & set(points))
            if len(temp) == 0: continue
            overlap = list(set(overlap) | set(temp))

        line[K_POINTS] = line_points
        lines_list.append(line)
    print("line count: ", len(lines_list))
    return len(overlap)

# main
#with open(Path(__file__).parent/"input_sample.txt", 'r') as file:
with open(Path(__file__).parent/"input.txt", 'r') as file:
    lines = file.read().splitlines()

result = main(lines, [TYPE_V, TYPE_H])
print("part 1: %d" % result)
result = main(lines, [TYPE_V, TYPE_H, TYPE_D_UP, TYPE_D_DOWN])
print("part 2: %d" % result)