n, my_score, length = map(int, input().split())
ans = 0
if n == 0:
    ans = 1
else:
    scores = list(map(int, input().split()))

    if n >= length and my_score <= min(scores):
        ans = -1
    elif scores == []:
        ans = 1
    else:
        if len(scores) == length:
            scores.sort(reverse = True)
            scores.remove(scores[-1])
            scores.append(my_score)
            scores.sort(reverse = True)
            ans = scores.index(my_score) + 1
        else:
            scores.append(my_score)
            scores.sort(reverse = True)
            ans = scores.index(my_score) + 1

print(ans)
