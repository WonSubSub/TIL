import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    ind = [x for x in range(1,n+1)]

    cnt = 0
    a = ind[0]
    b = nums[0]
    temp = a
    while len(ind) > 0:
        while a == b:
            cnt += 1
            ind.remove(a)
            nums.remove(b)
            if len(ind) > 0:
                a = ind[0]
                b = nums[0]
                temp = a
            else:
                break
        if len(ind) > 0:
            ind.remove(a)
            nums.remove(b)
        if len(ind) == 0:
            break
        else:
            if b in ind:
                c = ind.index(b)
                a = ind[c]
                b = nums[c]
                if b == temp:
                    cnt += 1
                    ind.remove(a)
                    nums.remove(b)
                    if len(ind) > 0:
                        a = ind[0]
                        b = nums[0]
                        temp = a
                    else:
                        break
            else:
                a = ind[0]
                b = nums[0]
                temp = a
    print(cnt)
