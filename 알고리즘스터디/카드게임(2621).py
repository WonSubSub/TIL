color = []
number = []

for i in range(5):
    c, n = input().split(' ')
    color.append(c)
    number.append(int(n))

ans = []

for i in number:
    if number.count(i) == 3:
        for a in number:
            if number.count(a) == 2:
                ans.append(i*10 + a + 700)
        ans.append(400 + i)
    if number.count(i) == 2:
        for a in number:
            if a != i and number.count(a) == 2:
                ans.append(max(a, i)*10 + min(a, i) + 300)
        ans.append(i + 200)
    if number.count(i) == 4:
        ans.append(800 + i)
    ans.append(100 + i)

series = 1
for i in range(4): 
    if sorted(number)[i+1] - sorted(number)[i] != 1:
        series = 0

if len(set(color)) == 1:
    ans.append(max(number) + 600)

if series:
    if len(set(color)) == 1:
        ans.append(max(number) + 900)
    ans.append(max(number) + 500)

print(max(ans))