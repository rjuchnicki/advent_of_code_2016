from collections import deque

fav = 1350
dest = (31, 39)

# fav = 10
# dest = (7, 4)

start = ((1, 1), 0)
d = deque()
d.append(start)

dirs = [(0,1), (0,-1), (-1,0), (1,0)]

visited = {(1,1): 1}
while d:
    move = d.popleft()
    pos = move[0]
    steps = move[1]

    # Part 1
    # if pos == dest:
    #     print 'Steps:', steps
    #     quit()

    # Part 2
    if steps > 50:
        print len(visited) - 1
        quit()

    for dir in dirs:
        dx,dy = dir
        x,y = pos[0] + dx, pos[1] + dy
        if x > -1 and y > -1 and (x, y) not in visited:
            wall = x*x + 3*x + 2*x*y + y + y*y
            wall += fav
            wall = bin(wall)[2:].count('1')
            if wall % 2 == 0:
                d.append(((x, y), steps + 1))
                visited[(x,y)] = 1

print visited
