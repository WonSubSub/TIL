from collections import deque

def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    genre_play_dict = {}
    for i in range(len(genres)):
        if genres[i] in genre_dict.keys():
            genre_dict[genres[i]] += plays[i]
        else:
            genre_dict[genres[i]] = plays[i]
        if genres[i] in genre_play_dict.keys():
            genre_play_dict[genres[i]].append([plays[i], i])
        else:
            genre_play_dict[genres[i]] = [[plays[i], i]]
    
    for key in genre_play_dict.keys():
        genre_play_dict[key].sort(key= lambda x: (-x[0], x[1]))
    
    play_list = sorted(list(genre_dict.values()))[::-1]
    popular = []
    for play in play_list:
        for key in genre_dict.keys():
            if genre_dict[key] == play:
                popular.append(key)
                
    for i in range(len(popular)):
        q = deque(genre_play_dict[popular[i]])
        cnt = 0
        while q:
            cnt += 1
            answer.append(q.popleft()[1])
            if cnt == 2:
                break
                
    return answer