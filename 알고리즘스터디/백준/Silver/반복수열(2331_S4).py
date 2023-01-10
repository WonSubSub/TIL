n, p = map(int, input().split())

numbers = [n]
cnt = 0
while True:
    number_list = list(map(int, str(numbers[cnt])))
    number = 0
    for i in number_list:
        number += i**p
    if number in numbers:
        print(numbers.index(number))
        break
    else:
        numbers.append(number)
        cnt += 1