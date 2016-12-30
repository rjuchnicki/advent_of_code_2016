import re
from hashlib import md5

stretches = 2016

keys = []
salt = 'qzyelonm'
# salt = 'abc'
for i in xrange(1001):
    gen = salt + str(i)
    # For Part 1, remove this loop and move the loop block back an indentation
    # level.
    for i in xrange(stretches + 1):
        gen = md5(gen.encode('utf-8')).hexdigest()
    keys.append(gen)

hashes = 0
i = 0
while hashes < 64:
    repeated = re.search(r'(\w)\1\1', keys[i])
    if repeated:
        s = repeated.group(0)
        s += s[0] * 2
        for j in xrange(i+1, i+1000):
            if s in keys[j]:
                hashes += 1
                break

    gen = salt + str(i + 1001)
    # Do the same as above for Part 1.
    for j in xrange(stretches + 1):
        gen = md5(gen.encode('utf-8')).hexdigest()
    keys.append(gen)

    i += 1

print i - 1
