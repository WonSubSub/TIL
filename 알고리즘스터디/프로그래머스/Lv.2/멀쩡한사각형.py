def solution(w,h):
    x, y = max(w,h), min(w,h)
    while True:
        if x%y == 0:
            break
        else:
            x, y= y, x%y
    answer = w*h-w-h+y
    return answer