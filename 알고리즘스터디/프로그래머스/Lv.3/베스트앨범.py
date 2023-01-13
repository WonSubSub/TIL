def solution(genres, plays):
    answer = []
    
    genre_dict = {}
    genre_sum = []
    for genre in set(genres):
        genre_dict[genre] = []
    
    for i in range(len(genres)):
        genre_dict[genres[i]].append(plays[i])
        
    for genre in genre_dict.keys():
        genre_sum.append([sum(genre_dict[genre]), genre])
    
    genre_sum.sort(reverse=True)
    
    for i in range(len(genre_sum)):
        g = genre_sum[i][1]
        cnt = 0
        for a in range(len(genre_dict[g])):
            genre_dict[g].sort(reverse=True)
            answer.append(plays.index(genre_dict[g][a]))
            cnt += 1
            if cnt == 2:
                break
    return answer