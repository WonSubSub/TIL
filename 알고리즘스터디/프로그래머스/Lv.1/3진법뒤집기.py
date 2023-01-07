# def solution(n):
#     answer = 0
#     cnt = 0
#     temp_n = 1
#     while temp_n < n:
#         temp_n = temp_n * 3
#         cnt += 1
#     print(cnt)
    
#     jeesoo = []
#     for i in range(cnt-1, -1, -1):
#         if n - 3**i * 2 >= 0:
#             n -= 3**i * 2
#             jeesoo.append(2)
#         elif n - 3**i >= 0:
#             n -= 3**i
#             jeesoo.append(1)
#         else:
#             jeesoo.append(0)
#     print(jeesoo)
    
#     for i in range(len(jeesoo)):
#         answer += 3**i * jeesoo[i]
        
#     if n == 2:
#         answer = 2
#     elif n == 1:
#         answer = 1
            
#     return answer

def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        print(n%3)
        n = n // 3
        print(n)
    print(tmp)
    answer = int(tmp, 3)
    return answer