# codes = ['a-b-c-d-e-f-g-h-987[abcde]', 'aaaaa-bbb-z-y-x-123[abxyz]',
#          'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

f = open('04_input.txt', 'r')
codes = [x.strip('\n') for x in f.readlines()]
f.close()

total = 0
for code in codes:
    checksum_ind = code.find('[')
    checksum = code[checksum_ind + 1:-1]
    sector_id = int(code[checksum_ind - 3:checksum_ind])

    chars = {}
    for i in xrange(0, checksum_ind - 3):
        if code[i] != '-':
            chars[code[i]] = 1 if code[i] not in chars else chars[code[i]] + 1
    ranked = sorted(chars.items(), key=lambda x : (x[1], ord('z') - ord(x[0])),
                    reverse=True)

    if ''.join([x[0] for x in ranked[:5]]) == checksum:
        total += sector_id

print total
