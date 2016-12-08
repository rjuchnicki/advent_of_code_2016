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
    passing_through = []
    xy_new = (xy[0], xy[1])
    if heading_new == NORTH:
        for i in xrange(0, distance):
            xy_new = (xy_new[0], xy_new[1] + 1)
            passing_through.append(xy_new)
    elif heading_new == SOUTH:
        for i in xrange(0, distance):
            xy_new = (xy_new[0], xy_new[1] - 1)
            passing_through.append(xy_new)
    elif heading_new == EAST:
        for i in xrange(0, distance):
            xy_new = (xy_new[0] + 1, xy_new[1])
            passing_through.append(xy_new)
    elif heading_new == WEST:
        for i in xrange(0, distance):
            xy_new = (xy_new[0] - 1, xy_new[1])
            passing_through.append(xy_new)    

    return xy_new, heading_new, passing_through

def navigate(xy, starting_heading, moves):
    previous_xy = {}

    xy_new = xy
    heading = starting_heading
    intermediate_points = []
    for move in moves:
        previous_xy[xy_new] = 1
        xy_new, heading, intermediate_points = step(xy_new, heading, move)
        for p in intermediate_points:
            if p in previous_xy:
                return p
            else:
                previous_xy[p] = 1

    # Return final destination if no points visited twice. Evil Easter bunny :(
    return xy_new

def manhattan_distance(src, dest):
    return abs(dest[1] - src[1]) + abs(dest[0] - src[0])

f = open('01_input.txt', 'r')
s = f.read()
f.close()

moves = s.replace('\n', '').split(', ')
start = (0,0)

print manhattan_distance(start, navigate(start, NORTH,
                                         ['R8', 'R4', 'R4', 'R8']))
print manhattan_distance(start, navigate(start, NORTH, moves)) # Result: 159
