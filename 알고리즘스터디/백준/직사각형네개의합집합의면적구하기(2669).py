cordinates = []

for i in range(4):
    a, b, c, d = map(int, input().split(' '))
    for first in range(a,c):
        for second in range(b,d):
            cordinates.append((first + 0.5, second + 0.5))

print(len(set(cordinates)))