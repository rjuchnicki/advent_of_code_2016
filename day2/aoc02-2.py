def valid(keypad, pos):
    return keypad[pos[0]][pos[1]] != '*'

def move(keypad, start, instruction):
    pos = start
    rows = len(keypad)
    cols = len(keypad[0])

    for step in instruction:
        if step == 'L':
            if pos[1] > 0:
                new = (pos[0], pos[1] - 1)
                if valid(keypad, new):
                    pos = new
        elif step == 'R':
            if pos[1] < cols - 1:
                new = (pos[0], pos[1] + 1)
                if valid(keypad, new):
                    pos = new
        elif step == 'U':
            if pos[0] > 0:
                new = (pos[0] - 1, pos[1])
                if valid(keypad, new):
                    pos = new
        elif step == 'D':
            if pos[0] < rows - 1:
                new = (pos[0] + 1, pos[1])
                if valid(keypad, new):
                    pos = new

    return pos

def bathroom_code(keypad, start, instructions):
    pos = start
    buttons = ''
    for instruction in instructions:
        pos = move(keypad, pos, instruction)
        buttons += keypad[pos[0]][pos[1]]

    return buttons

f = open('02_input.txt', 'r')
instructions = [x.strip('\n') for x in f.readlines()]
f.close()

keypad = [['*', '*', '1', '*', '*'], 
          ['*', '2', '3', '4', '*'],
          ['5', '6', '7', '8', '9'],
          ['*', 'A', 'B', 'C', '*'],
          ['*', '*', 'D', '*', '*']]
start = (2, 0)
print bathroom_code(keypad, start, instructions) # Result: C1A88
