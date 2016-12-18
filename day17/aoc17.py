""" 
Room grid:

#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |D 
####### V
"""

from hashlib import md5
from collections import deque
from itertools import compress

input = 'pxxbnzuo'
# Does not follow Cartesian coordinates. (0,0) is in the top left and (3,3) is
# the bottom right.
dirs = {'U': (0,-1), 'D':(0,1), 'L':(-1,0), 'R':(1,0)}

start = (0,0)
dest = (3,3)

# Perform BFS going through open doors.
d = deque()
d.append((start, ''))

while d:
    move = d.popleft()
    pos = move[0]
    steps = move[1]
    if pos == dest:
        # Uncomment for Part 1:
        print steps
        quit()
        # Uncomment for Part 2:
        # After finding a path to dest, print the path length and continue
        # expanding candidates in the deque. The last length printed will be
        # that of the longest path.
        # print len(steps)
        # continue

    passcode = input + move[1]
    open = [int(x, 16) > 10 for x in md5(passcode.encode('utf-8')).hexdigest()[:4]]
    for dir in compress('UDLR', open):
        dx,dy = dirs[dir]
        new = (pos[0] + dx, pos[1] + dy)
        if (0 <= new[0] < 4 and 0 <= new[1] < 4):
            d.append((new, steps + dir))
