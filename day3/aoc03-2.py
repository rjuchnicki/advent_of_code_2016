import re

def is_triangle(a, b, c):
    return 1 if (a + b > c and a + c > b and b + c > a) else 0

f = open('03_input.txt', 'r')
lengths = [[int(s) for s in re.findall('\d+', line)] 
           for line in f.readlines()]
f.close()

col1 = []
col2 = []
col3 = []
for l in lengths:
    col1.append(l[0])
    col2.append(l[1])
    col3.append(l[2])
lengths = col1 + col2 + col3

count = 0
for i in xrange(0, len(lengths) / 3):
    count += is_triangle(lengths[3 * i], lengths[3 * i + 1],
                         lengths[3 * i + 2])

print count
