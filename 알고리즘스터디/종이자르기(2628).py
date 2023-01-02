h, v = map(int, input().split(' '))
n = int(input())

horizontal = [x for x in range(1, h+1)]
vertical = [x for x in range(1, v+1)]

def cut(line, list):
    list.insert(list.index(line)+1 , 0)
    return list

def max_length(list):
    count = 0
    temp_count = 0
    for i in list:
        if i == 0:
            if temp_count > count:
                count = temp_count
            temp_count = 0
        elif i == list[-1]:
            temp_count += 1
            if temp_count > count:
                count = temp_count
        else:
            temp_count += 1
    return count


for _ in range(n):
    hv, line = map(int, input().split(' '))

    if hv == 0:
        vertical = cut(line, vertical)
    else:
        horizontal = cut(line, horizontal)

print(max_length(horizontal) * max_length(vertical))

 