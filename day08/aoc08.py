import re

f = open('08_input.txt', 'r')
instructions = [x.replace('\n', '') for x in f.readlines()]
f.close()

a = [['.' for x in xrange(50)] for i in xrange(6)]

# instructions = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4',
                # 'rotate column x=1 by 1']
# a = [['.' for x in xrange(7)] for i in xrange(3)]

for inst in instructions:
    rect = re.search(r'rect (\d+)x(\d+)', inst)
    if rect:
        for i in xrange(int(rect.group(2))):
            for j in xrange(int(rect.group(1))):
                a[i][j] = '#'

    row = re.search(r'rotate row y=(\d+) by (\d+)', inst)
    if row:
        r = int(row.group(1))
        pos = int(row.group(2))
        a[r] = a[r][-pos:] + a[r][:-pos]

    col = re.search(r'rotate column x=(\d+) by (\d+)', inst)
    if col:
        c = int(col.group(1))
        pos = int(col.group(2))
        l = []
        for i in xrange(len(a)):
            l.append(a[i][c])
        l = l[-pos:] + l[:-pos]
        for i in xrange(len(a)):
            a[i][c] = l[i]

count = 0
for i in xrange(len(a)):
    for j in xrange(len(a[0])):
        if a[i][j] == '#':
            count += 1

print count  # Part 1

# Part 2
for i in a:
    print ''.join(i)
