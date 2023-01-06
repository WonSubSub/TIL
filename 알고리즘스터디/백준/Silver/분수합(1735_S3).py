a, b = map(int, input().split())
c, d = map(int, input().split())

up = a * d + b * c
down = b * d

big, small = max(up, down), min(up, down)

while big % small != 0:
    big, small = small, big % small

divisor = small

print(int(up/small), int(down/small))

# def giyak(up, down):
#     if max(up, down) % min(up, down) == 0:
#         divisor = min(up, down)
#     else:
#         for i in range(int(min(up,down)/2), 0, -1):
#             if up % i == 0 and down % i == 0:
#                 divisor = i
#                 break
#     return int(up/divisor), int(down/divisor)

# up = a * d + b * c
# down = b * d

# a, b = giyak(a, b)
# c, d = giyak(c, d)

# up = a * d + b * c
# down = b * d
# up, down = giyak(up, down)