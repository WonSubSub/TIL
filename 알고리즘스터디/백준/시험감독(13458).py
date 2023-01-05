n = int(input())
people = list(map(int, input().split(' ')))
joo, boo = map(int, input().split(' '))

count = 0

new_people = []
for i in people:
    count += 1
    new_people.append(i - joo)

for i in new_people:
    if i > 0:
        if i % boo == 0:
            count += i//boo
        else:
            count += i//boo + 1

print(count)