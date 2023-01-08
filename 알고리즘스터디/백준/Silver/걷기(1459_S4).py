x, y, w, s = map(int, input().split())

answer = 0
if s > 2*w:
    answer = (x + y) * w

elif w <= s <= 2*w:
    answer += min(x,y) * s
    answer += (max(x,y) - min(x,y)) * w

elif s < w:
    if (max(x,y) - min(x,y)) % 2 == 0:
        answer = max(x,y) * s
    else:
        answer += min(x,y) * s
        answer += (max(x,y) - min(x,y) - 1) * s
        answer += w

print(answer)
