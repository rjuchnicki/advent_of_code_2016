from hashlib import md5

door_id = 'uqwqemis'
# door_id = 'abc'
passcode = ['*', '*', '*', '*', '*', '*', '*', '*']
filled = 0
i = 0
while filled < 8:
    h = md5((door_id + str(i)).encode('utf-8')).hexdigest()
    if h[:5] == '00000':
        pos = int(h[5], 16)
        if pos < 8:
            if passcode[pos] == '*':
                passcode[pos] = h[6]
                filled += 1

    i += 1

print ''.join(passcode)
