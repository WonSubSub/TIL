n, l = map(int, input().split())
holes = sorted(list(map(int, input().split())))
pipe = [0] * (max(holes) + 1)
ans = 0

for hole in holes:
    pipe[hole] = 1

for i in range(len(pipe)):
    if pipe[i] == 1:
        ans += 1
        if len(pipe) < i + l:
            for a in range(i, len(pipe)):
                pipe[a] = 0
        else:
            for a in range(i, i+l):
                pipe[a] = 0

print(ans)