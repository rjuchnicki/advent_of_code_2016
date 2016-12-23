import re

f = open('10_input.txt', 'r')
instructions = f.readlines()
f.close()

robots = {}
transfers = []
max_bot = 0
new_instructions = []
for i in instructions:
    assignment = re.search('value (\d+) goes to bot (\d+)', i)
    if assignment:
        value = int(assignment.group(1))
        robot = int(assignment.group(2))

        if robot > max_bot:
            max_bot = robot

        if robot not in robots:
            robots[robot] = [value]
        else:
            robots[robot].append(value)
    else:
        new_instructions.append(i)
instructions = new_instructions

for j in xrange(max_bot + 1):
    if j not in robots:
        robots[j] = []

outputs = [-1 for i in xrange(max_bot)]

count = 0
while len(instructions) > 0:
    new_instructions = []
    for i in instructions:
        search = re.search(
            'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', i)
        if search:
            robot = int(search.group(1))
            low = int(search.group(3))
            high = int(search.group(5))
            dest_1 = search.group(2)
            dest_2 = search.group(4)

            if len(robots[robot]) == 2:
                small,large = -1, -1
                first,second = robots[robot][0], robots[robot][1]
                if first > second:
                    small = second
                    large = first
                else:
                    small = first
                    large = second

                if dest_1 == 'bot':
                    robots[low].append(small)
                else:
                    outputs[low] = small
                if dest_2 == 'bot':
                    robots[high].append(large)
                else:
                    outputs[high] = large

                if small == 17 and large == 61:
                    print "ROBOT:", robot  # Part 1
            else:
                new_instructions.append(i)
        else:
            print "ERROR"

    instructions = new_instructions

print outputs[0] * outputs[1] * outputs[2]  # Part 2
