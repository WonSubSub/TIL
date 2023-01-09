import sys
input = sys.stdin.readline

title, player = map(int, input().split())

title_name = []
title_number = [0]
for i in range(title):
    name, number = input().split()
    if int(number) not in title_number:
        title_name.append(name)
        title_number.append(int(number))

def search(player_number, title_number):
    if len(title_number) == 1:
        if player_number == title_number[0]:
            return title_number[0], 1
        else:
            return title_number[0], 0
    else:
        if player_number < title_number[int(len(title_number)/2)]:
            return search(player_number, title_number[:int(len(title_number)/2)])
        else:
            return search(player_number, title_number[int(len(title_number)/2):])

for i in range(player):
    player_number = int(input())
    player_title, b = search(player_number, title_number)
    if player_number == 0:
        print(title_name[0])
    else:
        if b:
            print(title_name[title_number.index(player_title)-1])
        else:
            print(title_name[title_number.index(player_title)])
    