n = int(input())

cordinates = []
heights = []
ch = []
for i in range(n):
    cordinate, height = map(int, input().split())
    ch.append((cordinate, height))

ch.sort()
for i in range(n):
    cordinates.append(ch[i][0])
    heights.append(ch[i][1])

left_max_index = heights.index(max(heights))
heights_reverse = heights[::-1]
cordinates_reverse = cordinates[::-1]
right_max_index = n - 1 - heights_reverse.index(max(heights_reverse))

if heights.count(heights[left_max_index]) > 1:
    for i in range(left_max_index, (right_max_index + 1)):
        heights[i] = max(heights)

for i in range(1, left_max_index):
    if heights[i] < heights[i-1]:
        heights[i] = heights[i-1]

max_index_reverse = heights_reverse.index(max(heights_reverse))
for i in range(1, max_index_reverse):
    if heights_reverse[i] < heights_reverse[i-1]:
        heights_reverse[i] = heights_reverse[i-1]

ans = 0

ans += max(heights) * (cordinates[right_max_index] - cordinates[left_max_index] + 1)

for i in range(left_max_index):
    ans += (cordinates[i+1] - cordinates[i]) * heights[i]

for i in range(max_index_reverse):
    ans -= (cordinates_reverse[i+1] - cordinates_reverse[i]) * heights_reverse[i]

print(ans)


