f = open('12_input.txt', 'r')
instructions = [x.strip('\n').split(' ') for x in f.readlines()]
f.close()

def lookup(v):
    try:
        return int(v)
    except:
        return registers[v]

i = 0
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0} # Part 1 input
# registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0} # Part 2 input
while i < len(instructions):
    ins = instructions[i]
    if (ins[0] == 'inc'):
        registers[ins[1]] += 1
    elif (ins[0] == 'dec'):
        registers[ins[1]] -= 1
    elif (ins[0] == 'cpy'):
        registers[ins[2]] = lookup(ins[1])

    if ins[0] == 'jnz' and lookup(ins[1]) != 0:
        i = i + int(ins[2])
    else:
        i += 1

print registers['a']
