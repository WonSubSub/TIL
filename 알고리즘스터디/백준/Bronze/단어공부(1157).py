word = input().upper()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = []
for alphabet in alphabets:
    count.append(word.count(alphabet))

ans = alphabets[count.index(max(count))]
if count.count(max(count)) > 1:
    ans = "?"

print(ans)