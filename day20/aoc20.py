f = open('20_input.txt', 'r')
input = f.read()
f.close()

intervals = [interval.split('-') for interval in input.split('\n')]
intervals = [(int(i[0]), int(i[1])) for i in intervals]

# Since one of the intervals begins with 0, the smallest ip that is not blocked
# will be 1 more than the top of one of the intervals.
candidates = sorted([i[1] + 1 for i in intervals])

def is_whitelisted(n, intervals):
  for bottom,top in intervals:
    if bottom <= n <= top:
      return False

  return True

whitelisted = [c for c in candidates if is_whitelisted(c, intervals)]
print whitelisted[0]  # Part 1

# For each ip in the whitelist, count up to the nearest bottom of an interval.
bottoms = sorted([y[0] for y in intervals])
count = 0
for ip in whitelisted:
  for bottom in bottoms:
    if ip < bottom:
      count += (bottom - ip)
      break
print count  # Part 2
