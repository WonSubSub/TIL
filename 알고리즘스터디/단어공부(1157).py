word = input().lower()

alphabets = "abcdefghijklmnopqrstuvwxyz"
count = []
for alphabet in alphabets:
    count.append(word.count(alphabet))

ans = alphabets[count.index(max(count))].upper()

if count.count(max(count)) > 1:
    ans = "?"

print(ans)