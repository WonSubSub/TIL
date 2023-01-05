n = int(input())

name = []
day = []
month = []
year = []
age_list = []

for i in range(n):
    student = input().split(' ')
    name.append(student[0])
    day.append(int(student[1]))
    month.append(int(student[2]))
    year.append(int(student[3]))

def cal_age(year, month, day, index):
    return (2022 - year[index]) * 365 + (12 - month[index]) * 30 + (31 - day[index])

for i in range(n):
    age = cal_age(year, month, day, i)
    age_list.append(age)

young_index = age_list.index(min(age_list))
old_index = age_list.index(max(age_list))

print(name[young_index])
print(name[old_index])