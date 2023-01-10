import sys
input = sys.stdin.readline

key_num, cnt = map(int, input().split())

key_words = set()
for i in range(key_num):
    key_word = input().strip()
    key_words.add(key_word)
    # key_words[key_word] = 1

answer = key_num
for i in range(cnt):
    # words = set(map(str, input().strip().split(',')))
    # key_words = key_words - words
    # print(len(key_words))

    words = input().strip().split(',')
    for word in words:
        if word in key_words:
            key_words.remove(word)
            answer -= 1
    print(answer)

    # words = input().strip().split(',')
    # for word in words:
    #     if word in key_words.keys():
    #         if key_words[word] == 1:
    #             key_words[word] = 0
    #             answer -= 1
    # print(answer)