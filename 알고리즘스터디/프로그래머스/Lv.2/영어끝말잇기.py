def solution(n, words):
    answer = []
    
    word_dict = {}
    for i in set(words):
        word_dict[i] = 0
    
    cnt = 0
    for i in range(len(words)):
        if i % n == 0:
            cnt += 1
        word_dict[words[i]] += 1
        if word_dict[words[i]] == 2:
            answer = [i%n + 1, cnt]
            break
        elif i != 0 and (words[i][0] != words[i-1][-1]):
            answer = [i%n + 1, cnt]
            break
        else:
            answer = [0, 0]

    return answer