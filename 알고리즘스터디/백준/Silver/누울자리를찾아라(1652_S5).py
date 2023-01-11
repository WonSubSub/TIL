n = int(input())

matrix = []
for i in range(n):
    s = input()
    m = []
    for a in s:
        if a == '.':
            m.append(0)
        else:
            m.append(1)
    matrix.append(m)

horizontal = 0
for m in matrix:
    cnt = 0
    for i in m:
        if i == 0:
            cnt += 1
            if cnt == 2:
                horizontal += 1
        else:
            cnt = 0

vertical = 0
for i in range(n):
    cnt = 0
    for m in matrix:
        if m[i] == 0:
            cnt += 1
            if cnt == 2:
                vertical += 1
        else:
            cnt = 0

print(horizontal, vertical)