def solution(numbers, hand):
    answer = ''
    
    left = [1,4,7]
    right = [3,6,9]
    mid = [2,5,8,0]
    left_index = [-1, 3]
    right_index = [1, 3]
    
    for number in numbers:
        if number in left:
            answer += 'L'
            left_index = [-1, left.index(number)]
        elif number in right:
            answer += 'R'
            right_index = [1, right.index(number)]
        else:
            mid_index = [0, mid.index(number)]
            left_length = abs(mid_index[0] - left_index[0]) + abs(mid_index[1] - left_index[1])
            right_length = abs(mid_index[0] - right_index[0]) + abs(mid_index[1] - right_index[1])
            if left_length == right_length:
                if hand == "right":
                    answer += 'R'
                    right_index = [0, mid.index(number)]
                else:
                    answer += 'L'
                    left_index = [0, mid.index(number)]
            else:
                if left_length < right_length:
                    answer += 'L'
                    left_index = [0, mid.index(number)]
                else:
                    answer += 'R'
                    right_index = [0, mid.index(number)]

    return answer