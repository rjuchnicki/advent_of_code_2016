from collections import deque

n = 3014387

left = deque(i for i in xrange(1, int(n // 2) + 1))
right = deque(i for i in xrange(int(n // 2) + 1, n + 1))

while left and right:
    if len(left) > len(right):
        left.pop()
    else:
        right.popleft()

    if left and right:
        left.append(right.popleft())
        right.append(left.popleft())

print left[0]
