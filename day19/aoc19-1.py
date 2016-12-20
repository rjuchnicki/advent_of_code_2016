''' 
"Each Elf brings a present. They all sit in a circle, numbered starting with
position 1. Then, starting with the first Elf, they take turns stealing all
the presents from the Elf to their left. An Elf with no presents is removed  
from the circle and does not take turns."
'''

n = 3014387

elves = []
for i in xrange(n, 0, -1):
    elves.append(i)

while len(elves) > 1:
    remaining = []
    if len(elves) % 2 == 0:
        for i in xrange(1, len(elves), 2):
            remaining.append(elves[i])
    else:
        for i in xrange(0, len(elves) - 1, 2):
            remaining.append(elves[i])
    elves = remaining

print elves[0]
