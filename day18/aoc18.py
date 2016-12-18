f = open('18_input.txt', 'r')
tiles = f.read().replace('\n', '')
f.close()

tiles = '.' + tiles + '.'
# rows = 40  # Part 1
rows = 400000  # Part 2

count = 0
for i in xrange(0, rows):
    count += tiles.count('.')
    new_tiles = '.'
    for i in xrange(1, len(tiles) - 1):
        if tiles[i-1] == '^' and tiles[i] == '^' and tiles[i+1] == '.':
            new_tiles += '^'
        elif tiles[i-1] == '.' and tiles[i] == '^' and tiles[i+1] == '^':
            new_tiles += '^'
        elif tiles[i-1] == '^' and tiles[i] == '.' and tiles[i+1] == '.':
            new_tiles += '^'
        elif tiles[i-1] == '.' and tiles[i] == '.' and tiles[i+1] == '^':
            new_tiles += '^'
        else:
            new_tiles += '.'

    tiles = new_tiles + '.'

# print count - 40 * 2  # Part 1
print count - 400000 * 2  # Part 2
