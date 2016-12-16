a = '11011110011011101'
disk_size = 35651584

while len(a) < disk_size:
    a = a + '0' + a[::-1].replace('0', 'x').replace('1', '0').replace('x', '1')
a = a[:disk_size]

checksum = a
while len(checksum) % 2 != 1:
    new_checksum = ''
    for i in xrange(0, len(checksum) / 2):
        if checksum[2*i] == checksum[2*i + 1]:
            new_checksum += '1'
        else:
            new_checksum += '0'
    checksum = new_checksum

print checksum
