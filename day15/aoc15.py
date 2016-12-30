discs = [[10, 13], [15, 17], [17, 19], [1, 7], [0, 5], [1, 3]]  # Part 1
discs = [[10, 13], [15, 17], [17, 19], [1, 7], [0, 5], [1, 3],
         [0, 11]] # Part 2

def pass_through(discs):
    for i in xrange(len(discs)):
        if (discs[i][0] + i + 1) % discs[i][1] != 0:
            return False
    return True

t = 0
while not pass_through(discs):
    for pos in discs:
        pos[0] = (pos[0] + 1) % pos[1]
    t += 1

print t
