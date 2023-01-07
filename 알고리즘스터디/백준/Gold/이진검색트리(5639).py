# [[[[5], 24, [28]], 30, [45]], 50, [[52, [60]], 98]]

# [[], 50, []]
# [[[], 30, []], 50, []]
# [[[[], 24, []], 30, []], 50, []]
# [[[[[], 5, []], 24, []], 30, []], 50, []]
# [[[[[], 5, []], 24, [[], 28, []]], 30, []], 50, []]
# [[[[[], 5, []], 24, [[], 28, []]], 30, [[], 45, []]], 50, []]
# [[[[[], 5, []], 24, [[], 28, []]], 30, [[], 45, []]], 50, [[], 98, []]]
# [[[[[], 5, []], 24, [[], 28, []]], 30, [[], 45, []]], 50, [[[], 52, []], 98, []]]
# [[[[[], 5, []], 24, [[], 28, []]], 30, [[], 45, []]], 50, [[[], 52, [[], 60, []]], 98, []]]

def insert_node(number, tree):
    if tree == []:
        tree.append(number)
        tree.insert(0,[])
        tree.insert(2,[])
    else:
        if number < tree[1]:
            return insert_node(number, tree[0])
        else:
            return insert_node(number, tree[2])
    return tree

def print_tree(numbers, tree):
    index = [0,2,1]
    for i in range(len(tree)):
        number = tree[index[i]]
        if number in numbers:
            print(number)
        else:
            print_tree(numbers,number)

tree = []
numbers = []
while True:
    try:
        number = int(input())
        numbers.append(number)
        insert_node(number, tree)
    except:
        break
print_tree(numbers, tree)