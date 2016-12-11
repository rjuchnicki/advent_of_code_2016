NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def step(xy, heading, move):
    heading_new = heading
    if move[0] == 'L':
        heading_new = (heading - 1) % 4
    elif move[0] == 'R':
        heading_new = (heading + 1) % 4

    distance = int(move[1:])
    xy_new = None
    if heading_new == NORTH:
        xy_new = (xy[0], xy[1] + distance)
    elif heading_new == SOUTH:
        xy_new = (xy[0], xy[1] - distance)
    elif heading_new == EAST:
        xy_new = (xy[0] + distance, xy[1])
    elif heading_new == WEST:
        xy_new = (xy[0] - distance, xy[1])

    return xy_new, heading_new

def navigate(xy, start_heading, moves):
    xy_new = xy
    heading = start_heading
    for move in moves:
        xy_new, heading = step(xy_new, heading, move)

    return xy_new

def manhattan_distance(src, dest):
    return abs(dest[1] - src[1]) + abs(dest[0] - src[0])

f = open('01_input.txt', 'r')
s = f.read()
f.close()

moves = s.replace('\n', '').split(', ')
start = (0,0)

print manhattan_distance(start, navigate(start, NORTH, ['R2', 'L3']))
print manhattan_distance(start, navigate(start, NORTH, ['R2', 'R2', 'R2']))
print manhattan_distance(start, navigate(start, NORTH,
                                         ['R5', 'L5', 'R5', 'R3']))
print manhattan_distance(start, navigate(start, NORTH, moves)) # Result: 300
