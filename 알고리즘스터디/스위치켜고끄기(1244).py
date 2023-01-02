n_switch = int(input())
switches = list(map(int, input().split(' ')))
n_student = int(input())

def change_switch(switches, i):
    if switches[i] == 1:
        switches[i] = 0
    else:
        switches[i] = 1
    return switches


def change(sex, num, switches, n_switch):
    if sex == 1:
        for i in range(n_switch // num):
            switches = change_switch(switches, (i+1)*num - 1)
    if sex == 2:
        switches = change_switch(switches, num - 1)
        i = 0
        while switches[num - 1 + i] == switches[num - 1 - i]:
            switches = change_switch(switches, num - 1 + i)
            switches = change_switch(switches, num - 1 - i)
            if num - 1 - i == 0 or num - 1 + i == n_switch - 1:
                break
            else:
                i += 1
            

for i in range(n_student):
    sex, num = map(int, input().split(' '))
    change(sex, num, switches, n_switch)

count = 0
for i in switches:
    count += 1
    if count % 20 != 0:
        print(i, end=' ')
    else:
        print(i)