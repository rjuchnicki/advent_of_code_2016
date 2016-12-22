from hashlib import md5

door_id = 'uqwqemis'
# door_id = 'abc'
passcode = ''
i = 0
while len(passcode) < 8:
    h = md5((door_id + str(i)).encode('utf-8')).hexdigest()
    if h[:5] == '00000':
        passcode += h[5]

    i += 1

print passcode
