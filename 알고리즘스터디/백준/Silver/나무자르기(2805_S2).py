import sys
input = sys.stdin.readline

n, l = map(int, input().split())
trees = sorted(list(map(int, input().split())), reverse=True)

if n == 1:          # if n:할때 오류
    answer = trees[0] - l
else:
    sub = [0]
    for i in range(len(trees)-1):
        sub.append(trees[i] - trees[i+1])
    sub.append(trees[-1])

    for i in range(len(sub)):
        l -= i * sub[i]
        if l <= 0 :
            index = i
            leftover = l + i * sub[i]
            break
    
    answer = trees[0]
    for i in range(index):
        answer -= sub[i]

    if leftover % index == 0:
        answer -= int(leftover / index)
    else:
        answer -= int(leftover // index + 1)

print(answer)