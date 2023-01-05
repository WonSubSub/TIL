n = int(input())

cordinates = []
heights = []
ch = []
for i in range(n):
    cordinate, height = map(int, input().split())
    ch.append((cordinate, height))

ch.sort()
for i in range(n):
    cordinates.append(ch[0])
    heights.append(ch[1])

print(cordinates)
print(heights)


