n = int(input())

count = 1
clock = 0

for i in range(n):
    a, b, c = map(int, input().split(' '))

    count = count * b / a
    if c:
        clock = not clock

print(int(clock), int(count))
    