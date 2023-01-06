n, place = map(int, input().split(' '))

result = []
for i in range(n):
    country, gold, silver, bronze = map(int, input().split(' '))
    result.append((gold, silver, bronze, country))

result = sorted(result, reverse=True)

for i in range(n):
    if result[i][-1] == place:
        medals = result[i][:3]
        break

for i in range(n):
    if result[i][:3] == medals:
        ans = i + 1
        break

print(ans)