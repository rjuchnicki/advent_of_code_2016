def valid(pos, keypad, rows, cols):
    return (pos[0] >= 0 and pos[0] <= rows - 1 and pos[1] >= 0 and
            pos[1] <= cols - 1 and keypad[pos[0]][pos[1]] != '*')

def move(keypad, start, instruction):
    pos = start
    rows = len(keypad)
    cols = len(keypad[0])
    d = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    for step in instruction:
        drow,dcol = d[step]
        if valid((pos[0] + drow, pos[1] + dcol), keypad, rows, cols):
            pos = (pos[0] + drow, pos[1] + dcol)

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
