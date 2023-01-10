import sys
input = sys.stdin.readline

title, player = map(int, input().split())

title_name = []           # 리스트 두개
title_number = [0]
for i in range(title):
    name, number = input().split()
    if title_number[-1] != int(number) + 1:
        title_name.append(name)
        title_number.append(int(number)+1)

# titles = [[0,0]]            # 이중리스트
# for i in range(title):
#     name, number = input().split()
#     # if titles[-1][1] != int(number) + 1:
#     titles.append([name, int(number) + 1])

# titles = {0: 'a'}           # 딕셔너리
# for i in range(title):
#     name, number = input().split()
#     if (int(number) + 1) not in titles.keys():
#         titles[int(number)+1] = name
# title_number = list(titles.keys())

def search(score, title_number, s, e):
    m = int((s+e)/2)
    if score == title_number[m]:       # 리스트 두개 재귀
        answer = title_name[m]
        return answer
    elif e-s == 1:
        return title_name[s]
    elif score < title_number[m]:
        return search(score, title_number, s, m)
    else:
        return search(score, title_number, m, e)
    
    # answer = 0               # 리스트 두개 반복문
    # m = int((s+e)/2)
    # while True:
    #     if title_number[m] <= score < title_number[m+1] :
    #         answer = title_name[m]
    #         break
    #     elif score < title_number[m]:
    #         e = m
    #     else:
    #         s = m
    #     m = int((s+e)/2)
    # return answer

    # answer = 0              # 이중리스트 반복문
    # m = int((s+e)/2)
    # while True:
    #     if titles[m][1] <= score < titles[m+1][1] :
    #         answer = titles[m+1][0]
    #         break
    #     elif score < titles[m][1]:
    #         e = m
    #     else:
    #         s = m
    #     m = int((s+e)/2)
    # return answer

    # answer = 0            # 딕셔너리
    # while True:
    #     if title_number[int((s+e)/2)] <= score < title_number[int((s+e)/2)+1] :
    #         answer = titles[title_number[int((s+e)/2)+1]]
    #         break
    #     elif score < title_number[int((s+e)/2)]:
    #         e = (s+e)/2
    #     else:
    #         s = (s+e)/2
    # return answer

# for i in range(player):               # 이중리스트
#     score = int(input())
#     print(search(score, titles, 0, len(titles)-1))

for i in range(player):
    score = int(input())
    print(search(score, title_number, 0, len(title_number)-1))

    