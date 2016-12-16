import re

def is_triangle(sides):
    return 1 if (sides[0] + sides[1] > sides[2] and
                 sides[0] + sides[2] > sides[1] and
                 sides[1] + sides[2] > sides[0]) else 0

f = open('03_input.txt', 'r')
lengths = [[int(s) for s in re.findall('\d+', line)] 
           for line in f.readlines()]
f.close()

count = 0
for l in lengths:
    count += is_triangle(l)

print count
