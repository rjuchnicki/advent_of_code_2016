import re

f = open('09_input.txt', 'r')
s = f.read().replace('\n', '')
f.close()

def decompressed_length(s):
    i = 0
    count = 0
    while i < len(s):
        if s[i] == '(':
            match = re.match('\((\d+)x(\d+)\)', s[i:])
            marker = len(match.group(0))
            sequence = int(match.group(1))
            repeats = int(match.group(2))

            count += repeats * decompressed_length(
                s[i + marker : i + marker + sequence])
            i += len(match.group(0)) + sequence
        else:
            count += 1
            i += 1
    return count

print decompressed_length(s)
