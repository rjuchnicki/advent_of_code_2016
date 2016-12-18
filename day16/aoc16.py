a = '11011110011011101'
disk_size = 272  # Part 1 input
# disk_size = 35651584  # Part 2 input

while len(a) < disk_size:
    a = a + '0' + ''.join('1' if i == '0' else '0' for i in a[::-1])
a = a[:disk_size]

checksum = a
while len(checksum) % 2 == 0:
    new_checksum = ''
    for i in xrange(0, len(checksum), 2):
        if checksum[i] == checksum[i + 1]:
            new_checksum += '1'
        else:
            new_checksum += '0'
    checksum = new_checksum

print checksum
