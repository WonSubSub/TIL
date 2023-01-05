n = int(input())
times = []
costs = []
totals = [0] * (n)

for i in range(n):
    t, c = map(int, input().split(' '))
    times.append(t)
    costs.append(c)

for i in range(n):
    if times[i] > n - i:
        times[i] = 0
        costs[i] = 0

if times[-1] == 1:
    totals[-1] = costs[-1]

def get_total(times, costs, i, totals):
    temp_times = times
    if temp_times[i] == 1:
        totals[i] = totals[i+1] + costs[i]
    elif temp_times[i] != 1:
        time = temp_times[i]
        if time == n - i:
            totals[i] = costs[i]
        else:
            totals[i] = costs[i] + totals[i+time] 
        if totals[i] < totals[i+1]:
            totals[i] = totals[i+1]
    return totals


for i in range(n-2,-1,-1):
    totals = get_total(times, costs, i, totals)
    # print(totals)
ans = max(totals)

print(ans)