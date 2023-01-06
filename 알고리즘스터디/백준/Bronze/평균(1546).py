n = int(input())
scores = list(map(int, input().split(' ')))

new_scores = []
max_score = max(scores)

for score in scores:
    new_score = (score/max_score) * 100
    new_scores.append(new_score)

def sum(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum
    
print(sum(new_scores)/len(new_scores))