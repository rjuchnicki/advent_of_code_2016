f = open('06_input.txt', 'r')
messages = [x.strip('\n') for x in f.readlines()]
f.close()

counts = [{} for i in messages[0]]

for message in messages:
    for i in xrange(len(message)):
        c = message[i]
        counts[i][c] = 1 if c not in counts[i] else counts[i][c] + 1

code = ''
for count in counts:
    # code += max(count.items(), key=lambda k: k[1])[0]  # Part 1
    code += min(count.items(), key=lambda k: k[1])[0]  # Part 2
print code
