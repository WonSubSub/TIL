n = int(input())

direction = []
length = []
for i in range(6):
    a, b = map(int, input().split())
    direction.append(a)
    length.append(b)

max_index = length.index(max(length))
new_direction = []
new_length = []
new_direction.extend(direction[max_index:])
new_direction.extend(direction[:max_index])
new_length.extend(length[max_index:])
new_length.extend(length[:max_index])

double = []

for i in range(1,5):
    if new_direction.count(i) == 2:
        double.append(i)

for i in range(6):
    if new_direction[i] in double:
        new_length = new_length[i:i+4]
        break
answer = (new_length[0] + new_length[2]) * (new_length[3] + new_length[1]) - new_length[1] * new_length[2]
print(answer * n)
