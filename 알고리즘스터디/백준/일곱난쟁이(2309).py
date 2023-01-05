count = 0
numbers = []

for i in range(9):
    number = int(input())
    numbers.append(number)
    count += number

numbers.sort()

for i in range(9):
    for a in range(i+1,9):
        sum = numbers[i] + numbers[a]
        if count - sum == 100:
            numbers.pop(a)
            numbers.pop(i)
            break
    if count - sum == 100:
        break

for i in numbers:
    print(i)