n, num = input().split()
n = int(n)

num_horizontal1 = {'1': ' '*(n + 2),
                  '2': ' ' + '-' * n + ' ',
                  '3': ' ' + '-' * n + ' ',
                  '4': ' '*(n + 2),
                  '5': ' ' + '-' * n + ' ',
                  '6': ' ' + '-' * n + ' ',
                  '7': ' ' + '-' * n + ' ',
                  '8': ' ' + '-' * n + ' ',
                  '9': ' ' + '-' * n + ' ',
                  '0': ' ' + '-' * n + ' ',
                  }
num_horizontal2 = {'1': ' '*(n + 2),
                  '2': ' ' + '-' * n + ' ',
                  '3': ' ' + '-' * n + ' ',
                  '4': ' ' + '-' * n + ' ',
                  '5': ' ' + '-' * n + ' ',
                  '6': ' ' + '-' * n + ' ',
                  '7': ' '*(n + 2),
                  '8': ' ' + '-' * n + ' ',
                  '9': ' ' + '-' * n + ' ',
                  '0': ' '*(n + 2),
                  }
num_horizontal3 = {'1': ' '*(n + 2),
                  '2': ' ' + '-' * n + ' ',
                  '3': ' ' + '-' * n + ' ',
                  '4': ' '*(n + 2),
                  '5': ' ' + '-' * n + ' ',
                  '6': ' ' + '-' * n + ' ',
                  '7': ' '*(n + 2),
                  '8': ' ' + '-' * n + ' ',
                  '9': ' ' + '-' * n + ' ',
                  '0': ' ' + '-' * n + ' ',
                  }
num_vertical1 = {'1': ' '*(n+1) + '|',
                '2': ' '*(n+1) + '|',
                '3': ' '*(n+1) + '|',
                '4': '|' + ' '*n + '|',
                '5': '|' + ' '*(n+1),
                '6': '|' + ' '*(n+1),
                '7': ' '*(n+1) + '|',
                '8': '|' + ' '*n + '|',
                '9': '|' + ' '*n + '|',
                '0': '|' + ' '*n + '|',
                }
num_vertical2 = {'1': ' '*(n+1) + '|',
                '2': '|' + ' '*(n+1),
                '3': ' '*(n+1) + '|',
                '4': ' '*(n+1) + '|',
                '5': ' '*(n+1) + '|',
                '6': '|' + ' '*n + '|',
                '7': ' '*(n+1) + '|',
                '8': '|' + ' '*n + '|',
                '9': ' '*(n+1) + '|',
                '0': '|' + ' '*n + '|',
                }

for i in num:
    print(num_horizontal1[i], end=' ')
print()
for a in range(n):
    for i in num:
        print(num_vertical1[i], end=' ')
    print()
for i in num:
    print(num_horizontal2[i], end=' ')
print()
for a in range(n):
    for i in num:
        print(num_vertical2[i], end=' ')
    print()
for i in num:
    print(num_horizontal3[i], end=' ')
