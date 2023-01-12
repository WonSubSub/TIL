n = int(input())

numbers = list(map(int, input().split()))

answer = 0

max_index = numbers.index(max(numbers[::-1]))
new_numbers = numbers[:max_index+1]
numbers = numbers[max_index+1:]

min_num = min(new_numbers)
# for i in range(len(new_numbers)):


soo_list = []
def soo(soo_list, numbers, i):
    
# [10,11,12,13,14,15,16,5,2,4,1,2,5,3,2,5,4,3,2,3,1,4,2,1]
